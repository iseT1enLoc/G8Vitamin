import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import traceback
# Define the log file path
ERROR_LOG_FILE = '/home/teamq-g2-no2/DiabeteDatachain/logs/error.log'

def log_error(message, e):
    os.makedirs(os.path.dirname(ERROR_LOG_FILE), exist_ok=True)
    with open(ERROR_LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        f.write(f"{message}\n")
        f.write(f"{str(e)}\n")
        f.write(f"{traceback.format_exc()}\n")
        f.write('-' * 80 + '\n')

def download_html(cycles, components, local_raw_dir):
    """Fetch HTML content and save it to a local file."""
    """This function is use for analyse the html file"""
    # Ensure the directory exists
    os.makedirs(local_raw_dir, exist_ok=True)

    for cycle in cycles:
        for component in components:
            URL = f"https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component={component}&Cycle={cycle}"
            
            try:
                r = requests.get(URL, timeout=10)  # Added timeout to prevent hanging requests
                
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')

                    # Define a unique file path
                    file_path = os.path.join(local_raw_dir, f"{cycle}_{component}.html")

                    # Save raw HTML to file
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(soup.prettify())

                    print(f"HTML saved to {file_path}")
                else:
                    print(f"Failed to fetch {URL}, Status Code: {r.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"Network error fetching {URL}: {e}")
            except Exception as e:
                print(f"Unexpected error processing {URL}: {e}")

def download_file(url, file_path):
    """Download an XPORT file from a given URL and save it to a local path."""
    try:
        #headers = {"Accept": "application/x-sas-xport"}  # Set header for XPORT file
        r = requests.get(url, stream=True, timeout=20)
        if r.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"Downloaded XPORT file: {file_path}")
        else:
            print(f"Failed to download {url}, Status Code: {r.status_code}")
            log_error(f"Failed to download {url}, Status Code: {r.status_code}", None)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        log_error(f"Error downloading {url}", e)
    except Exception as e:
        print(f"Unexpected error downloading {url}: {e}")
        log_error(f"Unexpected error downloading {url}", e)

def process_data_each_page(cycles, components, local_raw_dir):
    # Ensure the directory exists
    os.makedirs(local_raw_dir, exist_ok=True)

    for cycle in cycles:
        for component in components:
            URL = f"https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component={component}&Cycle={cycle}"
            save_path = local_raw_dir+cycle+"/"+component
            
            os.makedirs(save_path, exist_ok=True)
            print(save_path)

            try:
                r = requests.get(URL, timeout=10)  # Added timeout to prevent hanging requests
                
                if r.status_code == 200:
                    soup = BeautifulSoup(r.content, 'html.parser')
                    if(component in ["Demographics","Dietary","Examination", "Laboratory", "Questionnaire"]):
                        print(cycle)
                        print(component)
                        # Find the table with id="GridView1"
                        table = soup.find("table", {"id": "GridView1"})
                        #print(table)
                        if not table:
                            print(f"No table found for {component} in {cycle}.")
                            continue
                        # Loop through all rows to find .xpt file links
                        for row in table.find_all("tr")[1:]:  # Skip header row
                            cells = row.find_all("td")
                            #print(cells)
                            if len(cells) < 3:
                                continue
                            #handle different cells order in 2017-2020 year
                            data_file_link = cells[3 if cycle == '2017-2020' else 2].find("a")  # 3rd column contains .xpt file link
                            if data_file_link and ".xpt" in data_file_link["href"]:
                                xpt_url = "https://wwwn.cdc.gov" + data_file_link["href"]  # Construct full URL
                                print(xpt_url)
                                xpt_filename = os.path.basename(data_file_link["href"])
                                file_path = os.path.join(save_path, xpt_filename)
                                if os.path.exists(file_path):
                                    print(f"File '{file_path}' exists. Continuing...")
                                    continue                                        
                                #Download the file
                                download_file(xpt_url, file_path)
                        print("processed examination!")                                                        
                    else:
                        print(f"FAIL to download the file {r.status_code}")
                else:
                    print(f"Failed to fetch {URL}, Status Code: {r.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"Network error fetching {URL}: {e}")
            except Exception as e:
                print(f"Unexpected error processing {URL}: {e}")

if __name__ == "__main__":
    cycles = ['1999-2000','2001-2002', '2003-2004', '2005-2006', '2007-2008','2009-2010', '2011-2012', '2013-2014', '2015-2016','2017-2018','2017-2020','2021-2023']
    #components = ["Demographics", "Examination", "Laboratory", "Questionnaire"]
    components = ["Dietary"]
    processed_path = "/home/teamq-g2-no2/DiabeteDatachain/data/processed/"
    raw_path = "/home/teamq-g2-no2/DiabeteDatachain/data/raw/"
    final_path = "/home/teamq-g2-no2/DiabeteDatachain/data/final/"
    print(datetime.now())
    #download_html(cycles=cycles, components=components, local_raw_dir=raw_path)
    process_data_each_page(cycles=cycles, components=components, local_raw_dir=raw_path)
    print(datetime.now())

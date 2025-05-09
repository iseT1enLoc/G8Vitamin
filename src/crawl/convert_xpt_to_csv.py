import os
import pandas as pd

def convert_xpt_to_csv(input_xpt, output_csv):
    """
    Converts a SAS XPT file to CSV.

    :param input_xpt: Path to the input .xpt file
    :param output_csv: Path to save the output .csv file
    """
    try:
        df = pd.read_sas(input_xpt, format='xport')
        df.to_csv(output_csv, index=False)
        print(f"Converted: {input_xpt} → {output_csv}")
    except Exception as e:
        print(f"Error processing {input_xpt}: {e}")

def process_directory(input_dir, output_dir):
    """
    Loops through a directory and converts all .xpt files to .csv.

    :param input_dir: Directory containing .xpt files
    :param output_dir: Directory to save converted .csv files
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if not exists

    for file in os.listdir(input_dir):
        if file.startswith("PAXMIN") :
            continue  # Skip PAXMIN files
        if file.endswith(".xpt") and file.startswith("VID"):
            input_path = os.path.join(input_dir, file)
            print(input_path)
            output_path = os.path.join(output_dir, file.replace(".xpt", ".csv"))
            convert_xpt_to_csv(input_path, output_path)

if __name__ == "__main__":
    #cycles = ['1999-2000','2001-2002', '2003-2004', '2005-2006', '2007-2008','2009-2010']
    cycles = ['2003-2004']
    components = ["Laboratory"]
    # components = ["Dietary"]
    processed_path = "/home/teamq-g2-no2/DiabeteDatachain/data/processed/"
    raw_path = "/home/teamq-g2-no2/DiabeteDatachain/data/raw/"
    final_path = "/home/teamq-g2-no2/DiabeteDatachain/data/final/"

    for cycle in cycles:
        for component in components:
            input_directory = os.path.join(raw_path, cycle, component)
            output_directory = os.path.join(processed_path, cycle, component)
            os.makedirs(input_directory, exist_ok=True)
            process_directory(input_directory, output_directory)

# 🧠 G8Vitamin
## 👨‍🏫 Lecture

| Name            | Role           | Affiliation              |
|-----------------|----------------|---------------------------|
| PhD.Nguyen Gia Tuan Anh  | Lecturer | Department of Information Science and Enginneering, University of Information Technology, HCM VNU |
| BS. Tran Quoc Khanh  | Teaching Assistant | Department of Information Science and Enginneering, University of Information Technology, HCM VNU |
## 👥 Project Members

| Name            | Role                | ID         |
|-----------------|---------------------|------------|
| Nguyen Vo Tien Loc    | Team Leader         | 22520792   |
| Pham Van Duy      | Member      | 22520341   |
| Truong Hoai Bao        | Member   | 22520126   |

## 📌 Overview
This project is aimed to help early predict vitamin D deficiency patients based on general report metrics and relavation demographics information.
![G8Vitamin Logo](media/DS108FINAL.png)

---

## 📁 Folder Structure(Connect author to request full dataset)
```
G8Vitamin/
│
├── media/                  # image for readme
├── docs/                   # document location
├── data/
│   ├── raw/                # Original, immutable data
│   ├── processed/          # Cleaned data
│   └── final/              # Data for trainning
│
├── notebooks/              # Jupyter notebooks for exploration and prototyping
│
├── src/                    # Source code
│   ├── crawl/              # Scripts for crawling data
|   ├── dataprocessing/     # Scripts for data processing
│   ├── dataquality/        # Scripts for evaluating data based on completeness and consistency metrics
│   ├── integration/        # Integration data
│   ├── models/             # Training, evaluation, saving models
|   │   └── experiments/    # Data for trainning
|   │   └── results/        # results store for sheet
│
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to ignore in version control
└── README.md               # Project overview and instructions
```
### ▶️ Demo Video

<p align="center">
  <a href="https://youtu.be/4tsfm1Lk0w0?si=ETV9QOtkRLBwBNwW" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/512px-YouTube_Logo_2017.svg.png" alt="Watch demo on YouTube" width="300"/>
  </a>
</p>

> Click the image above to watch the full demo.

### 📦 Installation and Setup
Accessing the source code of frontend and backend:
- **[Frontend](https://github.com/hoaibao2k4/Healthcare-Clinic)**: built with NextJS.
- **[Backend](https://github.com/duyp6090/private_clinic_management_se104)**: This is backend of website built with Java.
# Clone the repository
```bash
git clone https://github.com/iseT1enLoc/G8Vitamin.git
cd G8Vitamin
```

# (Optional) Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

# Install required dependencies
```
pip install -r requirements.txt
```
## 🤝 Acknowledgements
- [NHANES](https://wwwn.cdc.gov/)
- [Scikit-learn](https://scikit-learn.org/)
- [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/)
## 📬 Contact

For any questions or inquiries, feel free to contact us:

- **Team Representative:** Nguyen Vo Tien Loc 
  📧 Email: locnvt.it@gmail.com
  📱 Phone: +84 398541346



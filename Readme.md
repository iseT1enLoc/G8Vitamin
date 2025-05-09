# 🧠 G8Vitamin

## 📌 Overview
This project is aimed to help early predict vitamin D deficiency patients based on general report metrics and relavation demographics information.

---

## 📁 Folder Structure
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
│   ├── integration/        # Integration data
│   ├── models/             # Training, evaluation, saving models
│
├── models/                 # Trained and serialized models
│
├── outputs/                # Logs, reports, figures
│
├── requirements.txt        # Python dependencies
├── setup.py                # Project installation script (if packaging)
├── .gitignore              # Files to ignore in version control
└── README.md               # Project overview and instructions
```

### 📦 Installation and Setup
```bash
git clone https://github.com/iseT1enLoc/G8Vitamin.git
cd G8Vitamin
```
## 🤝 Acknowledgements
- [NHANES](https://wwwn.cdc.gov/)
- [Scikit-learn](https://scikit-learn.org/)
- [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/)
---

## 📄 License
Copyright (c) 2025 NguyenVoTienLoc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell    
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:                     

The above copyright notice and this permission notice shall be included in   
all copies or substantial portions of the Software.                          

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN    
THE SOFTWARE.

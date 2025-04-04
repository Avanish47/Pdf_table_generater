# Pdf_table_generater

# Extract Tables from PDF

## 📌 Overview
This project extracts tables from PDF files and saves them as Excel worksheets. The script uses `pdfplumber` for PDF parsing and `pandas` for data handling.

## 📂 Folder Structure (After Running)
```
📁 project_folder
 ├── extract_table.py      # Main script for extracting tables
 ├── test3 (1) (1).pdf    # Sample input PDF file
 ├── test6 (1) (1).pdf    # Another sample input PDF file
 ├── 📂 output             # Folder where extracted tables are saved
 │    ├── test3 (1) (1)_tables.xlsx
 │    ├── test6 (1) (1)_tables.xlsx
```

## 🚀 How to Run

### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install required packages:
```bash
pip install pdfplumber pandas openpyxl
```

### 2️⃣ Place PDF Files
Move the PDF files you want to process into the project folder.

### 3️⃣ Run the Script
Execute the Python script:
```bash
python extract_table.py
```

### 4️⃣ View Extracted Tables
The extracted tables will be saved as Excel files inside the `output` folder.

## 🛠 Features
✅ Extracts tables from all pages of a PDF  
✅ Saves tables to separate sheets in Excel  
✅ Skips pages with no tables  
✅ Deletes empty Excel files to avoid 0 KB issues  
✅ Handles errors gracefully  

## ⚠ Notes
- If no tables are found in a PDF, the output Excel file **won't be created**.
- Ensure that the PDFs contain properly formatted tables for best results.

## 📜 License
This project is open-source and free to use!


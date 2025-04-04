import pdfplumber
import pandas as pd
import os
import glob

def extract_tables_from_pdf(pdf_path, output_excel):
    """
    Extracts tables from a PDF file and saves them into an Excel sheet.
    
    :param pdf_path: Path to the input PDF file.
    :param output_excel: Path to the output Excel file.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
                table_found = False  # Track if any tables were extracted
                
                for i, page in enumerate(pdf.pages):
                    print(f"Processing page {i+1} of {pdf_path}...")

                    # Extract tables
                    tables = page.extract_tables()
                    
                    if not tables:  # If no tables found, log and continue
                        print(f"No tables found on page {i+1}.")
                        continue

                    for j, table in enumerate(tables):
                        df = pd.DataFrame(table)  # Convert to DataFrame
                        df.dropna(how="all", inplace=True)  # Remove empty rows
                        df.fillna("", inplace=True)  # Fill None values

                        if not df.empty:
                            sheet_name = f"Page_{i+1}_Table_{j+1}"
                            df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
                            table_found = True  # Mark that at least one table was saved

                if not table_found:  # If no tables were found in the entire PDF
                    print(f"⚠ No tables extracted from {pdf_path}. Skipping file.")
                    os.remove(output_excel)  # Delete the empty Excel file

        print(f"✅ Tables extracted and saved to '{output_excel}' successfully.")

    except Exception as e:
        print(f"❌ Error processing {pdf_path}: {e}")

if __name__ == "__main__":
    pdf_files = glob.glob("*.pdf")  # Get all PDF files in the current directory

    if not pdf_files:
        print("No PDF files found in the directory.")
    else:
        os.makedirs("output", exist_ok=True)  # Ensure output folder exists
        for pdf in pdf_files:
            output_file = os.path.join("output", f"{os.path.splitext(pdf)[0]}_tables.xlsx")
            extract_tables_from_pdf(pdf, output_file)







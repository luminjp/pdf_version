import os
import sys
import fitz  # PyMuPDF

def get_pdf_version(file_path):
    """
    Returns the PDF version of a file by reading the header directly.
    """
    try:
        with open(file_path, "rb") as file:
            header = file.read(8).decode('utf-8', errors='ignore')
            if header.startswith('%PDF-'):
                return header[5:8]  # Extract version number from header
            else:
                return "Unknown format"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def save_as_pdf_1_7(input_pdf_path, output_pdf_path):
    """
    Opens a PDF file with PyMuPDF and saves it as a new file,
    which should be in a more recent PDF version (1.7 compatible).
    """
    try:
        doc = fitz.open(input_pdf_path)
        doc.save(output_pdf_path)
        doc.close()
        print(f"Re-saved {input_pdf_path} as {output_pdf_path} in PDF 1.7-compatible format.")
    except Exception as e:
        print(f"Error converting {input_pdf_path}: {e}")

def list_and_convert_pdfs(directory, convert_to_1_7=False):
    """
    Lists all PDF files in the directory with their versions. Converts files
    to version 1.7 if their version is 1.6 or lower and convert_to_1_7 is True.
    """
    if not os.path.isdir(directory):
        print(f"The path {directory} is not a directory or does not exist.")
        return

    print(f"Listing PDF files in directory: {directory}\n")
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            version = get_pdf_version(file_path)
            if version:
                print(f"File: {filename}, Version: {version}")
                if convert_to_1_7 and version != "Unknown format" and version <= "1.6":
                    # 新しいファイル名に "_1.7" を追加
                    output_pdf_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_1.7.pdf")
                    save_as_pdf_1_7(file_path, output_pdf_path)
            else:
                print(f"File: {filename}, Version: Not readable")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_version_checker.py <directory_path> [-v17]")
        sys.exit(1)

    directory = sys.argv[1]
    convert_to_1_7 = "-v17" in sys.argv

    list_and_convert_pdfs(directory, convert_to_1_7)

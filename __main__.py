import os
import shutil
from helpers.scanned_pdf_to_pdf.scanned_pdf_to_pdf import ScannedPDFToPDF

def main():
    folder = input("Folder name: ")
    try:
        scanned_pdf_to_pdf = ScannedPDFToPDF(folder)
        scanned_pdf_to_pdf.transform_scanned_PDF_to_PDF()

        if os.path.exists(scanned_pdf_to_pdf.main_directory_path + '\pdf_pages'):
            shutil.rmtree(scanned_pdf_to_pdf.main_directory_path + '\pdf_pages')
        
        if os.path.exists(scanned_pdf_to_pdf.main_directory_path + '\images'):
            shutil.rmtree(scanned_pdf_to_pdf.main_directory_path + '\images')
            os.makedirs(scanned_pdf_to_pdf.main_directory_path + '\images')
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
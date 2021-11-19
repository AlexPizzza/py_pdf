import os
from os.path import dirname, abspath
import glob
import shutil
import pytesseract as tess
import progressbar
from pdf2image import pdfinfo_from_path, convert_from_path

from helpers.images_to_pdf.images_to_pdf import ImagesToPDF

class ScannedPDFToPDF:
    bar = None
    main_directory_path = None
    folder_name = ""
    threads = []

    def __init__(self, folder_name):
        self.main_directory_path = dirname(dirname(dirname(abspath(__file__))))
        self.tess_poppler_directory_path = dirname(dirname(abspath(__file__)))
        
        self.folder_name = folder_name
        
        if not os.path.exists(self.main_directory_path + '\\final_pdfs'):
            os.makedirs(self.main_directory_path + '\\final_pdfs')

        if not os.path.exists(self.main_directory_path + '\\final_pdfs' + f'\{self.folder_name}'):
            os.makedirs(self.main_directory_path + '\\final_pdfs' + f'\{self.folder_name}')

        if not os.path.exists(self.main_directory_path + f'\scanned_pdfs\{self.folder_name}\\'):
            raise Exception(
                f"No folder found with name: '{self.folder_name}'!")
        else:
            if not os.path.exists(self.main_directory_path + '\pdf_pages'):
                os.makedirs(self.main_directory_path + '\pdf_pages')
            else:
                shutil.rmtree(self.main_directory_path + '\pdf_pages')
                os.makedirs(self.main_directory_path + '\pdf_pages')
            
            if not os.path.exists(self.main_directory_path + '\images'):
                os.makedirs(self.main_directory_path + '\images')
            else:
                shutil.rmtree(self.main_directory_path + '\images')
                os.makedirs(self.main_directory_path + '\images')
            
            self.pdfs = glob.glob(
                self.main_directory_path + f'\scanned_pdfs\{self.folder_name}\*.pdf')
            self.pdfs_names = [os.path.basename(x) for x in self.pdfs]
            self.pdfs_names = [self.pdfs_names[i][:-4] for i in range(len(self.pdfs_names))]
            for pdf_name in self.pdfs_names:
                if not os.path.exists(self.main_directory_path + f'\images\{pdf_name}'):
                    os.makedirs(self.main_directory_path +
                                f'\images\{pdf_name}')

            tess.pytesseract.tesseract_cmd = self.tess_poppler_directory_path + \
                '\Tesseract\\tesseract.exe'

    def transform_scanned_PDF_to_PDF(self):
        poppler_path = self.tess_poppler_directory_path + "\Poppler\\bin\\"
        
        for pdf_path in self.pdfs:
            pdf_name = os.path.basename(pdf_path)
            pdf_name = pdf_name[:-4]

            info = pdfinfo_from_path(
                pdf_path, userpw=None, poppler_path=poppler_path)

            max_pages = info["Pages"]
            self.bar = progressbar.ProgressBar(maxval=max_pages,
                                               widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

            print("Loading images: ")
            self.bar.start()
            k = 1
            for page in range(1, max_pages+1, 10):
                pages = convert_from_path(pdf_path, first_page=page, last_page=min(
                    page+10-1, max_pages), poppler_path=poppler_path)

                for page_num, img_blob in enumerate(pages):
                    file_name = self.main_directory_path + \
                        f'\images\{pdf_name}\{pdf_name}{k}.png'
                    img_blob.save(file_name, "PNG")
                    self.bar.update(k)
                    k += 1

            self.bar.finish()

            images_to_pdf = ImagesToPDF(pdf_name, self.folder_name)
            images_to_pdf.transform_images_to_PDF()
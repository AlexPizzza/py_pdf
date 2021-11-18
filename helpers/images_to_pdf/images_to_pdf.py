import glob
import os
from os.path import dirname, abspath
import pytesseract as tess
import progressbar
import shutil
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

class ImagesToPDF:
    bar = None
    main_directory_path = None
    folder_name = ""
    final_folder_name = ""
    images = None
    output_file = None

    def __init__(self, folder_name, final_folder_name=""):
        self.main_directory_path = dirname(dirname(dirname(abspath(__file__))))
        self.tesseract_directory_path = dirname(dirname(abspath(__file__)))

        self.folder_name = folder_name
        self.final_folder_name = final_folder_name
        
        if not os.path.exists(self.main_directory_path + '\\final_pdfs'):
            os.makedirs(self.main_directory_path + '\\final_pdfs')

        if self.final_folder_name:
            if not os.path.exists(self.main_directory_path + '\\final_pdfs' + f'\{self.final_folder_name}'):
                os.makedirs(self.main_directory_path + '\\final_pdfs' + f'\{self.final_folder_name}')
        else:
            if not os.path.exists(self.main_directory_path + '\\final_pdfs' + f'\{self.folder_name}'):
                os.makedirs(self.main_directory_path + '\\final_pdfs' + f'\{self.folder_name}')
        
        if not os.path.exists(self.main_directory_path + f'\images\{self.folder_name}'):
            raise Exception(
                f"No folder found with name: '{self.folder_name}'!")
        else:
            self.images = sorted(glob.glob(
                self.main_directory_path + f'\images\{self.folder_name}\*'))

            if not os.path.exists(self.main_directory_path + '\pdf_pages\\' + f'{self.folder_name}'):
                os.makedirs(self.main_directory_path + '\pdf_pages\\' + f'{self.folder_name}')
            else:
                shutil.rmtree(self.main_directory_path + '\pdf_pages\\' + f'{self.folder_name}')
                os.makedirs(self.main_directory_path + '\pdf_pages\\' + f'{self.folder_name}')

            self.output_file = self.main_directory_path + \
                f'\pdf_pages\{self.folder_name}\{self.folder_name}1.pdf'

            tess.pytesseract.tesseract_cmd = self.tesseract_directory_path + \
                '\Tesseract\\tesseract.exe'

            self.bar = progressbar.ProgressBar(maxval=len([name for name in os.listdir(self.main_directory_path + f'\images\{self.folder_name}') if os.path.isfile(os.path.join(self.main_directory_path + f'\images\{self.folder_name}', name))]), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    def image_to_PDF(self, img, i, pdf_file):
        image = Image.open(img)
        if image.format.lower() in ['png', 'jpg', 'jpeg']:
            pdf = tess.image_to_pdf_or_hocr(img, extension='pdf')
            file_str = list(self.output_file)
            file_str[-5] = str(i)

            final_file_str = "".join(file_str)

            with open(final_file_str, "wb+") as output_stream:
                output_stream.write(pdf)

            with open(final_file_str, "rb") as input_stream:
                pdf_transformed = PdfFileReader(input_stream)
                pdf_file.addPage(pdf_transformed.getPage(0))

                if self.final_folder_name:
                    if not os.path.exists(self.main_directory_path + f"\\final_pdfs\{self.final_folder_name}\{self.folder_name}.pdf"):
                        with open(self.main_directory_path + f"\\final_pdfs\{self.final_folder_name}\{self.folder_name}.pdf", "wb") as final_output_stream:
                                    pdf_file.write(final_output_stream)
                    else:
                        with open(self.main_directory_path + f"\\final_pdfs\{self.final_folder_name}\{self.folder_name}.pdf", "ab") as final_output_stream:
                                    pdf_file.write(final_output_stream)
                else:
                    if not os.path.exists(self.main_directory_path + f"\\final_pdfs\{self.folder_name}\{self.folder_name}.pdf"):
                        with open(self.main_directory_path + f"\\final_pdfs\{self.folder_name}\{self.folder_name}.pdf", "wb") as final_output_stream:
                                    pdf_file.write(final_output_stream)
                    else:
                        with open(self.main_directory_path + f"\\final_pdfs\{self.folder_name}\{self.folder_name}.pdf", "ab") as final_output_stream:
                                    pdf_file.write(final_output_stream)

    def transform_images_to_PDF(self):
        print("Loading PDF:")

        self.bar.start()

        i = 1
        pdf_file = PdfFileWriter()
        for img in self.images:
            self.image_to_PDF(img, i, pdf_file)
            self.bar.update(i)
            i += 1

        self.bar.finish()

        if self.final_folder_name:
            print(f"Your PDF is inside the 'final_pdfs\{self.final_folder_name}' folder with the name of: '{self.folder_name}'.")
        else:
            print(f"Your PDF is inside the 'final_pdfs\{self.folder_name}' folder with the name of: '{self.folder_name}'.")     

# !! Uncomment next section if you want to transform images to PDF
# Run "python images_to_pdf.py" in the terminal under this file's folder
# images need to be under the images/your_folder_name

# def main():
#     folder = input("Folder name: ")
#     try:
#         images_to_PDF = ImagesToPDF(folder)
#         images_to_PDF.transform_images_to_PDF()
#     except Exception as error:
#         print(error)

# main()

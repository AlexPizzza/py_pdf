# Images/ScannedPDF to PDF

In this project there are two python files (**main**.py and images_to_pdf.py) which can be used to either transform images to a PDF file or transform scanned PDFs to PDF files.

## Installation

Before running file **'**main**.py'** or **'images_to_pdf.py'** you need to install **Tesseract** and **Poppler** and five python modules:

- **Pytesseract**
- **Progressbar2**
- **PyPDF2**
- **Python Imaging Library (PIL)**
- **Pdf2image**

#### Tesseract

**Link for installing Tesseract:**

[Link to Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

**_!! Install or move the Tesseract folder inside 'helpers' folder !!_**

#### Poppler

**Link for installing Poppler:**

[Link to Poppler](https://blog.alivate.com.au/poppler-windows/)

**_!! Install or Move the Poppler folder inside 'helpers' folder !!_**

#### Python Tesseract

```
pip install pytesseract
```

#### Progressbar2

```
pip install progressbar2
```

#### PyPDF2

```
pip install PyPDF2
```

#### Python Imaging Library (Fork)

```
pip install Pillow
```

#### Pdf2image

```
pip install pdf2image
```

## Usage

### Images to PDF

In order to transform your images to a searchable PDF file follow the next steps:

- **Create a new folder inside the 'images' folder**
- **Place your images inside the newly created folder**
- **Run the 'images_to_pdf.py' file inside the 'helpers/images_to_pdf' directory**
- **Write the name of your newly created folder in the terminal**
- **Your PDF will be inside the 'final_pdfs\your_folder_name'**

### Scanned PDFs to PDFs

In order to transform your raw PDF files to searchable PDF files follow the next steps:

- **Create a new folder inside the 'scanned_pdfs' folder**
- **Place your PDF files inside the newly created folder**
- **Run the '**main**.py' file**
- **Write the name of your newly created folder in the terminal**
- **Your PDFs will be inside the 'final_pdfs\your_folder_name'**

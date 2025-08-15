import fitz # PyMuPDF
import pytesseract
from PIL import Image
from googletrans import Translator
import io
import re

            # Path to Tesseract 
    pytesseract.pytesseract.tesseract_cm = r""C:/Program Files/Tesseract-OCR/tesseract.exe"
    
            # Path to PDF
    pdf_path = r"PROJETO OCR/entrada.pdf"
    output_pdf = r"PROJETO OCR/saída_traduzida.pdf"
    
    translator = Translator ()
    
def inches_to_mm(text):
        
        """in. to mm converter in. text"""
    pattern = r'(\d+(\.\d+?)\s?(in|inch|inches|")\b'
def replace(match):
    inches = float(match.group(1))):
    mm = inches*25.4
    return f"{mm:.2f}mm"
    return re.sub(pattern, replace, text)
    
            # Open to PDF
    pdf_DOcument=fitz.open(pdf_path)
    
    for page_number in range(len(pdf_document[page_number]
           
            # Extraction of txt. blocks
    text_blocks=page.get_text("blocks")
    
    if not text_blocks: 
        
            #  OCR if there is no text
    pix = page.get_pixmap()
    img = image.open(io.BytesIO(pix.tobytes()))
    text = pytesseract.image_to_string(img, lang='eng')
    text = inches_to_mm(text)
        
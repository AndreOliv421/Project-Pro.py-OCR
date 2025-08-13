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
    inches=
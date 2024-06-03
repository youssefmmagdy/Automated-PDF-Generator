#Zimmerkarte mit Schnitten
from pypdf2 import PdfWriter, PdfReader
from pypdf.annotations import FreeText
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def Create_PDF(filename):
    pdf = FPDF(orientation='l', unit='mm', format=(105, 148))
    writer = PdfWriter()
    reader = PdfReader('Zimmerkarte.pdf')
    page1 = reader.pages[0]
    page2 = reader.pages[1]
    # writer.add_blank_page(148,105)
    writer.add_page(page1)
    writer.add_page(page2)
    
    pdf.add_page()
    

    annotation = FreeText(
    text="Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
    font="Arial",
    bold=True,
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    background_color="cdcdcd",
    )
    writer.add_annotation(page_number=0, annotation=annotation)

    with open(filename,'wb') as file:
        writer.write(file)
    pdf.output('new1.pdf')
        
Create_PDF('new.pdf')

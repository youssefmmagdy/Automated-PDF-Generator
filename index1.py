# from PyPDF2 import PdfWriter, PdfReader
# import io
# import requests
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
import pandas as pd
from fpdf import FPDF
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.lib.pagesizes import A6

# connect you to the API
# response = requests.get('https://randomuser/api')
# print(response.status_code) # if 200 success
# print(response.json())
# gender = response.json()['results'][0]['gender']

def Name(i):
    if(i > 210):
        x = 260
        y = 190
        size = 8
    elif(i > 190):
        x = 260
        y = 190
        size = 8.5
    elif(i > 170):
        x = 260
        y = 190
        size = 9    
    elif(i > 160):
        x = 260
        y = 190
        size = 10
    elif(i > 140):
        x = 260
        y = 190
        size = 11
    elif(i > 120):
        x = 260
        y = 190
        size = 12
    elif(i > 100):
        x = 270
        y = 190
        size = 12
    else:
        x = 280
        y = 190
        size = 12
    return [x,y,size]

def Create_PDF(number,name,Room,Arrival,Departure,Breakfast):
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    s = name
    l = Name(pdfmetrics.stringWidth(s,'Arial',12))
    can.setFont('Arial',l[2])
    
    can.setFillColorRGB(0.95,0.5,0)
    can.drawString(l[0],l[1],s)
    can.setFontSize(13)
    can.drawString(290,152,Room)
    can.setFontSize(12)
    can.drawString(280,115,Arrival)
    can.drawString(280,77,Departure)
    
    if(Breakfast == 'Yes'):
        can.drawString(320,40,Breakfast)
        # can.drawImage('tick.html',320,40,20,20)
    else:
        can.drawString(383,40,Breakfast)
    can.save()
    packet.seek(0)
    
    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF
    existing_pdf = PdfReader(open("Zimmerkarte.pdf", "rb"))
    
    output = PdfWriter()
    page1 = existing_pdf.pages[0]
    # page1.scale_by(0.90)
    page2 = existing_pdf.pages[1]
    page1.merge_page(new_pdf.pages[0])
    output.add_page(page1) 
    output.add_page(page2)
   
    output_stream = open(name+'.pdf', 'wb')
    output.write(output_stream)
    output_stream.close()

data = pd.read_excel('book.xlsx')
for i in range(len(data)):
    Create_PDF(i+1,data.iloc[i,0],str(data.iloc[i,1]),str(data.iloc[i,2]),str(data.iloc[i,3]),str(data.iloc[i,4]))
# Create_PDF(0,'Youssef','101','1/1/2024','1/1/2024','Yes')
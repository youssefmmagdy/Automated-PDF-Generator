import pandas as pd

from fpdf import FPDF




def Create_PDF(firstName,lastName,roomNumber,arrival,departure,breakfast,id,corporateCode):

    nameFile = lastName + ', ' + firstName
    width = 148
    height = 105
    pdf = FPDF(orientation='l', unit='mm', format=(height, width))
    pdf.add_page()
    pdf.set_margins(0,0,0)
    pdf.set_auto_page_break(False,0)
    pdf.set_font('Arial', '', 8) # reduce the font size to 8
    pdf.set_text_color(0, 0, 0)
    
    pdf.image('hab-wide-text.png',10, 3, 53, 16, 'PNG')
    pdf.image('hab-wide-text.png',84, 3, 53, 16, 'PNG')
    pdf.set_fill_color(0,0,100)
    pdf.set_xy(0,22)
    pdf.set_font_size(13)
    pdf.set_font('','i')
    pdf.set_text_color(255,255,255)
    w = 'INFORMATIONEN'
    pdf.cell(width/2, 7, w,0,0,'C',True)

    pdf.set_xy(width/2,22)
    w = 'WILLKOMMEN · WELCOME'
    pdf.cell(width/2, 7, w,0,0,'C',True)

    pdf.set_text_color(0,0,100)
    pdf.set_font_size(10)
    pdf.set_font('',style='ub')
    w = 'Frühstück'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,32)
    pdf.cell(pdf.get_string_width(w),2.2,w,'',1,'C')

    x = 3
    y = 30
    w1 = 'Montag bis Freitag'
    w2 = '6:00 bis 10:00 Uhr'
    pdf.set_font_size(8)
    pdf.set_xy(width/4 - pdf.get_string_width(w1)/2 - pdf.get_string_width(w2)/2,37)
    pdf.set_font('',style='b')
    pdf.cell(pdf.get_string_width(w1),0,w1,0,1,'C')
    pdf.set_xy(4+width/4 - pdf.get_string_width(w1)/2 - pdf.get_string_width(w2)/2 + pdf.get_string_width(w2)/2-3,37)
    pdf.set_font('','')

    pdf.cell(width/4+pdf.get_string_width(w2)/2+1,0,w2,0,1,'C')

    pdf.set_xy(x,41)
    pdf.set_font('',style='b')
    w = 'Wochenende & Feiertage'
    pdf.cell(50-x,0,w,0,1,'C')
    pdf.set_xy(46,41)
    pdf.set_font('','')
    w = '7:00 bis 11:00 Uhr'
    pdf.cell(50-y,0,w,0,1,'C')

    pdf.set_font_size(10)
    pdf.set_font('',style='bu')
    w = 'Parken'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,44+1)
    pdf.cell(pdf.get_string_width(w),2,w,'',1,'C')

    pdf.set_font_size(8)
    pdf.set_xy(12,49+1)
    pdf.set_font('','')
    w = 'Parkplätze sind in unserem Parkhaus. Die Einfahrt'
    pdf.cell(50-x,0,w,0,1,'C')
    pdf.set_xy(12,53+1)
    pdf.set_font('','')
    w = 'befindet sich neben dem Kino (kostenpflichtig).'
    pdf.cell(50-x,0,w,0,1,'C')

    pdf.set_font_size(10)
    pdf.set_font('',style='bu')
    w = 'Zimmerreinigung nicht benötigt?'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,57+2)
    pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    pdf.set_font_size(8)
    pdf.set_xy(12,63)
    pdf.set_font('','')
    pdf.cell(50-x,0,'Erhalten Sie ein kostenfreies Getränk',0,1,'C')
    pdf.set_xy(12,67)
    pdf.set_font('','')
    pdf.cell(50-x,0,'bei Verzicht auf die Zimmerreinigung.',0,1,'C')

    pdf.set_font_size(10)
    pdf.set_font('',style='bu')
    w = 'Direkt buchen lohnt sich'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,72)
    pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    pdf.set_font_size(8)
    w = 'Über unsere Webseite erhalten Sie'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,76)
    pdf.set_font('','')
    pdf.cell(pdf.get_string_width(w),0,w,0,1,'C')
    w = 'immer den günstigsten Preis.'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,79)
    pdf.set_font('','')
    pdf.cell(pdf.get_string_width(w),0,w,0,1,'C')

    pdf.set_font_size(10)
    pdf.set_font('',style='bu')
    w = 'W-LAN · Wifi'
    pdf.set_xy(width/4-pdf.get_string_width(w)/2,85)
    pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    pdf.set_font_size(8)
    pdf.set_xy(28,89)
    pdf.set_font('',style='b')
    w = 'SSID:'
    pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')
    pdf.set_xy(37,89)
    pdf.set_font('','')
    w = 'HaB-Guest'
    pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')

    pdf.set_xy(26,93)
    pdf.set_font('',style='b')
    w = 'Passwort:'
    pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')
    pdf.set_xy(40,93)
    pdf.set_font('','')
    w = 'hab.berlin'
    pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')


    pdf.set_xy(0,98)
    pdf.set_font_size(8)
    pdf.set_text_color(255,255,255)
    w = 'www.hab.berlin · info@hab.berlin · 030 4303 6000'
    pdf.cell(width/2, 7, w,0,0,'C',True)
    pdf.set_font_size(9)

    pdf.set_xy(width/2,98)
    w = 'Am Borsigturm 1 · 13507 Berlin'
    pdf.cell(width/2, 7, w,0,0,'C',True)

    pdf.set_draw_color(0,0,100)
    pdf.set_xy(76,32)
    pdf.set_text_color(0,0,100)
    pdf.set_font('','bi')
    w = 'Name'
    pdf.cell(74-10,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76,36)
    w = 'Name'
    pdf.cell(74-10,6,w,'BLR',1,'L',False)

    pdf.set_xy(76,45)
    pdf.set_font('','bi')
    w = 'Zimmernr.'
    pdf.cell(74-10,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76,49)
    w = 'Room No.'
    pdf.cell(74-10,6,w,'BLR',1,'L',False)

    pdf.set_xy(76,58)
    pdf.set_font('','bi')
    w = 'Anreise'
    pdf.cell(74-10,5,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76,62)
    w = 'arrival'
    pdf.cell(74-10,6,w,'BLR',1,'L',False)

    pdf.set_xy(76,71)
    pdf.set_font('','bi')
    w = 'Abreise'
    pdf.cell(74-10,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76,75)
    w = 'departure'
    pdf.cell(74-10,6,w,'BLR',1,'L',False)


    pdf.set_xy(76,84)
    pdf.set_font('','bi')
    w = 'Frühstück'
    pdf.cell(24,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76,89)
    w = 'breakfast'
    pdf.cell(24,6,w,'BLR',1,'L',False)

    pdf.set_xy(76+26,84)
    pdf.set_font('','bi')
    w = 'Ja'
    pdf.cell(18,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76+26,89)
    w = 'Yes'
    pdf.cell(18,6,w,'BLR',1,'L',False)

    pdf.set_xy(76+46,84)
    pdf.set_font('','bi')
    w = 'Nein'
    pdf.cell(18,6,w,'LTR',1,'L',False)

    pdf.set_font('','i')
    pdf.set_xy(76+46,89)
    w = 'No'
    pdf.cell(18,6,w,'BLR',1,'L',False)


    def Name(i):
        if(i > 60):
            pdf.set_xy(85,37)
            pdf.set_font_size(8) 
        elif(i > 58):
            pdf.set_xy(85.5,37)
            pdf.set_font_size(8) 
        elif(i > 56):
            pdf.set_xy(86,37)
            pdf.set_font_size(8.25)     
        elif(i > 53):
            pdf.set_xy(86,37)
            pdf.set_font_size(8.5) 
        elif(i > 50):
            pdf.set_xy(86,37)
            pdf.set_font_size(9) 
        elif(i > 45):
            pdf.set_xy(86,37)
            pdf.set_font_size(9.5)
        elif(i > 40):
            pdf.set_xy(86,37)
            pdf.set_font_size(10) 
        elif(i > 35):
            pdf.set_xy(88,37)
            pdf.set_font_size(10) 
        elif(i > 30):
            pdf.set_xy(89,37)
            pdf.set_font_size(11) 
        elif(i > 25):
            pdf.set_xy(91,37)
            pdf.set_font_size(12) 
        else:
            pdf.set_xy(95,37)
            pdf.set_font_size(12) 

    w = nameFile
    
    x = pdf.get_string_width(w)
    Name(x)
    pdf.set_text_color(0,0,0)
    pdf.cell(x,0,w,0,1)

    pdf.set_xy(100,50)
    pdf.set_font_size(12)
    if (roomNumber != None):
        pdf.cell(0,0,str(roomNumber))

    pdf.set_xy(94,63)
    pdf.cell(0,0,str(arrival))

    pdf.set_xy(94,76)
    pdf.cell(0,0,str(departure))

    # pdf.set_xy(112,90) YES
    pdf.set_xy(132,90)
    pdf.cell(0,0,'X')


    # pdf.add_page()

    # pdf.set_xy(0,0)
    # pdf.set_font_size(13)
    # pdf.set_font('','i')
    # pdf.set_text_color(255,255,255)
    # w = 'INFORMATION'
    # pdf.cell(width/2, 7, w,0,0,'C',True)

    # pdf.set_xy(width/2,0)
    # w = 'ZIMMERKARTE'
    # pdf.cell(width/2, 7, w,0,0,'C',True)

    # pdf.set_text_color(0,0,100)
    # pdf.set_font_size(10)
    # pdf.set_font('',style='ub')
    # w = 'breakfast'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,12)
    # pdf.cell(pdf.get_string_width(w),2.2,w,'',1,'C')

    # x = 3
    # y = 30
    # w1 = 'Monday through Friday'
    # w2 = '6:00 a.m. - 10:00 a.m.'
    # pdf.set_font_size(8)
    # pdf.set_xy(width/4 - pdf.get_string_width(w1)/2 - pdf.get_string_width(w2)/2,18)
    # pdf.set_font('','bi')
    # pdf.cell(pdf.get_string_width(w1),0,w1,0,1,'C')
    # pdf.set_xy(9+width/4 - pdf.get_string_width(w1)/2 - pdf.get_string_width(w2)/2 + pdf.get_string_width(w2)/2-3,18)
    # pdf.set_font('','')
    # pdf.cell(width/4+pdf.get_string_width(w2)/2+1,0,w2,0,1,'C')

    # pdf.set_xy(x,23)
    # pdf.set_font('',style='b')
    # w = 'Weekends & Holidays'
    # pdf.cell(50-x,0,w,0,1,'C')
    # pdf.set_xy(46,23)
    # pdf.set_font('','')
    # w = '7:00 a.m. -  11:00 a.m.'
    # pdf.cell(50-y,0,w,0,1,'C')

    # pdf.set_font_size(10)
    # pdf.set_font('',style='bu')
    # w = 'Parking'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,31)
    # pdf.cell(pdf.get_string_width(w),2,w,'',1,'C')

    # pdf.set_font_size(8)
    # pdf.set_xy(12,36)
    # pdf.set_font('','')
    # w = 'Our parking garage is located next to the cinema.'
    # pdf.cell(50-x,0,w,0,1,'C')
    # pdf.set_xy(12,40)
    # pdf.set_font('','i')
    # w = '(additional cost)'
    # pdf.cell(50-x,0,w,0,1,'C')

    # pdf.set_font_size(10)
    # pdf.set_font('',style='bu')
    # w = 'Room cleaning not required?'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,49)
    # pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    # pdf.set_font_size(8)
    # pdf.set_xy(12,53)
    # pdf.set_font('','')
    # pdf.cell(50-x,0,'Receive a free drink if you choose to',0,1,'C')
    # pdf.set_xy(12,57)
    # pdf.set_font('','')
    # pdf.cell(50-x,0,'cancel the room cleaning service.',0,1,'C')

    # pdf.set_font_size(10)
    # pdf.set_font('',style='bu')
    # w = 'Ready to book your next stay?'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,67)
    # pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    # pdf.set_font_size(8)
    # w = 'Book directly from our website and'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,71)
    # pdf.set_font('','')
    # pdf.cell(pdf.get_string_width(w),0,w,0,1,'C')
    # w = 'always get the best price.'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2,75)
    # pdf.set_font('','')
    # pdf.cell(pdf.get_string_width(w),0,w,0,1,'C')

    # pdf.set_font_size(10)
    # pdf.set_font('',style='bu')
    # w = 'WIFI · W-LAN'
    # pdf.set_xy(width/4-pdf.get_string_width(w)/2-2,84)
    # pdf.cell(pdf.get_string_width(w),0,w,'',1,'C')

    # pdf.set_font_size(8)
    # pdf.set_xy(24,88)
    # pdf.set_font('',style='b')
    # w = 'SSID:'
    # pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')
    # pdf.set_xy(33,88)
    # pdf.set_font('','')
    # w = 'HaB-Guest'
    # pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')

    # pdf.set_xy(23,92)
    # pdf.set_font('',style='b')
    # w = 'Passwort:'
    # pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')
    # pdf.set_xy(37,92)
    # pdf.set_font('','')
    # w = 'hab.berlin'
    # pdf.cell(pdf.get_string_width(w),0,w,0,0,'C')

    # pdf.set_xy(0,98)
    # pdf.set_font_size(8)
    # pdf.set_text_color(255,255,255)
    # w = 'www.hab.berlin · info@hab.berlin · 030 4303 6000'
    # pdf.cell(width/2, 7, w,0,0,'C',True)
    # pdf.set_font_size(9)

    # pdf.set_xy(width/2,98)
    # w = 'Am Borsigturm 1 · 13507 Berlin'
    # pdf.cell(width/2, 7, w,0,0,'C',True)
    # pdf.set_xy(25,25)
    # pdf.cell(10,0,'Yous')

    
    pdf.output('./pdfs/'+nameFile+'.pdf')

data = pd.read_excel('Book.xlsx')
for i in range(len(data)):
    Create_PDF(data.iloc[i,0],data.iloc[i,1],str(data.iloc[i,2]),str(data.iloc[i,3]),str(data.iloc[i,4]),str(data.iloc[i,5]),str(data.iloc[i,6]),str(data.iloc[i,7]))

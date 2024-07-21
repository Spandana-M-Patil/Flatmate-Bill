import webbrowser
import fpdf
import os
class GeneratePdf:
    """
    Create a PDF about the data that contains their name, period of time they spent and 
    their share for that period
    """
    def __init__(self,filename) -> None:
        self.filename = filename
    
    def generate(self,flatmate1, flatmate2, bill):
        pdf = fpdf.FPDF(orientation='portrait', unit='pt', format='A4')
        # Adding page to our pdf
        pdf.add_page()

        # setting font attributes such as, family, size and style for the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h = pdf.font_size * 2.5, txt = 'Flatmate\'s Bill', border=0,align = "C",ln= 1)

        pdf.cell(w=0, h=0, border=1,ln=2)

        # inserting the period the bill is for
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=0, h = pdf.font_size * 2.5, txt = f'Period : {bill.period.capitalize()}', border=0,ln= 1)

        pdf.set_font(family='Times', size=18)
        line_height = pdf.font_size * 1.8
        
        pdf.cell(w=0, h=line_height, border=0,ln=1)

        # Inserting details and due amount of the flatemate 1
        pdf.cell(w=0, h=line_height, border=0, txt=f'Name : {flatmate1.name.capitalize()}',ln=2)
        pdf.cell(w=0, h=line_height, border=0, txt=f'{flatmate1.name.capitalize()}: {flatmate1.pays(bill, flatmate2)}',ln=1)

        pdf.cell(w=0, h=line_height, border=0,ln=1)

        # Inserting details and due amount of the flatmate2
        pdf.cell(w=0, h=line_height, border=0, txt=f'Name : {flatmate2.name.capitalize()}',ln=2)
        pdf.cell(w=0, h=line_height, border=0, txt=f'{flatmate2.name.capitalize()}: {flatmate2.pays(bill, flatmate1)}',ln=1)
        
        # changing the directory to files to generate the pdf and open through browser
        os.chdir('files')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
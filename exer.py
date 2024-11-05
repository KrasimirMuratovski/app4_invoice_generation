from pathlib import Path
from fpdf import FPDF
import glob



filepaths = glob.glob("Text-Files/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')
for filepath in filepaths:
	filename = Path(filepath).stem
	pdf.add_page()
	pdf.set_font('Times' , style='B', size=24)
	pdf.cell(w=20, h=20, text = filename.capitalize())
pdf.output('Animals.pdf')


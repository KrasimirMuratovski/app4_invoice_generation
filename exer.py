from pathlib import Path
from fpdf import FPDF
import glob
from fpdf.enums import XPos, YPos




filepaths = glob.glob("Text-Files/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')
for filepath in filepaths:
	with open(filepath, 'r') as f:
		data = f.read()
	filename = Path(filepath).stem
	pdf.add_page()
	pdf.set_font('Times' , style='B', size=24)
	pdf.cell(w=20, h=20, text = filename.capitalize(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

	pdf.set_font('Times' , style='B', size=10)
	pdf.multi_cell(w=0, h=6, text = data)
pdf.output('Animals.pdf')


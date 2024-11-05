import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
# from fpdf.enums import XPos, YPos



filepaths = glob.glob("invoices/*.xlsx")##
for path in filepaths:
	# df = pd.read_excel(path, sheet_name='Sheet 1')##
	filename = Path(path).stem
	invoice_nr = filename.split('-')[0]
	pdf = FPDF(orientation='P', unit='mm', format='A4')
	pdf.add_page()
	# pdf.set_font()
	pdf.set_font('Times', style = 'B', size=18)
	pdf.cell(w=50, h=12, text = f"Invoice nr.{invoice_nr}")
	# pdf.cell(w=50, h=12, text = "test")
	pdf.output(f"PDFs/{filename}.pdf")


import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
from fpdf.enums import XPos, YPos



filepaths = glob.glob("invoices/*.xlsx")##
for path in filepaths:

	pdf = FPDF(orientation='P', unit='mm', format='A4')
	pdf.add_page()

	filename = Path(path).stem
	invoice_nr, date = filename.split('-')

	pdf.set_font('Times', style = 'B', size=16)
	pdf.cell(w=50, h=12, text = f"Invoice nr.{invoice_nr}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

	pdf.set_font('Times', style = 'B', size=14)
	pdf.cell(w=50, h=12, text = f"Date.{date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

	df = pd.read_excel(path, sheet_name='Sheet 1')##

	columns = list(df.columns)
	# columns = [" ".join(x.split("_")) for x in columns]
	columns = [x.replace("_", " ").title() for x in columns]
	pdf.set_font('Times', size=10)
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=20, h=8, text=" ".join(columns[0].split("_")), border=1)
	pdf.cell(w=80, h=8, text=columns[1], border=1)
	pdf.cell(w=30, h=8, text=columns[2], border=1)
	pdf.cell(w=25, h=8, text=columns[3],border=1)
	pdf.cell(w=20, h=8, text=columns[4], border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
	for index, row in df.iterrows():
		pdf.set_font('Times', size=10)
		pdf.set_text_color(80,80,80)
		pdf.cell(w= 20, h=8, text = str(row["product_id"]), border=1)
		pdf.cell(w= 80, h=8, text = str(row["product_name"]), border=1)
		pdf.cell(w= 30, h=8, text = str(row["amount_purchased"]), border=1)
		pdf.cell(w= 25, h=8, text = str(row["price_per_unit"]), border=1)
		pdf.cell(w= 20, h=8, text = str(row["total_price"]), border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


	pdf.output(f"PDFs/{filename}.pdf")


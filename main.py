import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")
for path in filepaths:
	print(path)
	df = pd.read_excel(path, sheet_name='Sheet 1')
	print(df)
	# break
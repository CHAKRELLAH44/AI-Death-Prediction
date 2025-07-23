import pandas as pd

excel_file = "data/BaseMedicale_Talend.xlsx"
xls = pd.ExcelFile(excel_file)

print("Feuilles disponibles :", xls.sheet_names)

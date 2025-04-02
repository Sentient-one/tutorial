import pandas as pd
df = pd.read_excel('simple_output.xlsx')
print(df)
df_sheet = pd.read_excel('simple_multi_sheet.xlsx', sheet_name='2023')
print("\nData from 2023 sheet:")
print(df_sheet)

all_sheets = pd.read_excel('simple_multi_sheet.xlsx', sheet_name=None)
import pandas as pd


df1 = pd.DataFrame({'Month': ['Jan', 'Feb'], 'Sales': [1000, 1200]})
df2 = pd.DataFrame({'Month': ['Jan', 'Feb'], 'Sales': [1100, 1300]})


with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    df1.to_excel(writer, sheet_name='2023', index=False)
    df2.to_excel(writer, sheet_name='2024', index=False)

print("Multiple sheets written to Excel.")
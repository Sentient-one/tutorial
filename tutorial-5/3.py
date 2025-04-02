import pandas as pd
data = {'Product': ['Laptop', 'Printer', 'Tablet'], 
        'Price': [1200, 150, 300]}

df = pd.DataFrame(data)


df.to_excel('simple_output.xlsx', index=False)
print("Data written to Excel successfully.")
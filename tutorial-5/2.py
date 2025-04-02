import pandas as pd
data = [
    {'Name': 'appu', 'Age': 28, 'City': ' knpy'},
    {'Name': 'achu', 'Age': 24, 'City': 'ktym'},
    {'Name': 'anand', 'Age': 32, 'City': 'ktr'},
    {'Name': 'aravind', 'Age': 29, 'City': 'kollam'}
]

df = pd.DataFrame(data)

df_indexed = df.set_index('Name')
print("DataFrame with 'Name' as index:")
print(df_indexed)
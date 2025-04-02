import pandas as pd

df = pd.read_csv("auto.csv")

df['company'].fillna('Unknown', inplace=True)
df['body-style'].fillna('Unknown', inplace=True)
df['engine-type'].fillna('Unknown', inplace=True)
df['num-of-cylinders'].fillna('Unknown', inplace=True)
df['wheel-base'].fillna(df['wheel-base'].median(), inplace=True)
df['length'].fillna(df['length'].median(), inplace=True)
df['horsepower'].fillna(df['horsepower'].median(), inplace=True)
df['average-mileage'].fillna(df['average-mileage'].median(), inplace=True)
df['price'].fillna(df['price'].median(), inplace=True)

df.drop_duplicates(inplace=True)


df.to_csv("auto_cleaned.csv", index=False)
companies = df.groupby('company')
max_prices = companies['price'].max()
most_expensive_company = max_prices.idxmax()
print(f"Most expensive car company: {most_expensive_company} (${max_prices.max()})")
toyota_cars = df[df['company'].str.lower() == 'toyota']
print("\nToyota car details:")
print(toyota_cars)
car_count = df['company'].value_counts()
print("\nTotal cars by company:")
print(car_count)


max_price_index = df['price'].idxmax()
highest_priced = df.loc[max_price_index]
print("\nHighest priced car:")
print(highest_priced)

avg_mileage = companies['average-mileage'].mean()
print("\nAverage mileage by company:")
print(avg_mileage)

sorted_cars = df.sort_values(by='price', ascending=False)
print("\nCars sorted by price (highest to lowest):")
print(sorted_cars[['company', 'body-style', 'price']])
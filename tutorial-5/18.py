import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')

print("First 10 rows of weather data:")
print(df.head(10))

max_temp = df['temperature'].max()
min_temp = df['temperature'].min()
print(f"\nMaximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")

cool_places = df[df['temperature'] < 28]['place'].unique()
print("\nPlaces with temperature less than 28°C:")
print(cool_places)

cloudy_places = df[df['weather'] == 'Cloudy']['place'].unique()
print("\nPlaces with cloudy weather:")
print(cloudy_places)

weather_counts = df['weather'].value_counts().sort_index()
print("\nWeather frequency (sorted):")
print(weather_counts)

plt.figure(figsize=(12, 6))
plt.bar(df['date'], df['temperature'], color='orangered')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_temperature.png')
plt.show()

print("\nAnalysis complete!")
import pandas as pd
df = pd.read_csv('employee.csv')
print("First 7 records:")
print(df.head(7))

print("\nEmployee names in alphabetical order:")
sorted_names = df['name'].sort_values()
print(sorted_names.tolist())

highest_salary_employee = df.loc[df['salary'].idxmax(), 'name']
print("\nEmployee with highest salary:")
print(highest_salary_employee)
male_employees = df[df['gender'] == 'Male']['name']
print("\nMale employees:")
print(male_employees.tolist())
unique_teams = df['team'].unique()
print("\nTeams:")
print(unique_teams)
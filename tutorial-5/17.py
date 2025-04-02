import pandas as pd

df = pd.read_csv('student.csv')

avg_cgpa = df['CGPA'].mean()
print(f"Average CGPA: {avg_cgpa}")

high_performers = df[df['CGPA'] > 9]
print("\nStudents with CGPA > 9:")
print(high_performers)

cse_high_performers = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("\nCSE students with CGPA > 9:")
print(cse_high_performers)

top_student = df.loc[df['CGPA'].idxmax()]
print("\nStudent with maximum CGPA:")
print(top_student)

branch_avg = df.groupby('Branch')['CGPA'].mean()
print("\nAverage CGPA by branch:")
print(branch_avg)
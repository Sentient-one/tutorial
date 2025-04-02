import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def create_and_read_student_data():
   
    data = {
        'rollno': [101, 102, 103, 104, 105],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'place': ['New York', 'London', 'Paris', 'Sydney', 'Tokyo'],
        'mark': [85, 92, 78, 95, 88]
    }
    
   
    df = pd.DataFrame(data)
    df.to_csv('stud.csv', index=False)
    
    
    df_read = pd.read_csv('stud.csv')
    print("a) File contents:")
    print(df_read)
    
    return df_read
def analyze_student_data():
    df = create_and_read_student_data()
    df.set_index('rollno', inplace=True)
    print("\nb) Data with rollno as index:")
    print(df)
    
   
    print("\nc) Name and mark only:")
    print(df[['name', 'mark']])
    
    \
    df_reset = df.reset_index() 
    sorted_by_name = df_reset.sort_values(by='name')
    print("\nd) Data sorted by name:")
    print(sorted_by_name[['rollno', 'name', 'mark']])
    
    
    sorted_by_mark = df_reset.sort_values(by='mark', ascending=False)
    print("\ne) Data sorted by mark (descending):")
    print(sorted_by_mark[['rollno', 'name', 'mark']])
    
    
    average_mark = df['mark'].mean()
    median_mark = df['mark'].median()
    mode_mark = stats.mode(df['mark']).mode[0]
    
    print("\nf) Statistical measures:")
    print(f"   Average mark: {average_mark}")
    print(f"   Median mark: {median_mark}")
    print(f"   Mode mark: {mode_mark}")
    
    min_mark = df['mark'].min()
    max_mark = df['mark'].max()
    print("\ng) Min and Max marks:")
    print(f"   Minimum mark: {min_mark}")
    print(f"   Maximum mark: {max_mark}")
    
    
    variance = df['mark'].var()
    std_dev = df['mark'].std()
    print("\nh) Variance and Standard Deviation:")
    print(f"   Variance: {variance}")
    print(f"   Standard Deviation: {std_dev}")
    plt.figure(figsize=(8, 6))
    plt.hist(df['mark'], bins=5, edgecolor='black')
    plt.title('Histogram of Student Marks')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('marks_histogram.png') 
    plt.show()
    print("\ni) Histogram of marks has been displayed and saved as 'marks_histogram.png'")

    df_no_place = df.drop('place', axis=1)
    print("\nj) Data after removing place column:")
    print(df_no_place)
    df_no_place.to_csv('stud_no_place.csv')
    print("   Modified data saved to 'stud_no_place.csv'")

if __name__ == "__main__":
    analyze_student_data()
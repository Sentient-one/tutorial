import pandas as pd

def read_and_display_data():
    df = pd.read_csv("auto.csv")
    
    
    print("First five records of the auto.csv file:")
    print(df.head())

if __name__ == "__main__":
    read_and_display_data()
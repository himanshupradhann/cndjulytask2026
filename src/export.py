import os

def export_csv(df):
    df.to_csv("web/data/clean_data.csv",index=False)
    print("Clean data saved to web/data/clean_data.csv")

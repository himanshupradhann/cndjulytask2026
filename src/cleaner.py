import numpy as np

def clean_data(df):

    df.replace([-9999, -8888], np.nan, inplace=True)

    df["pressure"] = df["pressure"] / 100
    df["temperature"] = df["temperature"] / 10
    df["humidity"] = df["humidity"] / 10

    df.dropna(inplace=True)

    df = df.sort_values(by="altitude")

    df.reset_index(drop=True, inplace=True)

    return df
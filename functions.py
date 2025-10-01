import pandas as pd

def clean_open_complaints(df: pd.DataFrame)
   
    df["number_of_open_complaints"] = (df["number_of_open_complaints"].astype(str).str.split('/').str[1] .astype(float))
    return df


def remove_duplicates(df: pd.DataFrame, subset=None, keep="first")
   
    df = df.drop_duplicates(subset=subset, keep=keep)
    return df


def save_cleaned_data(df: pd.DataFrame, filename: str)
   
    df.to_csv(filename, index=False)
    print(f"Cleaned dataset saved to {filename}")
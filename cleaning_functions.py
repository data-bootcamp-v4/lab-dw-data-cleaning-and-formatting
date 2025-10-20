import pandas as pd

def main_cleaning(df):
    """
    Example cleaning function.
    Add your own cleaning steps here.
    """
    # Drop duplicate rows
    df = df.drop_duplicates()

    # Drop rows with missing values
    df = df.dropna()

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    return df
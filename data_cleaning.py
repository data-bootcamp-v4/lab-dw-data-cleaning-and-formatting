import pandas as pd

def to_snake_case(df):
    """
    Standardizes column names by converting them to lowercase and replacing spaces with underscores.
    """
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df

def remove_nans(df):
    """
    Removes rows with missing values from the DataFrame.
    """
    return df.dropna()

def remove_duplicates(df):
    """
    Removes duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def fill_nans_mean(df, column_name):
    """
    Fills missing values in a specific column with the mean.
    """
    df[column_name] = df[column_name].fillna(df[column_name].mean())
    return df

def forward_fill_data(df):
    """
    This function applies forward fill (ffill) to fill missing values in the DataFrame.
    """
    return df.ffill()

def convert_to_float(df, column_name):
    """
    Converts a specified column to float format.
    """
    df[column_name] = df[column_name].astype(float)
    return df
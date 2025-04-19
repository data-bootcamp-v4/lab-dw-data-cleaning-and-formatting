import pandas as pd
import numpy as np

def standardize_column_names(df):
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    return df

def replace_percent_sign(df, column):
    df[column] = df[column].str.replace('%', '', regex=False)
    return df

def convert_column_to_numeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def extract_middle_from_date_string(df, column):
    df[column] = df[column].str.split('/').str[1]
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

def fill_null_with_median(df, column):
    median = df[column].median()
    df[column] = df[column].fillna(median)
    return df

def drop_duplicates_and_reset_index(df):
    df = df.drop_duplicates().reset_index(drop=True)
    return df

def convert_floats_to_ints(df):
    for col in df.select_dtypes(include='float'):
        df[col] = df[col].astype(int)
    return df

def clean_data(df):
    df = standardize_column_names(df)
    df = replace_percent_sign(df, "some_percent_column")
    df = convert_column_to_numeric(df, "some_column")
    df = extract_middle_from_date_string(df, "some_date_column")
    df = fill_null_with_median(df, "income")
    df = drop_duplicates_and_reset_index(df)
    df = convert_floats_to_ints(df)
    return df
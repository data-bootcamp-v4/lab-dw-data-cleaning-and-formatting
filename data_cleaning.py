import pandas as pd

def standardize_column_names(df):
    """ Standardizes column names to lowercase and replaces spaces with underscores. """
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.rename(columns={'st': 'state'}, inplace=True)
    return df

def convert_data_types(df):
    """ Converts relevant columns to proper data types. """
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'].str.replace('%', '', regex=True), errors='coerce')
    df['number_of_open_complaints'] = df['number_of_open_complaints'].astype(str).str.split('/').str[1]
    df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce').astype('Int64')
    return df

def handle_missing_values(df):
    """ Fill null values with column mean for numerical data. """
    df.fillna(df.mean(numeric_only=True), inplace=True)
    return df

def remove_duplicates(df):
    """ Drop duplicate rows and reset index. """
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


import pandas as pd

def load_data(url):
    """Loads data from a specified URL into a DataFrame"""
    return pd.read_csv(url)

def clean_column_names(df):
    """Standardizes column names"""
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('%', 'percent')
    df.rename(columns={'st': 'state'}, inplace=True)
    return df

def fill_nulls(df):
    """Fills nulls in numerical and categorical columns"""
    numerical_columns = df.select_dtypes(include=['number']).columns
    df[numerical_columns] = df[numerical_columns].apply(lambda x: x.fillna(x.median()))
    
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        mode_value = df[column].mode()[0]
        df[column] = df[column].fillna(mode_value)
    return df

def convert_data_types(df):
    """Converts numerical columns to integers where appropriate"""
    numerical_columns = df.select_dtypes(include=['number']).columns
    df[numerical_columns] = df[numerical_columns].astype(int)
    return df

def main_cleaning_function(url):
    """Performs all cleaning and formatting steps"""
    df = load_data(url)
    df = clean_column_names(df)
    df = fill_nulls(df)
    df = convert_data_types(df)
    return df
# data_cleaning.py
# This file contains all functions to clean and format the insurance dataset
# Each function handles a specific step of the data cleaning process

# Step 0 - Import pandas library
# import: loads an external Python package
# pandas: used for data manipulation and analysis
# pd: alias (short name) used for easier access to pandas functions
import pandas as pd

# Step 1 - Function to load CSV data
def load_data(url):
    """
    Load the dataset from a CSV URL into a pandas DataFrame.
    - url: string containing the link or path to the CSV file
    Returns: pandas DataFrame with the raw data
    """
    # pd.read_csv: reads a CSV file from URL or local path and returns a DataFrame
    df = pd.read_csv(url)
    return df  # return the DataFrame to be used in other functions

# Step 2 - Function to clean column names
def clean_column_names(df):
    """
    Standardizes column names for consistency.
    - Converts all column names to lowercase
    - Replaces spaces with underscores
    - Renames 'st' column to 'state'
    """
    # df.columns: gets the column names of the DataFrame
    # str.lower(): converts all column names to lowercase
    # str.replace(" ", "_"): replaces spaces with underscores
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # df.rename(): renames specific columns
    # inplace=True: modifies the DataFrame directly without creating a copy
    df.rename(columns={"st": "state"}, inplace=True)
    return df  # return the cleaned DataFrame

# Step 3 - Function to clean inconsistent or invalid values
def clean_invalid_values(df):
    """
    Standardizes values in key columns:
    - gender: convert all variations to 'M' or 'F'
    - state: replace abbreviations with full state names
    - education: correct inconsistent values
    - customer_lifetime_value: remove % and convert to numeric
    - vehicle_class: group luxury and sports vehicles under 'Luxury'
    """
    # Gender: convert all strings to lowercase, then replace inconsistent values
    df['gender'] = df['gender'].str.lower().replace({
        'female':'F','femal':'F','f':'F',
        'male':'M','m':'M'
    })

    # State: replace state abbreviations with full state names
    df['state'] = df['state'].replace({
        'AZ':'Arizona','Cali':'California','WA':'Washington'
    })

    # Education: replace inconsistent education values
    df['education'] = df['education'].replace({'Bachelors':'Bachelor'})

    # Customer Lifetime Value: remove % symbol and convert to numeric
    # astype(str): ensures values are strings before replacing %
    # str.replace('%',''): removes the % character
    # pd.to_numeric(..., errors='coerce'): converts to numeric, invalid parsing becomes NaN
    df['customer_lifetime_value'] = pd.to_numeric(
        df['customer_lifetime_value'].astype(str).str.replace('%',''), 
        errors='coerce'
    )

    # Vehicle Class: group specific car types under 'Luxury'
    df['vehicle_class'] = df['vehicle_class'].replace({
        'Sports Car':'Luxury',
        'Luxury SUV':'Luxury',
        'Luxury Car':'Luxury'
    })

    return df  # return cleaned DataFrame

# Step 4 - Function to format column data types
def format_data_types(df):
    """
    Ensures columns have the correct data types:
    - customer_lifetime_value: numeric
    - number_of_open_complaints: extract numeric part and convert to int
    """
    # Convert customer_lifetime_value to numeric
    df['customer_lifetime_value'] = pd.to_numeric(
        df['customer_lifetime_value'], 
        errors='coerce'
    )

    # Number of Open Complaints: extract numeric value from string
    # astype(str): convert to string to use split()
    # str.split('/').str[1]: split by '/' and take the middle value
    # pd.to_numeric(..., errors='coerce'): convert to numeric
    df['number_of_open_complaints'] = pd.to_numeric(
        df['number_of_open_complaints'].astype(str).str.split('/').str[1],
        errors='coerce'
    )

    return df  # return formatted DataFrame

# Step 5 - Function to handle null/missing values
def handle_null_values(df):
    """
    Handles missing values:
    - Fill numeric columns with median
    - Fill categorical columns with mode
    - Convert numeric columns to integers
    """
    # Select numeric columns: float64 and int64 types
    numeric_cols = df.select_dtypes(include=['float64','int64']).columns
    for col in numeric_cols:
        # fillna(): replace NaN values
        df[col] = df[col].fillna(df[col].median())  # use median for numeric columns
        df[col] = df[col].astype(int)  # convert to integer

    # Select categorical columns: object type
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        # fill NaN with mode (most common value)
        df[col] = df[col].fillna(df[col].mode()[0])

    return df  # return DataFrame with no nulls

# Step 6 - Main function to run all cleaning steps
def main(url):
    """
    Runs the full data cleaning pipeline:
    1. Load data from CSV
    2. Clean column names
    3. Clean invalid values
    4. Format data types
    5. Handle missing values
    Returns: fully cleaned and formatted DataFrame
    """
    df = load_data(url)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = handle_null_values(df)
    return df
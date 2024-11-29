# data_cleaning.py

import pandas as pd

def load_data(url):
    # Load data from a CSV file
    return pd.read_csv(url)

def clean_column_names(df):
    # Clean column names by converting to lower case, replacing spaces with underscores,
    # and making other specific replacements
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('st', 'state').str.replace('custateomer', 'customer')
    return df

def clean_invalid_values(df):
    # Clean invalid values in specific columns
    # Standardize gender values
    df['gender'] = df['gender'].replace({
        'Femal': 'F', 'female': 'F', 'Female': 'F',
        'Male': 'M', 'male': 'M'
    })
    # Standardize state values
    df['state'] = df['state'].replace({
        'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'
    })
    # Standardize education values
    df['education'] = df['education'].replace('Bachelors', 'Bachelor')
    # Convert customer_lifetime_value to a float
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.rstrip('%').astype('float') / 100
    # Standardize vehicle_class values
    df['vehicle_class'] = df['vehicle_class'].replace({
        'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'
    })
    return df

def format_data_types(df):
    # Format data types of specific columns
    # Convert number_of_open_complaints to numeric
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(lambda x: x.split('/')[1] if isinstance(x, str) else x)
    df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')
    return df

def handle_missing_values(df):
    # Handle missing values in the DataFrame
    # Fill missing gender values with 'Unknown'
    df['gender'] = df['gender'].fillna('Unknown')
    # Fill missing customer_lifetime_value with the mean value
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(df['customer_lifetime_value'].mean())
    # Fill other missing values with 0
    df = df.fillna(0)
    return df

def remove_duplicates(df):
    # Remove duplicate rows from the DataFrame
    df = df.drop_duplicates()
    return df

def main():
    # Main function to perform all data cleaning steps
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    df = load_data(url)  # Load the data
    df = clean_column_names(df)  # Clean the column names
    df = clean_invalid_values(df)  # Clean invalid values
    df = format_data_types(df)  # Format data types
    df = handle_missing_values(df)  # Handle missing values
    df = remove_duplicates(df)  # Remove duplicates
    print(df.head())  # Print the first few rows of the cleaned DataFrame
    print(df.dtypes)  # Print the data types of the cleaned DataFrame

if __name__ == "__main__":
    main()
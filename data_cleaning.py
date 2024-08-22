import pandas as pd

def clean_column_names(df):
    df.columns = [col.lower().replace(" ", "_").replace("%", "") for col in df.columns]
    return df

def standardize_gender(df):
    df["gender"] = df["gender"].map({
        'M': 'Male', 'F': 'Female', 'Femal': 'Female', 'female': 'Female', 'Male': 'Male'
    })
    return df

def standardize_state(df):
    df["state"] = df["state"].map({
        'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington', 'Washington': 'Washington',
        'Arizona': 'Arizona', 'Nevada': 'Nevada', 'Oregon': 'Oregon', 'California': 'California'
    })
    return df

def standardize_education(df):
    df["education"] = df["education"].map({
        'Master': 'Master', 'Bachelor': 'Bachelor', 'High School or Below': 'High School or Below',
        'College': 'College', 'Bachelors': 'Bachelor', 'Doctor': 'Doctor'
    })
    return df

def clean_customer_lifetime_value(df):
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.split('%').str[0].astype(float)
    return df

def standardize_vehicle_class(df):
    df["vehicle_class"] = df["vehicle_class"].map({
        'Four-Door Car': 'Four-Door Car', 'Two-Door Car': 'Two-Door Car', 'SUV': 'SUV',
        'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'
    })
    return df

def clean_number_of_open_complaints(df):
    df['number_of_open_complaints'] = df['number_of_open_complaints'].str.split('/').str[1].astype(int)
    return df

def drop_na_values(df):
    df.dropna(how="all", inplace=True)
    df.dropna(subset=['gender', 'customer_lifetime_value'], how="all", inplace=True)
    df.dropna(axis=1, how='any', inplace=True)
    return df

def remove_duplicates(df):
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    return df

def dataset_cleaning(df):
    df = clean_column_names(df)
    df = standardize_gender(df)
    df = standardize_state(df)
    df = standardize_education(df)
    df = clean_customer_lifetime_value(df)
    df = standardize_vehicle_class(df)
    df = clean_number_of_open_complaints(df)
    df = drop_na_values(df)
    df = remove_duplicates(df)
    
    return df

def save_cleaned_data(df, filename='cleaned_data.csv'):
    df.to_csv(filename, index=False)
    print(f"Cleaned DataFrame has been saved to '{filename}'.")
import pandas as pd
from data_cleaning import dataset_cleaning, save_cleaned_data

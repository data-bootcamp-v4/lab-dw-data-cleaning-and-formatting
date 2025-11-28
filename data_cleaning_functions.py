"""
Data Cleaning and Formatting Functions
Author: Data Analytics Lab
Date: November 2025

This module contains functions for cleaning and formatting insurance customer data.
"""

import pandas as pd
import numpy as np


def load_data(url):
    """
    Load data from a CSV URL.
    
    Parameters:
    url (str): URL of the CSV file
    
    Returns:
    pandas.DataFrame: Loaded dataframe
    """
    df = pd.read_csv(url)
    return df


def clean_column_names(df):
    """
    Clean column names: lowercase, replace spaces with underscores, replace 'st' with 'state'.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned column names
    """
    df_copy = df.copy()
    df_copy.columns = ['customer', 'state', 'gender', 'education', 'customer_lifetime_value', 
                       'income', 'monthly_premium_auto', 'number_of_open_complaints', 
                       'policy_type', 'vehicle_class', 'total_claim_amount']
    return df_copy


def clean_gender_values(df):
    """
    Standardize gender values to 'M' and 'F'.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned gender values
    """
    df_copy = df.copy()
    df_copy['gender'] = df_copy['gender'].replace({
        'Male': 'M', 'Femal': 'F', 'female': 'F', 'MALE': 'M', 'FEMALE': 'F'
    })
    return df_copy


def clean_state_values(df):
    """
    Replace state abbreviations with full names.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned state values
    """
    df_copy = df.copy()
    state_mapping = {
        'AZ': 'Arizona',
        'Cali': 'California', 
        'WA': 'Washington'
    }
    df_copy['state'] = df_copy['state'].replace(state_mapping)
    return df_copy


def clean_education_values(df):
    """
    Replace 'Bachelors' with 'Bachelor'.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned education values
    """
    df_copy = df.copy()
    df_copy['education'] = df_copy['education'].replace('Bachelors', 'Bachelor')
    return df_copy


def clean_customer_lifetime_value(df):
    """
    Remove '%' character from customer lifetime value and convert to numeric.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned customer lifetime value
    """
    df_copy = df.copy()
    df_copy['customer_lifetime_value'] = df_copy['customer_lifetime_value'].astype(str).str.replace('%', '')
    df_copy['customer_lifetime_value'] = pd.to_numeric(df_copy['customer_lifetime_value'], errors='coerce')
    return df_copy


def clean_vehicle_class_values(df):
    """
    Replace luxury vehicle classes with 'Luxury'.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with cleaned vehicle class values
    """
    df_copy = df.copy()
    luxury_mapping = {
        'Sports Car': 'Luxury',
        'Luxury SUV': 'Luxury', 
        'Luxury Car': 'Luxury'
    }
    df_copy['vehicle_class'] = df_copy['vehicle_class'].replace(luxury_mapping)
    return df_copy


def format_number_of_complaints(df):
    """
    Extract middle value from number_of_open_complaints and convert to numeric.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with formatted number of complaints
    """
    df_copy = df.copy()
    df_copy['number_of_open_complaints'] = df_copy['number_of_open_complaints'].astype(str).str.split('/').str[1]
    df_copy['number_of_open_complaints'] = pd.to_numeric(df_copy['number_of_open_complaints'], errors='coerce')
    return df_copy


def handle_null_values(df):
    """
    Handle null values in the dataframe.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with handled null values
    """
    df_copy = df.copy()
    
    # Remove rows with too many null values
    df_copy = df_copy.dropna(thresh=6)
    
    # Fill gender with mode
    if df_copy['gender'].isnull().any():
        gender_mode = df_copy['gender'].mode()[0]
        df_copy['gender'] = df_copy['gender'].fillna(gender_mode)
    
    # Fill customer_lifetime_value with median
    if df_copy['customer_lifetime_value'].isnull().any():
        clv_median = df_copy['customer_lifetime_value'].median()
        df_copy['customer_lifetime_value'] = df_copy['customer_lifetime_value'].fillna(clv_median)
    
    return df_copy


def convert_to_integers(df):
    """
    Convert numeric columns to integers.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe with integer numeric columns
    """
    df_copy = df.copy()
    numeric_columns = ['customer_lifetime_value', 'income', 'monthly_premium_auto', 
                       'number_of_open_complaints', 'total_claim_amount']
    
    for col in numeric_columns:
        df_copy[col] = df_copy[col].astype(int)
    
    return df_copy


def remove_duplicates(df):
    """
    Remove duplicate rows and reset index.
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Dataframe without duplicates
    """
    df_copy = df.copy()
    df_copy = df_copy.drop_duplicates(keep='first')
    df_copy = df_copy.reset_index(drop=True)
    return df_copy


def main_cleaning_pipeline(url):
    """
    Main function that performs all cleaning and formatting steps.
    
    Parameters:
    url (str): URL of the CSV file to clean
    
    Returns:
    pandas.DataFrame: Fully cleaned and formatted dataframe
    """
    print("Starting data cleaning pipeline...")
    
    # Load data
    print("1. Loading data...")
    df = load_data(url)
    print(f"   Loaded data with shape: {df.shape}")
    
    # Clean column names
    print("2. Cleaning column names...")
    df = clean_column_names(df)
    
    # Clean values
    print("3. Cleaning invalid values...")
    df = clean_gender_values(df)
    df = clean_state_values(df)
    df = clean_education_values(df)
    df = clean_customer_lifetime_value(df)
    df = clean_vehicle_class_values(df)
    
    # Format data types
    print("4. Formatting data types...")
    df = format_number_of_complaints(df)
    
    # Handle null values
    print("5. Handling null values...")
    df = handle_null_values(df)
    print(f"   Shape after handling nulls: {df.shape}")
    
    # Convert to integers
    print("6. Converting to integers...")
    df = convert_to_integers(df)
    
    # Remove duplicates
    print("7. Removing duplicates...")
    df = remove_duplicates(df)
    print(f"   Final shape: {df.shape}")
    
    print("Data cleaning pipeline completed!")
    return df


if __name__ == "__main__":
    # Example usage
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    cleaned_df = main_cleaning_pipeline(url)
    print(f"\nFinal cleaned dataframe info:")
    print(cleaned_df.info())

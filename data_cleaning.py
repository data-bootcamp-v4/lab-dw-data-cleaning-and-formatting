{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
import pandas as pd

def find_middle_value(complaint_str):
    if isinstance(complaint_str, str):
        split_string = complaint_str.split('/')
        if len(split_string) == 3:
            return split_string[1]
    return None

def clean_number_of_open_complaints(df):
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(find_middle_value)
    df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')
    return df

def fill_null_values(df):
    # Fill numerical columns with mean
    if 'customer_age' in df.columns:
        df['customer_age'].fillna(df['customer_age'].mean(), inplace=True)
    if 'number_of_open_complaints' in df.columns:
        df['number_of_open_complaints'].fillna(df['number_of_open_complaints'].mean(), inplace=True)
    
    # Fill categorical columns with mode
    if 'education' in df.columns:
        df['education'].fillna(df['education'].mode()[0], inplace=True)
    
    return df

def clean_data(df):
    """Main function to perform all cleaning and formatting."""
    df = clean_number_of_open_complaints(df)
    df = fill_null_values(df)
    return df

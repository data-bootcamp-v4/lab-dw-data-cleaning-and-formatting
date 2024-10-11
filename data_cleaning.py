# data_cleaning.py
import pandas as pd

def rename_columns(df):
    """Rename columns to standardize the names."""
    df.columns = [
        'customer', 'state', 'gender', 'education', 'customer_lifetime_value',
        'income', 'monthly_premium_auto', 'number_of_open_complaints',
        'policy_type', 'vehicle_class', 'total_claim_amount'
    ]
    return df

def replace_values(df):
    """Replace specific values to clean up inconsistent data entries."""
    # Clean 'gender' column
    df['gender'] = df['gender'].replace({"Femal": "F", "female": "F", "Male": "M"})
    
    # Clean 'state' column
    df['state'] = df['state'].replace({"Cali": "California", "AZ": "Arizona", "WA": "Washington"})
    
    # Clean 'education' column
    df['education'] = df['education'].replace({"Bachelors": "Bachelor"})
    
    # Consolidate 'vehicle_class' column
    df['vehicle_class'] = df['vehicle_class'].replace(
        {"Sports Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"}
    )
    
    return df

def clean_customer_lifetime_value(df):
    """Remove % sign from 'customer_lifetime_value' column and convert it to float."""
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace("%", "").astype(float)
    return df

def clean_open_complaints(df):
    """Convert 'number_of_open_complaints' to integer, extracting the last part if it contains a '/'."""
    df.number_of_open_complaints = df.number_of_open_complaints.astype(str).fillna("0")
    df["number_of_open_complaints"] = df["number_of_open_complaints"].apply(lambda x: int(x.split("/")[1]) if len(x.split("/")) > 1 else 0)
    return df

def fill_missing_values(df):
    """Fill missing values in specific columns."""
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(df['customer_lifetime_value'].mean())
    return df

def drop_missing_data(df):
    """Drop rows and columns with missing data according to specific thresholds."""
    df = df.dropna(thresh=10)
    df = df.dropna(axis=1, how='any')
    return df

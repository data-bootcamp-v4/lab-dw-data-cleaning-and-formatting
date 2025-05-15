import pandas as pd

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def standardize_column_names(df):
    """Standardizes column names: lowercase and replaces spaces with underscores."""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df.rename(columns={"st": "state"}, inplace=True)
    return df

def clean_gender(df):
    """Standardizes gender values."""
    df["gender"] = df["gender"].str.lower().replace({"female": "F", "femal": "F", "f": "F", "male": "M", "m": "M"})
    return df

def clean_state(df):
    """Replaces state abbreviations with full names."""
    state_mapping = {"AZ": "Arizona", "Cali": "California", "WA": "Washington"}
    df["state"] = df["state"].replace(state_mapping)
    return df

def clean_education(df):
    """Standardizes education levels."""
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})
    return df

def clean_customer_lifetime_value(df):
    """Removes '%' and converts Customer Lifetime Value to numeric."""
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(str).str.replace("%", "").astype(float)
    return df

def clean_vehicle_class(df):
    """Standardizes vehicle class by grouping luxury cars."""
    df["vehicle_class"] = df["vehicle_class"].replace({"Sports Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"})
    return df

def fix_open_complaints(df):
    """Extracts the middle value from 'Number of Open Complaints' format."""
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str).apply(lambda x: x.split("/")[1] if "/" in x else x).astype(float)
    return df

def handle_missing_values(df):
    """Handles missing values using different strategies."""
    df["customer_lifetime_value"].fillna(df["customer_lifetime_value"].median(), inplace=True)
    df["income"].fillna(df["income"].median(), inplace=True)
    df["monthly_premium_auto"].fillna(df["monthly_premium_auto"].mean(), inplace=True)
    df["number_of_open_complaints"].fillna(df["number_of_open_complaints"].mode()[0], inplace=True)
    df["total_claim_amount"].fillna(df["total_claim_amount"].median(), inplace=True)
    
    df.dropna(subset=["customer"], inplace=True)  # Drop rows where customer ID is missing
    df["state"].fillna("Unknown", inplace=True)
    df["gender"].fillna("Unknown", inplace=True)
    df["education"].fillna(df["education"].mode()[0], inplace=True)
    df["policy_type"].fillna(df["policy_type"].mode()[0], inplace=True)
    df["vehicle_class"].fillna(df["vehicle_class"].mode()[0], inplace=True)
    
    return df

def convert_numeric_columns(df):
    """Converts all numeric columns to integers."""
    numeric_columns = df.select_dtypes(include=["number"]).columns
    df[numeric_columns] = df[numeric_columns].astype(int)
    return df

def remove_duplicates(df):
    """Removes duplicate rows and resets index."""
    df = df.drop_duplicates(keep="first")
    df.reset_index(drop=True, inplace=True)
    return df

def save_cleaned_data(df, output_filepath):
    """Saves the cleaned dataset to a CSV file."""
    df.to_csv(output_filepath, index=False)
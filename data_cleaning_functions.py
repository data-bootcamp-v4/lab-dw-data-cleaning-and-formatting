#Clean Columns
def rename_columns(df):
    """Rename DataFrame columns to specified names."""
    df.columns = [
        'customer', 'state', 'gender', 'education', 'customer_lifetime_value',
        'income', 'monthly_premium_auto', 'number_of_open_complaints',
        'policy_type', 'vehicle_class', 'total_claim_amount'
    ]
    return df


#clean_values()
def replace_gender(df):
    """Replace gender values with standardized values."""
    df["gender"] = df["gender"].replace({'Femal': 'F', 'Male': 'M', 'female': 'F'})
    return df
def replace_state(df):
    """Replace state abbreviations with full names."""
    df["state"] = df["state"].replace({'Cali': 'California', 'AZ': 'Arizona', 'WA': 'Washington'})
    return df

def replace_education(df):
    """Standardize education values."""
    df["education"] = df["education"].replace({'Bachelors': 'Bachelor'})
    return df

def strip_percentage(df):
    """Strip the percentage sign from the customer lifetime value column."""
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.strip('%').astype(float)
    df["customer_lifetime_value"]=pd.to_numeric(df["customer_lifetime_value"])
    return df
    
def replace_vehicle_class(df):
    """Standardize vehicle class values."""
    df["vehicle_class"] = df["vehicle_class"].replace({'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'})
    return df

#clean_data_type
def process_open_complaints(df):
    """Extract and convert the second part of the number_of_open_complaints."""
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.split('/').str[1]
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors='coerce')
    return df

# clean_missing_values
def clean_dataframe(df):
    # Drop rows with any NaN values
    df_cleaned = df.dropna()

    # Select numeric columns and convert them to int
    numeric_cols = df_cleaned.select_dtypes(include=["float64"]).columns
    df_cleaned[numeric_cols] = df_cleaned[numeric_cols].astype(int)

    # Select object columns and convert them to numeric, coercing errors to NaN
    object_cols = df_cleaned.select_dtypes(include=["object"]).columns
    for col in object_cols:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

    # Fill NaN values with 0
    df_cleaned.fillna(0, inplace=True)

    # Convert all columns to int
    df_cleaned = df_cleaned.astype(int)

    return df_cleaned
    
def clean_duplicates(df):
    df_clean_duplicate=df.drop_duplicates(keep="first")
    new_duplicates= df_clean_duplicate.duplicated()
    df_clean_duplicate.reset_index(drop=True, inplace=True)
    return df_clean_duplicate, new_duplicates
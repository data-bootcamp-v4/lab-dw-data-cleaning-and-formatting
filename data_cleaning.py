# data_cleaning.py
import pandas as pd

# -------------------------
# Function 1: Standardize column names
# -------------------------
def clean_column_names(df):
    def clean_column(name):
        name = name.lower().strip().replace(" ", "_")
        if name == "st":
            name = "state"
        return name
    df.columns = [clean_column(col) for col in df.columns]
    return df

# -------------------------
# Function 2: Clean invalid values
# -------------------------
def clean_invalid_values(df):
    # Gender
    gender_map = {'f': 'F', 'female': 'F', 'femal': 'F', 'm': 'M', 'male': 'M'}
    df['gender'] = df['gender'].str.strip().str.lower().map(gender_map)

    # State
    state_map = {'az': 'arizona', 'wa': 'washington', 'cali': 'california'}
    df['state'] = df['state'].str.strip().str.lower().replace(state_map)

    # Education
    df['education'] = df['education'].str.strip().replace({'Bachelors': 'Bachelor'})

    # Customer lifetime value (remove %)
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(str).str.replace('%', '', regex=False)

    # Vehicle class
    df['vehicle_class'] = df['vehicle_class'].replace({
        'Sports Car': 'Luxury',
        'Luxury SUV': 'Luxury',
        'Luxury Car': 'Luxury'
    })

    return df

# -------------------------
# Function 3: Format data types
# -------------------------
def format_data_types(df):
    # Customer lifetime value → numeric
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')

    # Number of open complaints → extract middle value → numeric
    df['number_of_open_complaints'] = (
        df['number_of_open_complaints'].astype(str).str.split('/').str[1]
    )
    df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce')

    return df

# -------------------------
# Function 4: Handle null values
# -------------------------
def handle_null_values(df):
    # Numeric columns → fill with median
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Categorical columns → fill with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Convert numeric columns to integers
    for col in numeric_cols:
        df[col] = df[col].astype(int)

    return df

# -------------------------
# Function 5: Remove duplicates
# -------------------------
def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    df.reset_index(drop=True, inplace=True)
    return df

# -------------------------
# Main function
# -------------------------
def clean_insurance_data(df):
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = handle_null_values(df)
    df = remove_duplicates(df)
    return df
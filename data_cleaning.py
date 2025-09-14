import pandas as pd
import numpy as np

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.rename(columns={'st': 'state'}, inplace=True)
    return df

# df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
# df.rename(columns={'st': 'state'}, inplace=True)

def clean_invalid_values(df):
    state_map = {
        'AZ': 'Arizona', 'CA': 'California', 'WA': 'Washington',
        'NV': 'Nevada', 'OR': 'Oregon', 'Cali': 'California'
    }
    df['state'] = df['state'].replace(state_map)
    # In education, "Bachelors" could be replaced by "Bachelor
    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})
    # In Customer Lifetime Value, delete the % character
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '', regex=False)
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')
    # In vehicle class, "Sports Car", "Luxury SUV" and "Luxury Car" could be replaced by "Luxury"
    df['vehicle_class'] = df['vehicle_class'].replace({'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'})
    df['gender'] = df['gender'].str.strip().str.upper().replace({'male': 'M', 'female': 'F', 'nan': None})
    return df

def format_data_types(df):
    # Customer lifetime value should be numeric
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce').astype(float).round(2)
    if 'number_of_open_complaints' in df.columns:
        df['number_of_open_complaints'] = df['number_of_open_complaints'].astype(str).str.split('/').str[1]
        df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce').astype('Int64')
    return df

# # Customer lifetime value should be numeric
# df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce').astype(float).round(2)
# df['number_of_open_complaints'] = df['number_of_open_complaints'].str.split('/').str[1]
# df['number_of_open_complaints'] = pd.to_numeric(df['number_of_open_complaints'], errors='coerce').astype('Int64')

def drop_all_null_rows(df):
    return df.dropna(how='all').reset_index(drop=True)

# Step 1: Drop rows that are entirely NaN
# df = df.dropna(how='all').reset_index(drop=True)

def fill_nulls(df):
    # Impute numerical columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.median()))
    # for col in numeric_cols:
    #     df[col] = df[col].fillna(df[col].median())
    # Impute categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))
    # for col in cat_cols:
    #     if df[col].isnull().sum() > 0:
    #         mode = df[col].mode()[0] if not df[col].mode().empty else ''
    #         df[col] = df[col].fillna(mode)
    return df

# --> Step 2: Impute numerical columns with median
# numerical_cols = ['customer_lifetime_value', 'income', 'monthly_premium_auto', 'number_of_open_complaints', 'total_claim_amount']
# numerical_cols = df.select_dtypes(include=['number']).columns
# df[numerical_cols] = df[numerical_cols].apply(lambda x: x.fillna(x.median()))
# --> Step 3: Impute categorical columns with mode
# categorical_cols = ['customer', 'state', 'gender', 'education', 'policy_type', 'vehicle_class']
# categorical_cols = df.select_dtypes(include=['object']).columns
# df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

def convert_numeric_to_int(df: pd.DataFrame) -> pd.DataFrame:
    # Convert numeric columns to integers (if appropriate)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    for col in numeric_cols:
        df[col] = df[col].astype(int)
    return df

# --> Step 5: Convert numeric columns to integers (if appropriate)
# for col in numerical_cols:
#     df[col] = df[col].astype(int)
    # df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().reset_index(drop=True)

# Drop all duplicates, keeping the first occurrence
# df = df.drop_duplicates().reset_index(drop=True)

def reset_index(df: pd.DataFrame) -> pd.DataFrame:
    # Reset the index to ensure consistency.
    df = df.reset_index(drop=True)

# def save_to_csv_file(df: pd.DataFrame):
#     # Save Cleaned Data to CSV
#     df.to_csv('cleaned_data.csv', index=False)

def data_cleaning_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = drop_all_null_rows(df)
    df = fill_nulls(df)
    df = convert_numeric_to_int(df)
    df = drop_duplicates(df)
    df = reset_index(df)
    # df = save_to_csv_file(df)
    return df

# Optionally, add a main block for script use
# if __name__ == "__main__":
#     file_path = "your_file_path.csv"
#     df = pd.read_csv(file_path)
#     df_cleaned = data_cleaning_pipeline(df)
#     df_cleaned.to_csv("cleaned_data.csv", index=False)
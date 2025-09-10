# cleaning_utils.py
import pandas as pd

# Step 1: load data
def load_data(path):
    return pd.read_csv(path)

# Step 2: clean column names
def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

# Step 3: clean invalid values
def clean_invalid_values(df):
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.upper().str.strip()
        df['gender'] = df['gender'].replace({'FEMALE':'F', 'MALE':'M'})
# Clean customer_lifetime_value: remove % and convert to float    
if 'customer_lifetime_value' in df.columns:    
    df['customer_lifetime_value'] =   df['customer_lifetime_valu    .astype(     .str.replace('%' '', regex=F      .astype(loat)        )

    return df

# Step 4: handle null values
def handle_nulls(df):
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

# Step 5: drop duplicates
def drop_dupes(df):
    return df.drop_duplicates()

# Step 6: main function (calls all steps)
def clean_data(path, save_path="cleaned.csv"):
    df = load_data(path)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = handle_nulls(df)
    df = drop_dupes(df)
    df.to_csv(save_path, index=False)
    return df
    

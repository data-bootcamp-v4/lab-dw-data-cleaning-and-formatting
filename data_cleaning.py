# data_cleaning.py
import pandas as pd
import logging

# Set up logging configuration
logging.basicConfig(
    filename='cleaning_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w' 
)

def handle_duplicates(df):
    initial_count = len(df)
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    dropped = initial_count - len(df)
    logging.info(f"DUPLICATES: Removed {dropped} duplicate rows.")
    return df

def handle_nulls(df, id_column='customer'):
    # Strategy 1: Drop critical missing IDs
    if id_column in df.columns:
        initial_rows = len(df)
        df = df.dropna(subset=[id_column])
        dropped_rows = initial_rows - len(df)
        logging.info(f"NULLS: Dropped {dropped_rows} rows due to missing '{id_column}' ID.")
    
    # Strategy 2: Numeric -> Median
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            df[col] = df[col].fillna(df[col].median())
            logging.info(f"NULLS: Filled {null_count} missing values in numeric column '{col}' with Median.")
        
    # Strategy 3: Categorical -> Mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        null_count = df[col].isnull().sum()
        if null_count > 0:
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            logging.info(f"NULLS: Filled {null_count} missing values in categorical column '{col}' with Mode ({mode_val}).")
            
    return df

def format_types(df):
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        df[col] = df[col].astype(int)
    logging.info(f"FORMATTING: Converted {len(num_cols)} columns to integer type.")
    return df

def full_clean_process(file_path, output_path):
    logging.info(f"--- STARTING NEW CLEANING JOB ---")
    logging.info(f"Source: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        original_shape = df.shape
        
        # Run Pipeline
        df = handle_duplicates(df)
        df = handle_nulls(df)
        df = format_types(df)
        
        # Save
        df.to_csv(output_path, index=False)
        final_shape = df.shape
        
        # Final Summary Logging
        logging.info(f"--- FINAL SUMMARY ---")
        logging.info(f"Original Data Shape: {original_shape[0]} rows, {original_shape[1]} columns")
        logging.info(f"Cleaned Data Shape:  {final_shape[0]} rows, {final_shape[1]} columns")
        logging.info(f"Total Rows Removed:  {original_shape[0] - final_shape[0]}")
        logging.info(f"Output saved to:     {output_path}")
        logging.info(f"--- CLEANING COMPLETE ---")
        
        return df
        
    except Exception as e:
        logging.error(f"CRITICAL ERROR during cleaning: {e}")
        raise
### BASIC STARTUPS
import pandas as pd

def clean_fix(row, dict):
    """
    takes a row and a dictionary with (1 value per key), converts all keys on the dictionary into it's value equivalent.
    """
    if pd.notna(row):
        if '/' in row and len(row.split('/')) == 3:
            parts = row.split('/')
            row = parts[1]
        
        for key, value in dict.items():
            if row in value:
                return key        
    return row

def col_int(row, df, col_list, type):
    """
    takes a database, a list of columns and converts them into the type specified.
    """
    for col in col_list:
        try:
            df[col] = df[col].astype(type)
        except:
            print(f"FunctionError: {col} could not be converted.")

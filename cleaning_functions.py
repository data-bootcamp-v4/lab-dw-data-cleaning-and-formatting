import pandas as pd
import numpy as np


def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.rename(columns={"st": "state"})
    return df 



def clean_invalid_values(df):
   
    df["gender"] = (df["gender"].astype(str).str.strip().str.upper()
                    .replace({"MALE": "M", "FEMALE": "F", "FEMAL": "F"}))
    
    
    df["state"] = df["state"].replace({
        "Cali": "California",
        "AZ": "Arizona",
        "WA": "Washington"
    })
    
    
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})
    
    
    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury Car": "Luxury",
        "Luxury SUV": "Luxury"
    })
    
    return df


def clean_clv(df):
    df["customer_lifetime_value"] = (
        df["customer_lifetime_value"].astype(str)
        .str.replace("%", "", regex=False)
        .str.replace("+", "", regex=False)
        .astype(float) / 100
    )
    df["customer_lifetime_value"] = df["customer_lifetime_value"].round(2)
    return df


def clean_open_complaints(df):
    splits = df["number_of_open_complaints"].astype(str).str.split("/", expand=True)
    df["number_of_open_complaints"] = pd.to_numeric(splits[1], errors="coerce").fillna(0).astype(int)
    return df


def handle_nulls(df):
    num_cols = df.select_dtypes(include=["number"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns
    
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
    
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    return df


def remove_duplicates(df):
    df = df.drop_duplicates(keep="first")
    df = df.reset_index(drop=True)
    return df


def clean_data(df):
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = clean_clv(df)
    df = clean_open_complaints(df)
    df = handle_nulls(df)
    df = remove_duplicates(df)
    return df

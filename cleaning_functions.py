import pandas as pd
import numpy as np

def clean_column_names(data_cleaning):
    data_cleaning.columns = (
        data_cleaning.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("st", "state")
    )
    return data_cleaning

def clean_invalid_values(data_cleaning):
    data_cleaning["gender"] = data_cleaning["gender"].replace({
        "Femal": "F",
        "female": "F",
        "Female": "F",
        "F": "F",
        "Male": "M",
        "male": "M",
        "M": "M"
    })

    data_cleaning["state"] = data_cleaning["state"].replace({
        "AZ": "Arizona",
        "WA": "Washington",
        "Cali": "California"
    })

    data_cleaning["education"] = data_cleaning["education"].replace({
        "Bachelors": "Bachelor"
    })

    data_cleaning["customer_lifetime_value"] = data_cleaning["customer_lifetime_value"].str.replace("%", "", regex=False)

    data_cleaning["vehicle_class"] = data_cleaning["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })
    return data_cleaning

def format_data_types(data_cleaning):
    data_cleaning["customer_lifetime_value"] = pd.to_numeric(
        data_cleaning["customer_lifetime_value"], errors="coerce"
    )

    data_cleaning["number_of_open_complaints"] = (
        data_cleaning["number_of_open_complaints"]
        .astype(str)
        .str.split("/")
        .str[1]
    )

    data_cleaning["number_of_open_complaints"] = pd.to_numeric(
        data_cleaning["number_of_open_complaints"], errors="coerce"
    )
    return data_cleaning

def handle_nulls(data_cleaning):
    numeric_cols = data_cleaning.select_dtypes(include=["number"]).columns
    for col in numeric_cols:
        data_cleaning[col] = data_cleaning[col].fillna(data_cleaning[col].mean())

    categorical_cols = data_cleaning.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        data_cleaning[col] = data_cleaning[col].fillna(data_cleaning[col].mode()[0])

    for col in numeric_cols:
        data_cleaning[col] = data_cleaning[col].round().astype(int)

    return data_cleaning

def remove_duplicates(data_cleaning):
    data_cleaning = data_cleaning.drop_duplicates().reset_index(drop=True)
    return data_cleaning

def clean_data(data_cleaning):
    data_cleaning = clean_column_names(data_cleaning)
    data_cleaning = clean_invalid_values(data_cleaning)
    data_cleaning = format_data_types(data_cleaning)
    data_cleaning = handle_nulls(data_cleaning)
    data_cleaning = remove_duplicates(data_cleaning)
    return data_cleaning

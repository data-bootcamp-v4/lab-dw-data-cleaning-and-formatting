import pandas as pd


def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.rename(columns={"st": "state"})
    return df


def clean_gender(df):
    df["gender"] = df["gender"].replace({
        "M": "M",
        "Male": "M",
        "F": "F",
        "female": "F",
        "Femal": "F"
    })
    return df


def clean_state(df):
    df["state"] = df["state"].replace({
        "AZ": "Arizona",
        "Cali": "California",
        "WA": "Washington"
    })
    return df


def clean_education(df):
    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })
    return df


def clean_customer_lifetime_value(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"], errors="coerce")
    return df


def clean_vehicle_class(df):
    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })
    return df


def clean_open_complaints(df):
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str).str.split("/").str[1]
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce")
    return df


def fill_null_values(df):
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def convert_numeric_to_int(df):
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].astype(int)
    return df


def remove_duplicates(df):
    df = df.drop_duplicates().reset_index(drop=True)
    return df


def main(df):
    df = clean_column_names(df)
    df = clean_gender(df)
    df = clean_state(df)
    df = clean_education(df)
    df = clean_customer_lifetime_value(df)
    df = clean_vehicle_class(df)
    df = clean_open_complaints(df)
    df = fill_null_values(df)
    df = convert_numeric_to_int(df)
    df = remove_duplicates(df)
    return df
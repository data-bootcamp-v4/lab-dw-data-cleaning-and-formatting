
import pandas as pd


def clean_column_names(df):
    """
    Standardize column names.

    Converts column names to lowercase.
    Removes extra spaces.
    Replaces spaces with underscores.
    Renames st to state.
    """
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    df = df.rename(columns={
        "st": "state",
        "custateomer_lifetime_value": "customer_lifetime_value"
    })

    return df


def clean_gender(df):
    """
    Standardize gender values to M and F.
    """
    df = df.copy()

    df["gender"] = (
        df["gender"]
        .astype("string")
        .str.strip()
        .str.lower()
        .replace({
            "male": "M",
            "m": "M",
            "female": "F",
            "f": "F",
            "femal": "F"
        })
    )

    return df


def clean_state(df):
    """
    Replace state abbreviations with complete state names.
    """
    df = df.copy()

    state_mapping = {
        "AZ": "Arizona",
        "Cali": "California",
        "WA": "Washington"
    }

    df["state"] = df["state"].replace(state_mapping)

    return df


def clean_education(df):
    """
    Standardize education values.
    """
    df = df.copy()

    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })

    return df


def clean_customer_lifetime_value(df):
    """
    Remove the percent sign and convert customer lifetime value
    to a numeric data type.
    """
    df = df.copy()

    df["customer_lifetime_value"] = (
        df["customer_lifetime_value"]
        .astype("string")
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    df["customer_lifetime_value"] = pd.to_numeric(
        df["customer_lifetime_value"],
        errors="coerce"
    )

    return df


def clean_vehicle_class(df):
    """
    Combine selected vehicle classes into Luxury.
    """
    df = df.copy()

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })

    return df


def clean_open_complaints(df):
    """
    Extract the middle number from values such as 1/5/00.

    Example:
    1/5/00 becomes 5.
    """
    df = df.copy()

    complaints = df["number_of_open_complaints"].astype("string")

    df["number_of_open_complaints"] = pd.to_numeric(
        complaints.str.split("/").str[1],
        errors="coerce"
    )

    return df


def handle_null_values(df):
    """
    Fill numeric null values with the median.

    Fill categorical null values with the mode.
    """
    df = df.copy()

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    categorical_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in categorical_columns:
        mode_values = df[column].mode(dropna=True)

        if not mode_values.empty:
            df[column] = df[column].fillna(mode_values.iloc[0])

    return df


def convert_numeric_to_integer(df):
    """
    Convert all numeric columns to integer data type.

    This function should be used after handling null values.
    """
    df = df.copy()

    numeric_columns = df.select_dtypes(include="number").columns

    df[numeric_columns] = df[numeric_columns].astype(int)

    return df


def remove_duplicates(df):
    """
    Remove duplicated rows while keeping the first occurrence.

    Reset the index after removing duplicates.
    """
    df = df.copy()

    df = df.drop_duplicates(keep="first")
    df = df.reset_index(drop=True)

    return df


def clean_insurance_data(df):
    """
    Main function that performs all data cleaning steps.
    """
    df = clean_column_names(df)
    df = clean_gender(df)
    df = clean_state(df)
    df = clean_education(df)
    df = clean_customer_lifetime_value(df)
    df = clean_vehicle_class(df)
    df = clean_open_complaints(df)
    df = handle_null_values(df)
    df = convert_numeric_to_integer(df)
    df = remove_duplicates(df)

    return df

"""Reusable cleaning functions for the Data Cleaning and Formatting lab.

The CLV scale follows this lab: remove the percent symbol without rescaling.
All numeric variables are rounded and converted to integers as instructed.
"""

import pandas as pd


DEFAULT_SOURCE = (
    "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
)


def clean_column_names(data):
    """Standardize column names and replace ST with state."""
    data = data.copy()
    data.columns = data.columns.str.strip().str.lower().str.replace(
        " ", "_", regex=False
    )
    return data.rename(columns={"st": "state"})


def clean_invalid_values(data):
    """Standardize categorical labels and remove the CLV percent symbol."""
    data = data.copy()
    replacements = {
        "gender": {"Femal": "F", "female": "F", "Male": "M"},
        "state": {"AZ": "Arizona", "Cali": "California", "WA": "Washington"},
        "education": {"Bachelors": "Bachelor"},
        "vehicle_class": {
            "Sports Car": "Luxury",
            "Luxury SUV": "Luxury",
            "Luxury Car": "Luxury",
        },
    }
    for column, mapping in replacements.items():
        data[column] = data[column].replace(mapping)
    data["customer_lifetime_value"] = (
        data["customer_lifetime_value"].str.replace("%", "", regex=False)
    )
    return data


def format_data_types(data):
    """Convert CLV and complaint counts to numeric values, preserving nulls."""
    data = data.copy()
    data["customer_lifetime_value"] = data["customer_lifetime_value"].astype(float)
    data["number_of_open_complaints"] = (
        data["number_of_open_complaints"].str.split("/").str[1].astype(float)
    )
    return data


def handle_missing_values(data):
    """Remove empty rows and fill missing gender and CLV values."""
    data = data.dropna(how="all").copy()
    data["gender"] = data["gender"].fillna("Unknown")
    clv_median = data["customer_lifetime_value"].median()
    data["customer_lifetime_value"] = (
        data["customer_lifetime_value"].fillna(clv_median)
    )
    return data


def convert_numeric_to_integers(data):
    """Round numeric values before converting them to integer types."""
    data = data.copy()
    numeric_columns = data.select_dtypes(include="number").columns
    data[numeric_columns] = data[numeric_columns].round().astype("int64")
    return data


def remove_duplicates(data):
    """Keep the first occurrence of each identical row and reset the index."""
    return data.drop_duplicates(keep="first").reset_index(drop=True)


def main(source=DEFAULT_SOURCE, output_file=None):
    """Load a raw CSV, run the cleaning pipeline, and optionally save it."""
    data = pd.read_csv(source)
    data = clean_column_names(data)
    data = clean_invalid_values(data)
    data = format_data_types(data)
    data = handle_missing_values(data)
    data = convert_numeric_to_integers(data)
    data = remove_duplicates(data)
    if output_file is not None:
        data.to_csv(output_file, index=False)
    return data


if __name__ == "__main__":
    cleaned_data = main(output_file="customer_data_cleaned.csv")
    print(f"Cleaned dataset shape: {cleaned_data.shape}")

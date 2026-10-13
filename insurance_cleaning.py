
import pandas as pd


def load_data(url):
    """Load the insurance dataset."""
    return pd.read_csv(url)


def clean_column_names(df):
    """Standardize column names."""
    df.columns = (
        df.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df.rename(columns={"st": "state"})


def clean_invalid_values(df):
    """Standardize inconsistent categorical values."""
    df = df.copy()

    df["gender"] = (
        df["gender"].astype("string")
        .str.strip()
        .str.lower()
        .replace({
            "f": "F", "female": "F", "femal": "F",
            "m": "M", "male": "M"
        })
    )

    df["state"] = df["state"].replace({
        "AZ": "Arizona",
        "Cali": "California",
        "CA": "California",
        "WA": "Washington",
        "OR": "Oregon",
        "Nev": "Nevada"
    })

    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })

    df["customer_lifetime_value"] = (
        df["customer_lifetime_value"]
        .astype("string")
        .str.replace("%", "", regex=False)
    )

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })

    return df


def format_data_types(df):
    """Convert columns to their appropriate numeric types."""
    df = df.copy()

    df["customer_lifetime_value"] = pd.to_numeric(
        df["customer_lifetime_value"], errors="coerce"
    )

    df["number_of_open_complaints"] = pd.to_numeric(
        df["number_of_open_complaints"]
        .astype("string")
        .str.split("/")
        .str[1],
        errors="coerce"
    )

    return df


def handle_missing_values(df):
    """Remove empty rows and impute missing values."""
    df = df.dropna(how="all").copy()

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    categorical_columns = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    for column in numeric_columns:
        median = df[column].median()
        df[column] = df[column].fillna(median)

    for column in categorical_columns:
        modes = df[column].mode(dropna=True)
        if not modes.empty:
            df[column] = df[column].fillna(modes.iloc[0])

    for column in numeric_columns:
        df[column] = df[column].round().astype("int64")

    return df


def remove_duplicates(df):
    """Remove duplicate rows and reset the index."""
    return df.drop_duplicates().reset_index(drop=True)


def main(url):
    """Run the complete data-cleaning workflow."""
    df = load_data(url)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    df.to_csv("insurance_data_cleaned.csv", index=False)

    return df

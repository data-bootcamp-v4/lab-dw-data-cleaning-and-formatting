import pandas as pd


def clean_column_names(df):
    df = df.rename(columns={"ST": "state"})
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def clean_values(df):
    df["gender"] = df["gender"].replace({
        "Female": "F",
        "Femal": "F",
        "female": "F",
        "Male": "M",
        "male": "M"
    })

    df["state"] = df["state"].replace({
        "AZ": "Arizona",
        "Cali": "California",
        "WA": "Washington"
    })

    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })

    df["customer_lifetime_value"] = (
        df["customer_lifetime_value"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })

    return df


def format_data_types(df):
    df["customer_lifetime_value"] = pd.to_numeric(
        df["customer_lifetime_value"]
    )

    df["number_of_open_complaints"] = (
        df["number_of_open_complaints"].apply(
            lambda x: x.split("/")[1]
            if isinstance(x, str) else x
        )
    )

    df["number_of_open_complaints"] = pd.to_numeric(
        df["number_of_open_complaints"]
    )

    return df


def handle_null_values(df):
    print("Null values before cleaning:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    for column in df.select_dtypes(include="number").columns:
        df[column] = df[column].fillna(df[column].median())

    for column in df.select_dtypes(
        include=["object", "string"]
    ).columns:
        if df[column].isnull().sum() > 0:
            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

    for column in df.select_dtypes(include="number").columns:
        df[column] = df[column].round().astype(int)

    print("Null values after cleaning:")
    print(df.isnull().sum())

    return df


def remove_duplicates(df):
    print("Duplicates before:", df.duplicated().sum())

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    print("Duplicates after:", df.duplicated().sum())

    return df


def save_dataset(df):
    df.to_csv("dataset_clean.csv", index=False)
    print("Cleaned dataset saved successfully!")
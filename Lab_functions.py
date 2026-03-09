import pandas as pd


# Exercise 1 — Clean column names
def clean_column_names(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df = df.rename(columns={"st": "state"})
    return df


def clean_invalid_values(df):

    df["gender"] = df["gender"].replace({
        "female": "F",
        "Femal": "F",
        "f": "F",
        "F": "F",
        "Male": "M",
        "m": "M",
        "M": "M"
    })

    state_mapping = {
        "AZ": "Arizona",
        "Cali": "California",
        "CA": "California",
        "WA": "Washington"
    }

    df["state"] = df["state"].replace(state_mapping)

    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })

    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })

    return df


def format_data_types(df):

   
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(float)


    df["number_of_open_complaints"] = (
        df["number_of_open_complaints"].str.split("/").str[1].astype(float)
    )

    return df



def handle_null_values(df):

    drop_cols = [
        "customer",
        "state",
        "education",
        "income",
        "number_of_open_complaints",
        "policy_type",
        "vehicle_class",
        "total_claim_amount"
    ]

    df = df.dropna(subset=drop_cols)


    df["gender"] = df["gender"].fillna(method="ffill")

    return df



def remove_duplicates(df):

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df



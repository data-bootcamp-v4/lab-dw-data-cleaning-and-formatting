# En este script creamos las funciones para cleaning y formatting

import pandas as pd

def changing_col_names(df):
    """
    It takes df and it formats the names of the columns
    """
    mapping = {col: str(col).strip().lower().replace(" ", "_") for col in df}
    df.rename(columns=mapping, inplace=True)
    df.rename(columns={"st": "state"}, inplace=True)
    return df


def clean_gender(df):
    """
    It takes gender variables and it returns F/M/NaN
    """
    gender_mapping = {'Male': 'M', 'female': 'F', 'Femal': 'F', 'F': 'F', 'M': 'M'}
    df['gender'] = df['gender'].map(gender_mapping)
    return df

def clean_state(df):
    """
    It expands abreviations of states.
    """
    state_mapping = {
        'Cali': 'California', 
        'WA': 'Washington', 
        'AZ': 'Arizona',
        'California': 'California',
        'Arizona': 'Arizona',
        'Oregon': 'Oregon',
        'Washington': 'Washington',
        'Nevada': 'Nevada'
        }
    df['state'] = df['state'].map(state_mapping)
    return df

def clean_education(df):
    """
    It standarize values of education.
    """
    education_mapping = {
        'Bachelor': 'Bachelor',
        'College': 'College',
        'High School or Below': 'High School or Below',
        'Master': 'Master',
        'Doctor': 'Doctor',
        'Bachelors': 'Bachelor'
    }
    df["education"] = df["education"].map(education_mapping)
    return df

def clean_clv(df):
    """
    It cleans values of clv.
    """
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"], errors="coerce")
    return df

def clean_vehicle_class(df):
    """
    It cleans values of vehicle class.
    """
    vehicle_mapping = {
        'Four-Door Car': 'Four-Door Car',
        'Two-Door Car': 'Two-Door Car',
        'SUV': 'SUV',
        'Sports Car': 'Luxury',
        'Luxury SUV': 'Luxury',
        'Luxury Car': 'Luxury'
    }
    df["vehicle_class"] = df["vehicle_class"].map(vehicle_mapping)
    return df

def clean_number_of_open_complaints(df):
    """
    It cleans values of number_of_open_complaints.
    """
    open_complaints_mapping = {
        "1/0/00": 0,
        "1/1/00": 1,
        "1/2/00": 2,
        "1/3/00": 3,
        "1/4/00": 4,
        "1/5/00": 5
    }
    df["number_of_open_complaints"] = df["number_of_open_complaints"].map(open_complaints_mapping)
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce").astype("Int64")
    return df

def clean_all(df):
    """
    It execute all functions of cleaning.
    """
    df = changing_col_names(df)
    df = clean_gender(df)
    df = clean_state(df)
    df = clean_education(df)
    df = clean_clv(df)
    df = clean_vehicle_class(df)
    df = clean_number_of_open_complaints(df)
    return df

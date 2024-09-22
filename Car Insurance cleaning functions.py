import numpy as np
import pandas as pd


def strip_replace (df):
    car_insurance_df.columns = car_insurance_df.columns.str.lower().str.replace(" ","_")

"""
def strip_values(df):
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x)
    return df
"""

"""
def strip_replace_whitespace(df):
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: x.strip() if isinstance(x, str) else x)
        df[col] = df[col].apply(
            lambda x: x.replace(" ","_") if isinstance(x, str) else x)
    return df
"""

def rename (row, *args):


def merge_values(row, arg1, *args):
    if row in args:
        return arg1
    else:
        return row
"""
shark_df["Type"] = shark_df["Type"].apply(lambda x: merge_values(x, "Invalid", "Questionable", "Unconfirmed", "?",'Unverified','Under investigation'))
"""

def formatting_data_types ():
"""
round?, split?, get?
"""

def get_complaints(comp):
    if isinstance(comp, str):
        comp_list = comp.split("/")
        return int(comp_list[1])
    else:
        return pd.NA

def drop_na ():
    """
    """

def fill_na():
    """
    mean, mode, ratio
    """


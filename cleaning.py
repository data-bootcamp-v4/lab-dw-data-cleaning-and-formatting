import pandas as pd

def snake(data):
    data.columns = [column.lower().replace(" ", "_") for column in data.columns]

def replace_col(data, col_, old, new):
    data[col_] = data[col_].replace(old, new)

def filling_nan(data, col_, method):
    if method == "mode":
        data[col_] = data[col_].fillna(data[col_].mode()[0])

def drop(data):
    data.drop_duplicates(keep="first", inplace=True)

def in_col_replace(data, col_, old, new, type_):
    data[col_] = data[col_].str.replace(old, new, regex=True).astype(type_)
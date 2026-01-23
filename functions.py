import pandas as pd
import numpy as np


def cleaning_column_names(dframe):
    dframe = dframe.dropna(thresh=1)
    dframe.columns = [column.lower() for column in dframe.columns]
    dframe = dframe.rename(columns = {"st":"state"})
    dframe.columns = [column.replace(" ","_") for column in dframe.columns]
    return dframe

def cleaning_invalid(dframe):
    dframe["gender"]=["F" if isinstance(row,str) and row.lower().startswith("f") else "M" if isinstance(row,str) and row.lower().startswith("m") else row for row in dframe["gender"]]
    dframe["state"]=["Arizona" if row == "AZ" else "Washington" if row == "WA" else "California" if row == "Cali" else row for row in dframe["state"]]
    dframe["education"]=["Bachelor" if row == "Bachelors" else row for row in dframe["education"]]
    dframe["customer_lifetime_value"]=[row.replace("%","") if isinstance(row, str) else row for row in dframe["customer_lifetime_value"]]
    dframe["vehicle_class"]=[row.replace("Luxury Car","Luxury") if row == "Luxury Car" else row.replace("Luxury SUV","Luxury") if row == "Luxury SUV" else row.replace("Sports Car","Luxury") if row == "Sports Car" else row for row in dframe["vehicle_class"]]
    return dframe
def formatting(dframe):
    dframe["customer_lifetime_value"] = pd.to_numeric(dframe["customer_lifetime_value"])
    dframe["number_of_open_complaints"] = dframe["number_of_open_complaints"].astype(str)
    dframe["number_of_open_complaints"]=dframe["number_of_open_complaints"].str.split("/").str[1]
    dframe["number_of_open_complaints"]=pd.to_numeric(dframe["number_of_open_complaints"], errors='coerce')
    dframe["number_of_open_complaints"].apply(type).value_counts()
    return dframe

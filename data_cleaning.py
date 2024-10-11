
import pandas as pd


url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
df = pd.read_csv(url)
 
def show_columns(df):
    print(f"Data Frame columns are: {df.columns}")
    return
   

def format_column_names(df):
    df.columns = df.columns.str.lower() # To make all column names in lower case
    df.columns = df.columns.str.replace(" ", "_") #To replace spaces in column names with "_"
    print(f"Date Frame columns names modified are: {df.columns}")
    return df


df = df.rename(columns={'st': 'state'})


def clean_invalid_data(df):
    df['gender'] = df.gender.str.replace("female", "F").replace("Femal", "F").replace("Male", "M")
    df['state'] = df.state.str.replace("AZ", "Arizona").replace("WA", "Washington").replace("").replace("California", "Cali")
    df['state'] = df.state.str.replace("Cali", "California")
    df['education'] = df.education.str.replace("Bachelors", "Bachelor")
    df["customer_lifetime_value"] = df.customer_lifetime_value.str.replace("%", "")
    df["vehicle_class"] = df.vehicle_class.str.replace("Sports Car", "Luxury").replace("Luxury SUV", "Luxury").replace("Luxury Car", "Luxury")
    return df


def format_data_types(df):
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"]) 
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.replace('/00','') # Noticing there is a value "1/1/00", I apply first replacing the final part "/00" 
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.replace('1/','')
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"])
    return df


def deal_with_null_values(df):
    df.dropna(how = "all")
    df = df.dropna(how = "all")
    df.dropna(subset=["customer_lifetime_value"], inplace = True)
    df["gender"] = df["gender"].fillna(method = 'ffill')
    return df


def reset_indexes(df):
    df.reset_index(drop=True)
    return df

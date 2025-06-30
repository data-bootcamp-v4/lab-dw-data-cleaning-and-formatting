import pandas as pd
def replace_values(data_df):
    data_df["gender"] = data_df["gender"].replace("Femal", "F").replace("female", "F").replace("Male", "M")
    # data_df["gender"] .nunique()
    data_df["state"] = data_df["state"].replace("AZ", "Arizona").replace("Cali", "California").replace("WA", "Washington")
    # data_df["state"].unique()
    data_df["education"] = data_df["education"].replace("Bachelors", "Bachelor")
    #print(data_df["education"].unique())
    data_df["customer_lifetime_value"] = data_df["customer_lifetime_value"].str.replace("%", "")
    #print(data_df["customer_lifetime_value"].unique())
    data_df["vehicle_class"] = data_df["vehicle_class"].replace("Sports Car", "Luxury").replace("Luxury SUV", "Luxury").replace("Luxury Car", "Luxury")

    return data_df


def rename_columns(data_df):
    data_df.columns = [cln_name.lower() for cln_name in data_df.columns] # Column Names should be in Lower Case
    data_df.columns = [cln_name.replace(" ", "_") for cln_name in data_df.columns]
    data_df.rename(columns={"st": "state"}, inplace=True)
    return data_df

def change_data_types(data_df):
    data_df["customer_lifetime_value"] = data_df["customer_lifetime_value"].astype(float)   
    data_df["number_of_open_complaints"] = data_df["number_of_open_complaints"].str.split("/").str[1]
    data_df["number_of_open_complaints"] = data_df["number_of_open_complaints"].astype(float)
    return data_df

def fill_na_values(data_df):
    df_remove_all_null = data_df[~data_df.isnull().all(axis=1)]
    # df_remove_all_null["gender"] = df_remove_all_null["gender"].fillna("?")
    df_remove_all_null["number_of_open_complaints"] = df_remove_all_null["number_of_open_complaints"].fillna(0)
    df_remove_all_null["total_claim_amount"] = df_remove_all_null["total_claim_amount"].fillna(0)

    mean_value = df_remove_all_null["customer_lifetime_value"].mean()

    df_remove_all_null["customer_lifetime_value"] = df_remove_all_null["customer_lifetime_value"].fillna(mean_value)
    df_remove_all_null["income"] = df_remove_all_null["income"].fillna(df_remove_all_null["income"].mean())
    return df_remove_all_null

def handle_duplicates(data_df):
    df_no_duplicates = data_df.drop_duplicates(keep='first').reset_index(drop="index")
    return df_no_duplicates
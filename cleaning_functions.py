import pandas as pd

def clean_column_names(my_df):
    '''
    cleans the column names
    '''
    my_df.columns = [col.replace(" ", "_").lower() for col in my_df.columns]

    my_df.rename({"st": "state"}, axis = 1, inplace=True)
    
    return my_df
    
def clean_na(my_df):
    '''
    Cleans invalid values
    '''
    
    my_df["gender"] = my_df["gender"].replace({"Male": "M", "Female": "F", "female": "F", "Femal": "F"})
    my_df["state"] = my_df["state"].replace({"AZ": "Arizona", "Cali": "California", "WA": "Washington"})
    my_df["education"] = my_df["education"].replace({"Bachelors": "Bachelor"})
    my_df["customer_lifetime_value"] = my_df["customer_lifetime_value"].str.rstrip("%")
    my_df["vehicle_class"] = my_df["vehicle_class"].replace({"Sports Car": "Luxury", "Luxury SUV": "Luxury", 
                                                         "Luxury Car": "Luxury"})
    return my_df
    
def formating_dtypes(my_df):
    '''
    formats current dtypes to correct dtypes
    '''
    my_df["customer_lifetime_value"] = pd.to_numeric(my_df["customer_lifetime_value"])
    my_df["number_of_open_complaints"] = my_df["number_of_open_complaints"].str.split("/").str.get(1)
    my_df["number_of_open_complaints"] = pd.to_numeric(my_df["number_of_open_complaints"])
    
    return my_df

def dealing_na(my_df):
    
    '''
    Deals with nulls appropiately.
    '''
    
    my_df["customer"] = my_df["customer"].ffill()
    
    gender_mode = my_df["gender"].mode()[0]
    my_df["gender"].fillna(gender_mode, inplace=True)
    
    education_mode = my_df["education"].mode()[0]
    my_df["education"].fillna(education_mode, inplace=True)
    
    customer_mean = my_df["customer_lifetime_value"].mean()
    my_df["customer_lifetime_value"].fillna(customer_mean, inplace=True)
    
    income_mean = my_df["income"].mean()
    my_df["income"].fillna(income_mean, inplace=True)
    
    premium_mean = my_df["monthly_premium_auto"].mean()
    my_df["monthly_premium_auto"].fillna(premium_mean, inplace=True)
    
    complaints_mean = my_df["number_of_open_complaints"].mean()
    my_df["number_of_open_complaints"].fillna(complaints_mean, inplace=True)
    
    policy_mode = my_df["policy_type"].mode()[0]
    my_df["policy_type"].fillna(policy_mode, inplace=True)

    vehicle_mode = my_df["vehicle_class"].mode()[0]
    my_df["vehicle_class"].fillna(policy_mode, inplace=True)
    
    claim_mean = my_df["total_claim_amount"].mean()
    my_df["total_claim_amount"].fillna(claim_mean, inplace=True)
    
    my_df["customer_lifetime_value"] = my_df["customer_lifetime_value"].astype(int)
    
    my_df["income"] = my_df["income"].astype(int)
    
    my_df["monthly_premium_auto"] = my_df["monthly_premium_auto"].astype(int)
    
    my_df["number_of_open_complaints"] = my_df["number_of_open_complaints"].astype(int)
    
    my_df["total_claim_amount"] = my_df["total_claim_amount"].astype(int)
    
    return my_df

def dealing_duplicates(my_df):
    '''
    Deals with duplicates based on the customer column.
    '''
    my_df.drop_duplicates(subset = ["customer"], inplace=True)
    my_df.reset_index(drop=True)
    
    return my_df
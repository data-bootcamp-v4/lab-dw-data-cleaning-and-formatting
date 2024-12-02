import pandas as pd
def clean_col_name (df):
    df.columns = ['customer', 'state', 'gender', 'education', 'customer_lifetime_value',
       'income', 'monthly_premium_auto', 'number_of_open_complaints',
       'policy_type', 'vehicle_class', 'total_claim_amount']
    return df


def format_row_data(df):
    df.gender = df.gender.apply(lambda x: "M"  if x =="Male" else 
                                ("F" if x == 'Femal' else ("F" if x == 'female' else x ) ) )
    df.state = df.state.apply(lambda x: "California" if x == "Cali" else ("Arizona" if x == 'AZ' else("Washington" if x == 'WA' else x )) )
    df.education = df.education.apply(lambda x: "Bachelor" if x == "Bachelors" else x)
    df.customer_lifetime_value = df.customer_lifetime_value.apply(lambda x : x[:-1] if pd.notnull(x) else x)
    df.vehicle_class = df.vehicle_class.apply(lambda x: "Luxury"  if (x =="Sports Car" or x == "Luxury SUV" or x=="Luxury Car") else x )
    
    return df

def format_col_data_type (df):
    df.customer_lifetime_value = df.customer_lifetime_value.astype("float64")
    df.monthly_premium_auto = df.monthly_premium_auto.astype("float64")
    df.total_claim_amount = df.total_claim_amount.astype("float64")
    df.number_of_open_complaints = df.number_of_open_complaints.apply(lambda x : (str(x).split("/")[1]) if pd.notnull(x)  else  x )
    df.number_of_open_complaints = df.number_of_open_complaints.astype("float64")
    return df

def clean_nun_values (df):
    df = df.dropna(how="all")
    df.customer_lifetime_value = df.customer_lifetime_value.fillna(0)
    df.gender = df.gender.fillna(df.gender.describe().top)
    return df


def complete_cleaning (df):
    df = clean_col_name(df)
    df = format_row_data(df)
    df = format_col_data_type(df)
    df = clean_nun_values(df)
    df.reset_index(drop=True, inplace=True)
    return df
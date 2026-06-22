import pandas as pd

def clean_column_names(df):
    df1 = df.copy()

    df1.rename(columns = {col: col.strip().replace(
        "ST", "state").replace(" ", "_").lower() for col in df1.columns}, inplace = True)
    return df1

####################################################################################################
def clean_gender_col(df):
    df1 = df.copy()
    df1.gender = df1["gender"].apply(lambda x : "F" if str(x).lower().startswith("f") else ("M" if str(x).lower().startswith("m") else "NaN"))
                                  
    return df1
####################################################################################################
def clean_state_col(df):
    df1 = df.copy()
    df1['state'] = df1.state.replace({'AZ': 'Arizona', 'WA': 'Washington', 'Cali': 'California'})
    return df1

####################################################################################################
def clean_education_col(df):
    df1 = df.copy()
    df1['education'] = df1.education.replace({'Bachelors': 'Bachelor'})
    return df1
####################################################################################################
def clean_liftime_col(df):
    df1 = df.copy()
    df1["customer_lifetime_value"]= df1["customer_lifetime_value"].apply(lambda x: str(x).strip("%"))
    return df1
####################################################################################################
def clean_vehicle_class_col(df):
    df1 = df.copy()
    df1["vehicle_class"]= df1["vehicle_class"].apply(lambda x: "Luxury" if x in ["Sports Car", "Luxury SUV","Luxury Car"] else x)
    return df1
####################################################################################################
def to_float_lifetime(df):
    """
    input dfoutput from:  df1 = clean_liftime_col(df)
    
    """
    df1 = df.copy()
    df1["customer_lifetime_value"] = df1["customer_lifetime_value"].apply(float)
    return df1

####################################################################################################
def to_num_nbr_of_complaints(df):
    df1 = df.copy()
    df1["number_of_open_complaints"] = df1["number_of_open_complaints"].apply(lambda x : x.split("/")[1] if type(x) != float else x)
    df1["number_of_open_complaints"] = pd.to_numeric(df1["number_of_open_complaints"], errors="coerce").astype("Int64")
    return df1
####################################################################################################
def main(df):
    df1 = df.copy()
    df1 = clean_column_names(df1)
    df1 = clean_gender_col(df1)
    df1 = clean_state_col(df1)
    df1 = clean_education_col(df1)
    df1 = clean_liftime_col(df1)
    df1 = clean_vehicle_class_col(df1)
    df1 = to_float_lifetime(df1)
    df1 = to_num_nbr_of_complaints(df1)
    
    return df1

    
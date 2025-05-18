def column_form(df):
    df.columns = [col.replace(" ", "_").lower() for col in df.columns]
    return df

def st_column(df):
    try:
        df.rename(columns = {"st": "state"}, inplace=True)
    except:
        return df

def clean_gender(df):
    df["gender"] = df["gender"].replace({"Femal": "F", "Male": "M", "female": "F"})
    return df

def clean_state(df):
    df["state"] = df["state"].replace({"AZ": "Arizona", "Cali": "California", "WA": "Washington"})
    return df

def clean_educ(df):
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})
    return df

def clean_clv(df):
    try:
        df["customer_lifetime_value"] = [float(str(value).strip("%")) for value in df["customer_lifetime_value"]]
    except:
        return df

def clean_vehicle(df):
    try:
        df["vehicle_class"] = df["vehicle_class"].replace({"Sports Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"})
    except:
        return df


def clean_noc_main(df):
    try:
        clean_noc = [str(number).strip("1") for number in df["number_of_open_complaints"]]
        clean_noc2 = [number.strip("00") for number in clean_noc]
        clean_noc3 = [number.strip("/") for number in clean_noc2]
        df["number_of_open_complaints"] = clean_noc3
    except:
        return df

def clean_nan_main(df):
    try:
        df.dropna(subset="customer", inplace = True)
        df.dropna(subset="customer_lifetime_value", inplace = True)
        mode_gender = df["gender"].mode()
        df["gender"] = df["gender"].fillna(mode_gender)
        df["number_of_open_complaints"] = [int(number) for number in df["number_of_open_complaints"]]
    except:
        return df

def clean_data_insurance(df):
    column_form(df)
    st_column(df)
    clean_gender(df)
    clean_state(df)
    clean_educ(df)
    clean_clv(df)
    clean_vehicle(df)
    clean_noc_main(df)
    clean_nan_main(df)
    return df
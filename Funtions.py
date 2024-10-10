def clean_columns_names(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df.rename(columns= {'st': 'state'}, inplace=True)

def fix_invalid_values(df):
    df['gender'] = df['gender'].replace({'Male': 'M','Femal': 'F', 'female': 'F'})
    df['state'] = df['state'].replace({'AZ': 'Arizona','Cali': 'California', 'WA': 'Washington'})
    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace("%", "").astype(float)
    df['vehicle_class'] = df['vehicle_class'].replace({'Sports Car':'Luxury', "Luxury Car":'Luxury', "Luxury SUV":'Luxury'})

def format_data_types(df):
    df["customer_lifetime_value"]= df["customer_lifetime_value"].astype(float)
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str[2]
    df["number_of_open_complaints"]= df["number_of_open_complaints"].astype(float)

def drop_null(df):
    df.dropna(inplace=True)

def drop_duplicates(df):
    df.drop_duplicates(inplace=True)
    df.reset_index(inplace=True)

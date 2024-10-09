# functions for cleaning


import pandas as pd

def cargar_fichero(url): 
    '''
    Lectura del fichero
    '''
    
    #url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
    df = pd.read_csv(url)
    return df

# change cols names

def change_cols_names(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.rename(columns = {'st': 'state'}, inplace=True)
    
    return df

# cleaning invalid Values

def gender(gender): 
    mujer = ['F', 'Femal', 'female']
    hombre = ['M', 'Male']
    if (gender in mujer): 
        return 'F'
    elif (gender in hombre): 
        return 'M'
    else: 
        return gender



def cleaning_invalid_Value(df): 
    
    df["gender"] = df["gender"].apply(gender)
    df['state'] = df['state'].replace('AZ', 'Arizona')
    df['state'] = df['state'].replace('WA', 'Washington')
    df['state'] = df['state'].replace('Cali', 'California')
    df['education'] = df['education'].replace("Bachelors", "Bachelor")
    df["vehicle_class"] = df["vehicle_class"].apply(lambda x: "Luxury" if ( x in ["Sports Car", "Luxury SUV", "Luxury Car"]) else x)
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", " ")
    
    return df

# type

def correct_format(com): 
    
    try: 
        middle_value = com.split('/')[1]
        return int(middle_value)
    except: 
        return com

def change_type(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", " ")
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(float)
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(correct_format)
    
    return df

#null values

def drop_null_values(df):
    
    df.dropna(how='all', inplace=True)
    
    return df

#remplace null values

def replace_null(df):
    
    df['customer_lifetime_value'] = df['customer_lifetime_value'].fillna(df['customer_lifetime_value'].mean())
    df['gender'].fillna(method='bfill', inplace=True)
    
    return df

def duplicates(df):
    
    num_dup = df.duplicated().sum()
    print(f"Hay {num_dup} valores duplicados")
    
    num_esp = df.duplicated(subset=["state", "income", "customer_lifetime_value"]).sum()
    print(f"De las columnas `state`, `income` y `customer_lifetime_value` hay {num_esp} valores duplicados")
    
    df.drop_duplicates(subset=["state", "income", "customer_lifetime_value"], keep="last", inplace=True)
    
    return df
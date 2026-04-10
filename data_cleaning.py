def cleaning_columns(insurance_data):
    insurance_data.columns=insurance_data.columns.str.lower()
    insurance_data.columns=insurance_data.columns.str.replace(" ","_")
    insurance_data=insurance_data.rename(columns={"st": "state"})
    return insurance_data

def cleaning_invalid_values(insurance_data):
    print("Gender column cleaning:")
    print(insurance_data['gender'].unique())
    insurance_data['gender'] = insurance_data['gender'].str.replace('Femal','F')
    insurance_data['gender'] = insurance_data['gender'].str.replace('female','F')
    insurance_data['gender'] = insurance_data['gender'].str.replace('Male','M')
    print("Gender column after cleaning:")
    print(insurance_data['gender'].unique())

    print("State column cleaning:")
    print(insurance_data['state'].unique())
    insurance_data['state'] = insurance_data['state'].replace({
        'WA': 'Washington',
        'AZ': 'Arizona',
        'Cali': 'California'
    })
    print("State column after cleaning:")
    print(insurance_data['state'].unique())

    print("Education column cleaning:")
    print(insurance_data['education'].unique())
    insurance_data['education'] = insurance_data['education'].replace({
    'Bachelors':'Bachelor'
    })
    print("Education column after cleaning:")
    print(insurance_data['education'].unique())

    print("Vehicle class column cleaning:")
    print(insurance_data['vehicle_class'].unique())
    insurance_data['vehicle_class'] = insurance_data['vehicle_class'].replace({
    'Sports Car':'Luxury',
    'Luxury SUV':'Luxury',
    'Luxury Car':'Luxury'
    })
    print("Vehicle class column after cleaning:")
    print(insurance_data['vehicle_class'].unique())
    
    return insurance_data

def formatting_dtypes(insurance_data):
    print(insurance_data.dtypes)
    print(insurance_data["customer_lifetime_value"].value_counts())
    insurance_data["customer_lifetime_value"]= insurance_data["customer_lifetime_value"].str.replace("%","")
    insurance_data["customer_lifetime_value"] = insurance_data["customer_lifetime_value"].astype(float)


    insurance_data["number_of_open_complaints"]=insurance_data["number_of_open_complaints"].str.split('/').str[1].astype('Int64')
    
    return insurance_data

def null_value_cleaning(insurance_data):
    print(insurance_data.isnull().sum())
    print((insurance_data.isnull().sum()/len(insurance_data))*100)

    insurance_data["gender"]=insurance_data["gender"].fillna(insurance_data["gender"].mode()[0])
    insurance_data["customer_lifetime_value"]=insurance_data["customer_lifetime_value"].fillna(insurance_data["customer_lifetime_value"].mean())
    print(round((insurance_data.isnull().sum()/len(insurance_data))*100))

    return insurance_data


def drop_duplicates(insurance_data):
    insurance_data=insurance_data.drop_duplicates()
    print(insurance_data.duplicated())

    return insurance_data




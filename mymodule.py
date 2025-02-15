def clean_data():
    import pandas as pd
    import numpy as np
    cust_data = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv')
    cust_data.head()
    
    cust_data = cust_data.rename(columns = {'ST':'State'})
    cust_data.columns = cust_data.columns.str.replace(' ','_').str.lower()

    cust_data.gender = cust_data.gender.replace('Femal','F').replace('female','F').replace('Male','M')

    cust_data.state = cust_data.state.replace('AZ','Arizona').replace('Cali','California').replace('WA','Washington')

    cust_data.education = cust_data.education.replace('Bachelors','Bachelor')

    cust_data.customer_lifetime_value = cust_data.customer_lifetime_value.replace('%','',regex=True) #the replace looks for the whole str without regex true"
    cust_data.customer_lifetime_value = cust_data.customer_lifetime_value.astype(float)
    
    cust_data.vehicle_class = cust_data.vehicle_class.replace(['Luxury SUV','Sports Car','Luxury Car'],'Luxury')

    cust_data.customer_lifetime_value = cust_data.customer_lifetime_value.astype(float)

    cust_data.number_of_open_complaints = cust_data.number_of_open_complaints.replace(['1/','/00'],'',regex=True).replace('00','0')
    cust_data.number_of_open_complaints = pd.to_numeric(cust_data.number_of_open_complaints,errors = 'coerce').astype('Int64')

    cust_data = cust_data.dropna(how='all')
    cust_data.isnull().sum()

    cust_data.customer_lifetime_value = cust_data.customer_lifetime_value.fillna(cust_data.customer_lifetime_value.mean())
    cust_data.customer_lifetime_value.isnull().sum()

    cust_data.gender = cust_data.gender.fillna('Unknown')
    
    for column in cust_data.select_dtypes(include = 'float').columns:
        cust_data[column]= cust_data[column].astype(int)

    print(cust_data.dtypes,cust_data.head())
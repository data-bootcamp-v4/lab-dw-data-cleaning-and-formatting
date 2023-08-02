#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cleaning_column_names(insurance_company):
    insurance_company = insurance_company.rename(columns = {'ST':'State', 'GENDER':'Gender'})
    return insurance_company

def standardized_gender(row):
    if type(row['Gender']) != float:
        if row['Gender'] == 'Male':
            return 'M'
        elif row['Gender'] == 'female' or row['Gender'] == 'Femal':
            return 'F'
        else:
            return row['Gender']


def standardized_complaints(row):
    if type(row['Number of Open Complaints']) == str:
        return int(row['Number of Open Complaints'].split('/')[1])
    else:
        return row['Number of Open Complaints']


def standardized_lifetime_value(row):
    if type(row['Customer Lifetime Value']) == str:
        return float(row['Customer Lifetime Value'].strip('%'))/100
    else:
        return row['Customer Lifetime Value']

def replace_null_values(df, column, replacement):
    df[column].fillna(replacement, inplace=True)

def convert_to_integer(x):
    try:
        return int(x)
    except:
        return x


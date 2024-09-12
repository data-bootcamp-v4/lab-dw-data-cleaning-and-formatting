#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np

csv_url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
df = pd.read_csv(csv_url)

df.head()


# In[1]:


def cleaning_column_names(insurance):
    insurance = insurance.rename(columns = {'ST': 'State', 'GENDER': 'Gender'})

    return insurance


# In[4]:


def cleaning_values(insurance):
    insurance.replace(to_replace = ["F", "Femal", "female"],
                          value = "F", inplace=True)

    insurance.replace(to_replace = ["M", "Male"],
                          value = "M", inplace=True)

    insurance.replace(to_replace = ["Cali"],
                          value = "California", inplace=True)
                          
    insurance.replace(to_replace = ["WA"],
                          value = "Washington ", inplace=True)
                          
    insurance.replace(to_replace = ["AZ"],
                          value = "Arizona", inplace=True)
                          
    insurance.replace(to_replace = ["Bachelors"],
                          value = "Bachelor", inplace=True)
    
    return insurance


# In[7]:


def transform_complaints(row):
    complaints = row["Number of Open Complaints"]
    if pd.notnull(complaints) and type(complaints) == str:
        complaints = complaints.replace("/", "")
        return float(complaints[0]) if complaints else None
    else:
        return complaints


# In[8]:


def null_values(insurance):
    null_exists = False
    for column in insurance:
        for value in insurance[column].isnull():
           if(value):
               null_exists = True
    if null_exists == True:
        insurance = insurance.dropna()
    
    return insurance


# In[9]:


def duplicates(insurance):
    duplicates_exists = False
    for column in insurance:
        for value in insurance[column].duplicated():
           if(value):
               duplicates_exists = True
    if duplicates_exists == True:
        insurance = insurance.drop_duplicates()    
    
    return insurance


# In[12]:


def data_cleaning(insurance):  
    insurance = cleaning_column_names(insurance)
    insurance = cleaning_invalid_values(insurance)
    insurance = formatting_data_types(insurance)
    insurance = null_values(insurance)
    insurance = duplicates(insurance)
    
    return insurance

df = data_cleaning(df)


# In[13]:


display(df)


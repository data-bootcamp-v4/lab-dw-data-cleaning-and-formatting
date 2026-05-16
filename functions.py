import pandas as pd
import numpy as np

def clean_cols(df):
    df2=df.copy()
    df2.columns = df2.columns.map(lambda x: x.lower().replace(' ','_'))
    df2.rename(columns={'st': 'state'}, inplace=True)
    return df2

def clean_vals(df):
    df2=df.copy()
    df2.gender = df2.gender.replace({'M':'male','Male':'male','F':'female','Femal':'female'})
    df2.state = df2.state.replace({'AZ':'Arizona','Cali':'California','WA':'Washington'})
    df2.education = df2.education.replace({'Bachelors':'Bachelor'})
    df2.customer_lifetime_value = df2.customer_lifetime_value.apply(lambda x: x.replace('%','') if isinstance(x,str) else x)
    df2.vehicle_class = df2.vehicle_class.replace({'Sports Car':'Luxury','Luxury SUV':'Luxury','Luxury Car':'Luxury'})
    return df2

def convert_numeric(df):
    df2 = df.copy()
    df2.customer_lifetime_value = df2.customer_lifetime_value.replace(['', ' '], np.nan).astype(float)
    df2.loc[:,'number_of_open_complaints'] = df2['number_of_open_complaints'].apply(lambda x: float(x.split("/")[1]) if isinstance(x,str)
                                                                                                else np.nan)
    df2.loc[:, 'number_of_open_complaints'] = df2.loc[:, 'number_of_open_complaints'].astype(float)
    df2.number_of_open_complaints.value_counts()
    return df2

def remove_nans(df):
    df2 = df.copy()
    df2 = df2.dropna(thresh=len(df2.columns)-1)
    df2.gender = df2.gender.fillna('unknown')
    df2.customer_lifetime_value = df2.customer_lifetime_value.fillna(df2.customer_lifetime_value.mode()[0])
    return df2

def remove_dupl(df):
    df2 = df.copy()
    cols = list(df2.columns)
    df2.drop_duplicates(subset=cols[1:], keep='last', inplace=True) 
    df2 = df2.reset_index()
    #df.to_csv('insurance_dataset.csv', index=False) #optional save to csv
    return df2

def clean_all(df):
    df2 = df.copy()
    df2 = clean_cols(df2)
    df2 = clean_vals(df2)
    df2 = convert_numeric(df2)
    df2 = remove_nans(df2)
    df2 = remove_dupl(df2)
    return df2
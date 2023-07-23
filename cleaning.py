def cleaning_dataframes(df):
    import re
    import pandas as pd
    def low_clean_columns(column_name):
        column_name = re.sub(r"[^\w\s\%]", " ", str(column_name).lower())
        return column_name
    def types_setting(df):
        df["customer lifetime value"] = df["customer lifetime value"].str.replace("N/A","0")
        df["customer lifetime value"] = df["customer lifetime value"].str.rstrip("%")#Elitminates all the strings
        df["customer lifetime value"] = df["customer lifetime value"].astype(float)
        return df
    def cleaning_nulls(df):
        df.dropna(axis=0,how="all",inplace=True) #Cleaning Null Values in the Dataframe
        df.fillna(axis=0,value="N/A",inplace=True)
        return df
    def checking_dup(df):
        df["customer"].duplicated().sum()
        return df
    
    df.columns = [low_clean_columns(i) for i in df.columns]
    df=cleaning_nulls(df)
    df=checking_dup(df)
    df=types_setting(df)
    return df

'''def cleaning_dataframes(df):
    def types_setting(df):
        df_1 = df.convert_dtypes()
        df_1["Customer Lifetime Value"] = df_1["Customer Lifetime Value"].str.rstrip('%')#Elitminates all the strings
        df_1["Customer Lifetime Value"] = df_1["Customer Lifetime Value"].astype(float)
        return df_1
    def cleaning_nulls(df_1):
        df_1.dropna(axis=0,how="all",inplace=True) #Cleaning Null Values in the Dataframe
        df_1.fillna(axis=0,value="N/A",inplace=True)
        return df_1
    def checking_dup(df_1):
        df_1["Customer"].duplicated().sum()
    return df'''
import pandas as pd
def lowercase_columns(df):
    df.columns = df.columns.str.lower()
    return df


def replace(df):
    df.columns = df.columns.str.replace(" ", "_")
    return(df)
                                        
def rename_columns(df, columns_dict):
    df = df.rename(columns= columns_dict)
    return df
    
def mapping(df, column_name, value_map):
    df[column_name] = df[column_name].map(value_map)
    return df
    
def replace_column_value(df, column, column_dict):
    df[column] = df[column].replace(column_dict)
    return df

def process_column(df, column_name, char_to_replace, new_type):
    df[column_name] = df[column_name].str.replace(char_to_replace, '').astype(new_type)
    return df
def split_and_select_num(df, column_name, delimiter, part_index):
    df[column_name] = df[column_name].str.split(delimiter).str[part_index]
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    return df
                                        
                                        
def standardize_columns():
    df.rename(columns={'ST':'State', 'GENDER':'Gender'})
    return df

def standardie_values():
    df['Gender'].replace({'female': 'F', 'Femal': 'F', 'Male': 'M'}, inplace=True)
    df['State'].replace({'WA': 'Washington', 'AZ': 'Arizona', 'Cali': 'California'}, inplace=True)
    df['Education'].replace({'Bachelors': 'Bachelor'}, inplace=True)
    return df
    
def drop_null_values():
    df.dropna(subset=['Customer'])
    df.dropna(subset=['Gender'])
    return df

def change_types():
    df['Monthly Premium Auto'] = df['Monthly Premium Auto'].astype(int)
    return df

def drop_duplicates():
    df = df.drop_duplicates()
    return df

def main_cleaning_function(df):
    standardize_columns(df)
    standardie_values(df)
    drop_null_values(df)
    drop_duplicates(df)
    return df
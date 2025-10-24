def rename_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('(', '')
        .str.replace(')', '')
    )
    df = df.rename(columns={'customer': 'customer_id', 'st': 'state'})
    return df

def clean_invalid_values(df):
    df['gender'] = df['gender'].str.replace('Male', 'M').str.replace('female', 'F').str.replace('Femal', 'F')
    df['state'] = df['state'].str.replace('WA', 'Washington').str.replace('AZ', 'Arizona')
    df['education'] = df['education'].str.replace('Bachelors', 'Bachelor')
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '')
    df['vehicle_class'] = df['vehicle_class'].str.replace('Luxury Car', 'Luxury').str.replace('Sports Car', 'Luxury').str.replace('Luxury SUV', 'Luxury')
    return df

def formatting_data_types(df):
    df['customer_lifetime_value'] = df['customer_lifetime_value'].astype(float)
    df['number_of_open_complaints'] = df['number_of_open_complaints'].str.split('/').str[1]
    return df

def dealing_null_values(df):
    # Cleaning rows with missing values in all the columns
    df = df.dropna(how='all')
    # Filling missing values in CLV with the mean value of the column
    df.loc[:,'customer_lifetime_value'] = df['customer_lifetime_value'].fillna(df['customer_lifetime_value'].mean())
    # Filling missing values in gender with the mode of the column
    df.loc[:,'gender'] = df['gender'].fillna(df['gender'].mode()[0])
    return df

def main_cleaning(df):
    df = rename_columns(df)
    df = clean_invalid_values(df)
    df = formatting_data_types(df)
    df = dealing_null_values(df)
    return df
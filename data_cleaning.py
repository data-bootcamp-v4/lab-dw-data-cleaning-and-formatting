import pandas as pd

def load_data(url):
    return pd.read_csv(url)

def standardize_column_names(df):
    def standardize_column_name(col_name):
        col_name = col_name.lower().replace(' ', '_')
        if col_name == 'st':
            return 'state'
        return col_name
    df.columns = [standardize_column_name(col) for col in df.columns]
    return df

def clean_gender(df):
    df['gender'] = df['gender'].replace({
        'Femal': 'F', 'female': 'F', 'Female': 'F',
        'Male': 'M', 'male': 'M'
    })
    return df

def replace_state_abbreviations(df):
    state_replacements = {
        'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'
    }
    df['state'] = df['state'].replace(state_replacements)
    return df

def clean_education(df):
    df['education'] = df['education'].replace('Bachelors', 'Bachelor')
    return df

def clean_customer_lifetime_value(df):
    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '').astype(float)
    return df

def clean_number_of_open_complaints(df):
    def clean_complaints(value):
        if isinstance(value, str):
            return int(value.split('/')[1])
        return value
    df['number_of_open_complaints'] = df['number_of_open_complaints'].apply(clean_complaints).astype(float)
    return df

def replace_vehicle_class(df):
    vehicle_class_replacements = {
        'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'
    }
    df['vehicle_class'] = df['vehicle_class'].replace(vehicle_class_replacements)
    return df

def drop_duplicates(df):
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    return df

def save_data(df, filename):
    df.to_csv(filename, index=False)

def main():
    url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
    df = load_data(url)
    df = standardize_column_names(df)
    df = clean_gender(df)
    df = replace_state_abbreviations(df)
    df = clean_education(df)
    df = clean_customer_lifetime_value(df)
    df = clean_number_of_open_complaints(df)
    df = replace_vehicle_class(df)
    df = drop_duplicates(df)
    save_data(df, 'customer_data_cleaned_no_duplicates.csv')
    return df

if __name__ == "__main__":
    main()
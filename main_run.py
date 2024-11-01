from data_cleaning_functions.loading_function import load_data
from data_cleaning_functions.cleaning_function import drop_na, drop_duplicates, convert_numeric_columns_to_int
from data_cleaning_functions.rename_n_replace_function import rename_columns, replace_values

def main():
    url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
    insurance_data = load_data(url)

    rename_columns(insurance_data, {'st': 'state'})
    replace_values(insurance_data, 'state', {'WA': 'Washington', 'AZ': 'Arizona'})
    
    drop_na(insurance_data)
    drop_duplicates(insurance_data)
    
    # Convert all numeric columns to int
    convert_numeric_columns_to_int(insurance_data)

    print(insurance_data.head())

if __name__ == "__main__":
    main()
    
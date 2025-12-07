import pandas as pd

def cleaning_column_names(df, rename_dict={}):
    #replacing space with underscore in the column_names
    df.columns = [ col.replace(" ","_").lower() for col in df.columns ]

    # renaming the columns in the data frame if a renaming dict is given
    if rename_dict:
        df.rename(columns=rename_dict, inplace = True)

    return df 


def replace_values(df, replace_dict):

    """
    Docstring for replace_values
    
    :param df: Description
    :param replace_dict: A dictionary of type 
    {
        "col1": 
        {
            "old_value": "new_value"
        },

        "col2": 
        {
            "old_value": "new_value"
        },
    }

    """
    df = df.replace(replace_dict)
    return df 

def to_numeric(df, numeric_columns=[]):

    if numeric_columns:
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def cast_datatype(df, cast_dict):
    """
    Docstring for cast_datatype
    
    :param df: Description
    :param cast_dict: A dictionary of type 
    {
        "col1": "integer"

        "col2": "float"
    }

    """
    df.astype(cast_dict)
    return df


def numeric_to_int(df, numeric_columns =[]):
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors = "coerce").round().astype('Int64')
    return df



def handle_null(df, replace_null_dict ={}):

    # drop rows with all collumns as null
    df.dropna(how='all', inplace=True)

    if replace_null_dict:
        df = df.fillna(replace_null_dict)
    return df


def handle_duplicates(df, subset=None):

    df.drop_duplicates(subset, inplace=True)

    # Identifying the duplicate rows
    duplicates = df.duplicated()

    #Checking if there is any row duplicated; answer = no
    if not duplicates.any():
        print("There are no more duplicates")

    else:
        print("There are duplicates")
        print("Here are the duplicates rows")
        print(df[duplicates])

    return df


def main():
    url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
    company_df = pd.read_csv(url)

    company_df = cleaning_column_names(company_df, rename_dict={'st': 'state'})
    replace_dict = {
        "gender" : {"Femal":"F", "female":"F", "Male":"M"},
        "state": {"Cali":"California", "AZ":"Arizona", "WA": "Washington"},
        "education": {"Bachelors":"Bachelor"},
        "vehicle_class": {"Sports Car": "Luxury", "Luxury SUV":"Luxury", "Luxury Car": "Luxury"}
        }
    company_df = replace_values(company_df, replace_dict)

    # remove %
    company_df['customer_lifetime_value'] = company_df['customer_lifetime_value'].str.replace('%', '', regex=False)
    company_df = to_numeric(company_df, numeric_columns=["customer_lifetime_value"])
    company_df = cast_datatype(company_df, cast_dict={"customer_lifetime_value":"float64"})

    #splitting the format of number_of_complaints and turning it into an integer 
    company_df['number_of_open_complaints'] =company_df['number_of_open_complaints'].str.split('/').str[1].astype('Int64')
    replace_null_dict = {'gender':'unknown','customer_lifetime_value': round(company_df.customer_lifetime_value.mean(),2) }
    company_df = handle_null(company_df, replace_null_dict = replace_null_dict)
    company_df = numeric_to_int(company_df, numeric_columns=["customer_lifetime_value", 'income', 'monthly_premium_auto', 'total_claim_amount'])
    company_df = handle_duplicates(company_df)

    print(company_df)

if __name__ == "__main__":
    main()













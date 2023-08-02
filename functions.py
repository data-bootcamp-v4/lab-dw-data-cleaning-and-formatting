def rename_columns(df):
    new_col_names = [name.strip().lower().replace(' ', '_') for name in df.columns]
    new_col_names = ['state' if name == 'st' else name for name in new_col_names]
    df.columns = new_col_names

def consolidate_gender(row):
    if type(row['gender']) != float:
        if row.gender == 'Male':
            return 'M'
        elif row['gender'] == 'female' or row['gender'] == 'Femal':
            return 'F'
        else:
            return row['gender']


def consolidate_complaints(row):
    if type(row['number_of_open_complaints']) == str:
        return int(row['number_of_open_complaints'].split('/')[1])
    else:
        return row['number_of_open_complaints']


def consolidate_lifetime_value(row):
    if type(row['customer_lifetime_value']) == str:
        return float(row['customer_lifetime_value'].strip('%'))/100
    else:
        return row['customer_lifetime_value']


def replace_null_values(df, column, replacement):
    df[column].fillna(replacement, inplace=True)
    

def main():
    df = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv')
    
    rename_columns(df)
    df['gender'] = df.apply(consolidate_gender, axis=1)
    
    df['number_of_open_complaints'] = df.apply(consolidate_complaints, axis=1)
    df['customer_lifetime_value'] = df.apply(consolidate_lifetime_value, axis=1)
    
    replace_null_values(df, 'gender', 'O')
    replace_null_values(df, 'education', 'other')

    df.dropna(inplace=True)

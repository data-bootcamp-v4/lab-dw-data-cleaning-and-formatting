import pandas as pd

## loading data set
url="https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"

data = pd.read_csv(url)


print("DataSet \n",data )



#Data Preprossing
df1 = data.copy()
df1

df1= df1.rename(columns= {'ST':'State'})
df1.head()

def trim(df):
    # Strip leading and trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop duplicate rows to ensure unique entries
    df = df.drop_duplicates()

    # Convert all column names to lowercase for consistency
    df.columns = df.columns.str.lower()

    # Replace spaces in column names with underscores for easier access
    df.columns = df.columns.str.replace(' ', '_')

    # Select columns with object data types (categorical/textual data)
    df_obj = df.select_dtypes(['object'])

    # Convert object type columns to string and strip whitespace from each value
    df[df_obj.columns] = df_obj.apply(lambda x: x.astype(str).str.strip())

    # Print confirmation message after cleaning
    print("All column names cleaned, duplicates dropped, and text columns processed.")

    # Return the cleaned DataFrame
    return df   


#Column names should be in lower case
#Data types should be specified
df1_clean= trim(df1)
print("updated data set \n",df1_clean)

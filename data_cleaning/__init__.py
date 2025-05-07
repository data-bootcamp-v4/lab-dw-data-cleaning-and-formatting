

%%writefile data_cleaning/__clean_column_names__.py
# clean column names
import pandas as pd

df.columns = [column.lower().replace(" ","-").replace("ST","state") for column in df.columns]


%%writefile data_cleaning/clean_gender_column.py
#clean gender column
def clean_gender_column(df):
    def gender_category(value):
        if value == "Male":
            return "M"
        elif value == "female":
            return "F"
        elif value == "Femal":
            return "F"
        else:
            return value

    df["gender"] = df["gender"].apply(gender_category)
    return df
    

%%writefile data_cleaning/clv_to_intr.py
# covert CLV to integer
def clv_to_intr(df):
    def remove_percentage_char(value):
        if type(value) == str:
            return float(value.strip("%"))
        else:
            return value
    df["customer-lifetime-value"] = df["customer-lifetime-value"].apply(remove_percentage_char)
    return df



%%writefile data_cleaning/clean_number_of_complains.py
# convert number of complaints into inter
def clean_number_of_complains(value):
    if type(value) == str:
        return int(value.split("/")[1])
    else:
        return value

df["number-of-open-complaints"] = df["number-of-open-complaints"].apply(clean_number_of_complains)



%%writefile data_cleaning/drop_full_null_columns.py
# drop the rows or columns with null values
df = df.dropna(axis=0, how="all")



%%writefile data_cleaning/null_gender_to_mode.py
# fill null vales in gender with mode
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])



%%writefile data_cleaning/null_cv_to_median.py
# fill null values in CLV with median
df["customer-lifetime-value"] = df["customer-lifetime-value"].fillna(df["customer-lifetime-value"].median())



%%writefile data_cleaning/convert_full_df_to_int.py
# convert all values to int
df = df.select_dtypes(include=["number"]).astype("int")



%%writefile data_cleaning/remove_duplicates.py
# remove duplicates & save them in a new file
df_duplicates = df.copy()

df_duplicates.drop_duplicates(keep = "first")

df_duplicates.to_csv("./data/df_duplicates_lab.csv")
    

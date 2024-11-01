def drop_na(data):
    data.dropna(inplace=True)

def drop_duplicates(data):
    data.drop_duplicates(inplace=True)

def convert_numeric_columns_to_int(data):
    # Select columns of type float and convert them to int
    float_cols = data.select_dtypes(include=['float64']).columns
    data[float_cols] = data[float_cols].astype(int)
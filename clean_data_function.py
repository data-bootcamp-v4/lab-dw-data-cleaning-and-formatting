def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ","_")
    df.rename(columns={"st":"state"}, inplace=True)
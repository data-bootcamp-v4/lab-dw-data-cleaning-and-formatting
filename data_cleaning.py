import pandas as pd

# Limpia los nombres de las columnas
def clean_column_names(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.rename(columns={"st": "state"})
    return df

# Limpia valores inconsistentes
def clean_invalid_values(df):

    df["gender"] = df["gender"].replace({
        "Femal": "F",
        "female": "F",
        "Male": "M"
    })

    df["state"] = df["state"].replace({
        "AZ": "Arizona",
        "Cali": "California",
        "WA": "Washington"
    })

    df["education"] = df["education"].replace({
        "Bachelors": "Bachelor"
    })

    df["customer_lifetime_value"] = (
        df["customer_lifetime_value"].str.replace("%", "")
    )

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"
    })

    return df

# Corrige los tipos de datos
def format_data_types(df):
    df["customer_lifetime_value"] = pd.to_numeric(
        df["customer_lifetime_value"]
    )

    df["number_of_open_complaints"] = (
        df["number_of_open_complaints"].str.split("/").str[1]
    )

    df["number_of_open_complaints"] = pd.to_numeric(
        df["number_of_open_complaints"]
    )

    return df

# Rellena los valores nulos
def handle_nulls(df):
    numeric_columns = df.select_dtypes(include="number").columns

    df[numeric_columns] = df[numeric_columns].fillna(
        df[numeric_columns].median()
    )

    text_columns = df.select_dtypes(include="str").columns

    for column in text_columns:
        df[column] = df[column].fillna(df[column].mode()[0])

    numeric_columns = df.select_dtypes(include="number").columns
    df[numeric_columns] = df[numeric_columns].astype(int)

    return df

# Elimina las filas duplicadas
def remove_duplicates(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df

# Ejecuta todo el proceso de limpieza
def clean_data(df):
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = handle_nulls(df)
    df = remove_duplicates(df)

    return df
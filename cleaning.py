import pandas as pd

# Ejercicio 1: limpiar los nombres de las columnas
def clean_column_names(df):
    df.columns = [column.lower().replace(" ", "_")for column in df.columns]

    df = df.rename(columns={"st": "state"})

    return df


# Ejercicio 2: unificar valores
def clean_values(df):
    df["gender"] = df["gender"].replace({"Femal": "F","female": "F","Male": "M"})

    df["state"] = df["state"].replace({"Cali": "California","AZ": "Arizona","WA": "Washington"})

    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})

    df["customer_lifetime_value"] = (df["customer_lifetime_value"].str.replace("%", ""))

    df["vehicle_class"] = df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury SUV": "Luxury",
        "Luxury Car": "Luxury"})

    return df


# Función auxiliar: extraer el número de quejas
def extract_complaints(value):
    try:
        parts = value.split("/")
        return parts[1]
    except AttributeError:
        return value


# Ejercicio 3: convertir los tipos de datos
def format_data_types(df):
    df["customer_lifetime_value"] = (df["customer_lifetime_value"].astype(float))

    df["number_of_open_complaints"] = (df["number_of_open_complaints"].apply(extract_complaints))

    df["number_of_open_complaints"] = (df["number_of_open_complaints"].astype(float))

    return df


# Ejercicio 4: tratar los nulos y convertir a enteros
def clean_null_values(df):
    df = df.dropna(how="all")

    df["gender"] = df["gender"].fillna("Unknown")

    clv_median = df["customer_lifetime_value"].median()

    df["customer_lifetime_value"] = (df["customer_lifetime_value"].fillna(clv_median))

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        df[column] = df[column].astype(int)

    return df


# Ejercicio 5: eliminar duplicados y reorganizar el índice
def clean_duplicates(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df


# Función principal: ejecutar todos los pasos en orden
def clean_data(df):
    df = clean_column_names(df)
    df = clean_values(df)
    df = format_data_types(df)
    df = clean_null_values(df)
    df = clean_duplicates(df)

    return df
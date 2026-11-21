import pandas as pd


def clean_column_names(df):
    """Estandariza los nombres de las columnas."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    
    df = df.rename(columns={"st": "state"})
    return df


def clean_categorical_data(df):
    """Estandariza los valores de las columnas categóricas."""
    
    df["gender"] = df["gender"].replace({
        "M": "Male",
        "F": "Female",
        "Femal": "Female",
        "female": "Female"
    })

    df["state"] = df["state"].str.upper()

    return df


def format_data_types(df):
    """Convierte las columnas necesarias a formato numérico."""

    df["customer_lifetime_value"] = pd.to_numeric(
        df["customer_lifetime_value"],
        errors="coerce"
    )

    df["number_of_open_complaints"] = (
        df["number_of_open_complaints"]
        .str.split("/")
        .str[1]
    )

    df["number_of_open_complaints"] = pd.to_numeric(
        df["number_of_open_complaints"],
        errors="coerce"
    )

    return df


def handle_missing_values(df):
    """Gestiona los valores nulos."""

    # Eliminamos filas completamente vacías
    df = df.dropna(how="all")

    # Rellenamos columnas numéricas con la mediana
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    # Rellenamos columnas categóricas con la moda
    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:
        if not df[column].mode().empty:
            df[column] = df[column].fillna(df[column].mode()[0])

    return df


def remove_duplicates(df):
    """Elimina filas duplicadas conservando la primera."""
    df = df.drop_duplicates(keep="first")
    return df


def clean_data(df):
    """Ejecuta todo el proceso de limpieza."""

    df = clean_column_names(df)
    df = clean_categorical_data(df)
    df = format_data_types(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    return df
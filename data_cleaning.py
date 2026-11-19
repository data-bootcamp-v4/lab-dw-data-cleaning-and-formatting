"""Funciones de limpieza y formato para los datos de clientes (file1.csv)."""
import pandas as pd


def clean_column_names(df):
    """Columnas en minúsculas, espacios -> '_', y 'st' -> 'state'."""
    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df.rename(columns={"st": "state"})


def clean_invalid_values(df):
    """Unifica valores escritos de distintas formas."""
    df = df.copy()
    df["gender"] = df["gender"].replace({"Femal": "F", "female": "F", "Male": "M"})
    df["state"] = df["state"].replace({"AZ": "Arizona", "Cali": "California", "WA": "Washington"})
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")
    df["vehicle_class"] = df["vehicle_class"].replace(
        {"Sports Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"})
    return df


def format_data_types(df):
    """CLV a número y 'number_of_open_complaints' ('1/5/00' -> 5)."""
    df = df.copy()
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"])
    df["number_of_open_complaints"] = pd.to_numeric(
        df["number_of_open_complaints"].str.split("/").str[1])
    return df


def handle_nulls(df):
    """Borra filas vacías; rellena numéricas con la mediana y texto con la moda; pasa números a enteros."""
    df = df.dropna(how="all").copy()
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].round().astype(int)
    return df


def handle_duplicates(df):
    """Elimina filas duplicadas (se queda con la primera) y reinicia el índice."""
    return df.drop_duplicates(keep="first").reset_index(drop=True)


def main(url="https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"):
    """Ejecuta toda la limpieza y devuelve el DataFrame limpio."""
    df = pd.read_csv(url)
    df = clean_column_names(df)
    df = clean_invalid_values(df)
    df = format_data_types(df)
    df = handle_nulls(df)
    df = handle_duplicates(df)
    return df


if __name__ == "__main__":
    clean = main()
    clean.to_csv("clean_customers.csv", index=False)
    print(clean.shape)

import pandas as pd


def clean_column_names(df):
    """Estandariza los nombres de columnas: minúsculas, sin espacios, st→state."""
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ', '_', regex=False)
    )
    df.columns = ['state' if col == 'st' else col for col in df.columns]
    return df


def clean_invalid_values(df):
    """Limpia valores inconsistentes en gender, state, education, CLV y vehicle_class."""

    df['gender'] = df['gender'].str.strip()
    df['gender'] = df['gender'].replace({
        'Femal': 'F', 'female': 'F', 'Female': 'F',
        'Male': 'M', 'male': 'M'
    })

    df['state'] = df['state'].replace({
        'AZ': 'Arizona',
        'Cali': 'California',
        'WA': 'Washington'
    })

    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})

    df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '', regex=False)

    df['vehicle_class'] = df['vehicle_class'].replace({
        'Sports Car': 'Luxury',
        'Luxury SUV': 'Luxury',
        'Luxury Car': 'Luxury'
    })

    return df


def format_data_types(df):
    """Corrige los tipos de datos de las columnas."""

    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors='coerce')

    df['number_of_open_complaints'] = (
        df['number_of_open_complaints']
        .str.split('/')
        .str[1]
        .astype(float)
    )

    return df


def handle_null_values(df):
    """Elimina filas vacías y rellena nulos con mediana/moda."""

    # Eliminar filas completamente vacías y hacer copia explícita
    df = df.dropna(how='all').copy()

    # Variables numéricas → mediana
    numerical_cols = df.select_dtypes(include='float64').columns
    for col in numerical_cols:
        df.loc[:, col] = df[col].fillna(df[col].median())

    # Variables categóricas → moda
    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        df.loc[:, col] = df[col].fillna(df[col].mode()[0])

    # Convertir numéricos a enteros
    for col in numerical_cols:
        df.loc[:, col] = df[col].astype(int)

    return df


def handle_duplicates(df):
    """Elimina duplicados y resetea el índice."""
    df = df.drop_duplicates(keep='first')
    df = df.reset_index(drop=True)
    return df


def main(url):
    """Función principal que ejecuta todos los pasos de limpieza."""

    print("Cargando datos...")
    df = pd.read_csv(url)

    print("Limpiando nombres de columnas...")
    df = clean_column_names(df)

    print("Limpiando valores inválidos...")
    df = clean_invalid_values(df)

    print("Formateando tipos de datos...")
    df = format_data_types(df)

    print("Manejando valores nulos...")
    df = handle_null_values(df)

    print("Manejando duplicados...")
    df = handle_duplicates(df)

    print(f"\n✅ Limpieza completada! Shape final: {df.shape}")
    return df


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    df = main(url)
    df.to_csv('clean_data.csv', index=False)
    print("💾 Dataset guardado como 'clean_data.csv'")

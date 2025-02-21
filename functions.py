import pandas as pd

def identify_duplicates(df):
    num_duplicates = df.duplicated().sum()
    print(f"Número de filas duplicadas: {num_duplicates}")
    return num_duplicates

def remove_duplicates(df):
    df = df.drop_duplicates(keep='first')
    return df

def verify_no_duplicates(df):
    num_duplicates_after = df.duplicated().sum()
    print(f"Número de filas duplicadas después de limpieza: {num_duplicates_after}")
    return num_duplicates_after

def reset_index(df):
    df.reset_index(drop=True, inplace=True)
    return df

def save_cleaned_data(df, filename):
    df.to_csv(filename, index=False)
    print(f"El dataset ha sido limpiado de duplicados y guardado como '{filename}'.")

# Function to standardize gender values
def clean_gender(gender):
    if pd.isna(gender):
        return gender
    gender = gender.strip().lower()
    if gender in ['female', 'femal', 'f']:
        return 'F'
    elif gender in ['male', 'm']:
        return 'M'
    else:
        return gender
    
# Estrategia para manejar valores nulos
# - Para columnas numéricas, se rellenan con la mediana de la columna.
# - Para columnas categóricas, se rellenan con la moda (valor más frecuente).
def fillna_columns(df):
    for column in df.columns:
        if df[column].isnull().sum() > 0:  # Si la columna tiene valores nulos
            if df[column].dtype in ['int64', 'float64']:  # Si es numérica
                median_value = df[column].median()
                df[column] = df[column].fillna(median_value)
            else:  # Si es categórica
                mode_value = df[column].mode()[0]
                df[column] = df[column].fillna(mode_value)
    return df

def main(df):
    identify_duplicates(df)
    df = remove_duplicates(df)
    verify_no_duplicates(df)
    df = reset_index(df)
    save_cleaned_data(df, 'data/processed/file1_no_duplicates.csv')
    print(df.shape)  # Mostrar el tamaño del dataframe tras la eliminación de duplicados

if __name__ == "__main__":
    # Cargar el dataframe aquí si se ejecuta este script directamente
    df = pd.read_csv('data/raw/file1.csv')  # Ajusta el path según sea necesario
    main(df)
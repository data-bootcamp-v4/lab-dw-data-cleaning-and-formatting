import pandas as pd
import numpy as np 

#  1. Carga de Datos y Formato Inicial

def load_data(url):
    return pd.read_csv(url)

def initial_formatting(df):
    # Hacer una copia para evitar SettingWithCopyWarning
    df_copy = df.copy()

    # Formato de nombres de columnas
    df_copy.columns = df_copy.columns.str.lower().str.replace(' ', '_')

    # Renombrar columna
    df_copy.rename(columns={'st': 'state'}, inplace=True)

    return df_copy

#  2. Corrección y Estandarización de Valores Categóricos

def clean_categorical_values(df):
    df_copy = df.copy()

    # Mapeo de valores
    generos = {'M': 'Male', 'F': 'Female', 'female': 'Female', 'Femal': 'Female'}
    estados = {'Cali': 'California', 'AZ': 'Arizona', 'WA': 'Washington'}
    grado = {'Bachelors': 'Bachelor'}
    auto = {'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'}

    # Aplicar mapeos
    df_copy['gender'] = df_copy['gender'].replace(generos)
    df_copy['state'] = df_copy['state'].replace(estados)
    df_copy['education'] = df_copy['education'].replace(grado)
    df_copy['vehicle_class'] = df_copy['vehicle_class'].replace(auto)

    return df_copy

#  3. Limpieza y Conversión de Tipos de Datos (Numéricos)

def clean_numerical_data_types(df):
    df_copy = df.copy()

    # Limpieza de 'customer_lifetime_value'
    df_copy['customer_lifetime_value'] = (
        df_copy['customer_lifetime_value']
        .astype(str) 
        .str.replace('%', '')
        .astype(float)
    )

    # Limpieza de 'number_of_open_complaints'
    df_copy['number_of_open_complaints'] = (
        df_copy['number_of_open_complaints']
        .astype(str) 
        .str.split('/')
        .str[1]
    )
    # Reemplazar 'nan' (string) con un valor NaN real para la conversión
    df_copy['number_of_open_complaints'].replace({'nan': np.nan}, inplace=True)
    # Convertir a Int64 (el tipo de entero de pandas que maneja valores NaN)
    df_copy['number_of_open_complaints'] = df_copy['number_of_open_complaints'].astype('Int64')

    return df_copy

#  4. Gestión de Valores Faltantes y Duplicados 

def handle_missing_and_duplicate_values(df):
    df_copy = df.copy()

    # Eliminar filas con muchos NaN (thresh=10)
    df_copy = df_copy.dropna(thresh=10)

    # Eliminar la columna 'number_of_open_complaints'
    df_copy = df_copy.drop(columns=['number_of_open_complaints'])

    # Imputación de faltantes
    # Rellenar 'gender' usando forward fill
    df_copy['gender'] = df_copy['gender'].ffill()

    # Rellenar 'customer_lifetime_value' con la media
    media_clv = df_copy['customer_lifetime_value'].mean()
    df_copy['customer_lifetime_value'] = df_copy['customer_lifetime_value'].fillna(media_clv)

    # Eliminar duplicados
    df_copy = df_copy.drop_duplicates(keep='first')

    # Resetear el índice
    df_copy = df_copy.reset_index(drop=True)

    return df_copy

#  5. Conversión Final de Tipos de Datos 

def final_type_conversion(df):
    """Convierte las columnas finales a tipos de datos enteros (int64)."""
    df_copy = df.copy()

    # Conversión a int64
    for col in ['customer_lifetime_value', 'income', 'monthly_premium_auto', 'total_claim_amount']:
        df_copy[col] = df_copy[col].astype('int64')

    return df_copy

# --- 🎯 FUNCIÓN PRINCIPAL DE LIMPIEZA ---

def clean_and_format_data(url):
    """
    Realiza todos los pasos de limpieza y formateo en el orden correcto.

    Argumentos:
        url (str): La URL del archivo CSV a cargar.

    Retorna:
        pd.DataFrame: El DataFrame limpio y formateado.
    """
    print("Iniciando la carga de datos...")
    df = load_data(url)

    print("Paso 1: Formato inicial de columnas...")
    df = initial_formatting(df)

    print("Paso 2: Limpieza y estandarización de valores categóricos...")
    df = clean_categorical_values(df)

    print("Paso 3: Limpieza y conversión de tipos numéricos (CLV y Complaints)...")
    df = clean_numerical_data_types(df)

    print("Paso 4: Gestión de valores faltantes y duplicados...")
    df = handle_missing_and_duplicate_values(df)

    print("Paso 5: Conversión final de tipos de datos (entero)...")
    df = final_type_conversion(df)

    print("✅ Limpieza de datos completada.")
    return df

# --- 6. Guardar el DataFrame ---

def save_data(df, filename='datos_limpios_sin_duplicados.csv'):
    """Guarda el DataFrame limpio en un archivo CSV."""
    df.to_csv(filename, index=False)
    print(f"Datos guardados en '{filename}'")

if __name__ == '__main__':
    # Ejemplo de uso si el archivo se ejecuta directamente
    # Se recomienda usar el archivo main.py para el flujo principal
    url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
    df_limpio = clean_and_format_data(url)
    save_data(df_limpio)
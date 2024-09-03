import pandas as pd
import re

def limpiar_fecha(source):
    """
    Elimina las fechas en formato ', dd/mm/yyyy' de una cadena.
    """
    if isinstance(source, str):
        return re.sub(r', \d{1,2}/\d{1,2}/\d{4}', '', source)
    return source

def eliminar_columnas(df, columnas):
    """
    Elimina las columnas especificadas de un DataFrame.
    """
    return df.drop(columns=columnas)

def convertir_a_cadenas(df, columnas):
    """
    Convierte los valores en las columnas especificadas a cadenas.
    """
    for col in columnas:
        df[col] = df[col].astype(str)
    return df

def limpiar_datos(df):
    """
    Realiza todas las etapas de limpieza de datos.
    """
    # Aquí puedes agregar más pasos de limpieza si es necesario.
    df = convertir_a_cadenas(df, ['source'])
    df['source'] = df['source'].apply(limpiar_fecha)
    df = eliminar_columnas(df, ['unnamed_11', 'unnamed_21', 'unnamed_22'])
    return df

def main(file_path):
    """
    Función principal que carga el DataFrame, limpia los datos y lo guarda.
    """
    df = pd.read_csv(file_path)
    df_limpio = limpiar_datos(df)
    df_limpio.to_csv('data_limpio.csv', index=False)
    print("Datos limpios guardados en 'data_limpio.csv'.")

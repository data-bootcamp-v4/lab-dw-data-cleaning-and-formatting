import pandas as pd

def limpiar_nombres_columnas(df):
    """Normaliza nombres de columnas a minúsculas y guiones bajos."""
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def limpiar_clv(df):
    """Elimina el símbolo % de customer_lifetime_value y lo convierte a float."""
    col = 'customer_lifetime_value'
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('%', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def gestionar_nulos_y_duplicados(df):
    """Elimina duplicados y filas con valores nulos, reseteando el índice."""
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna().reset_index(drop=True)
    return df

def limpiar_texto(df):
    """Limpia espacios en blanco y pone en mayúsculas las columnas de texto."""
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].astype(str).str.strip().str.upper()
    return df

def informe_detallado(df):
    """Muestra el resumen final del DataFrame."""
    print("\n--- INFORME FINAL (2026) ---")
    print(f"Dimensiones finales: {df.shape}")
    print(f"Duplicados: {df.duplicated().sum()}")
    print(f"Nulos totales: {df.isnull().sum().sum()}")
    print("\nPrimeras filas:")
    print(df.head())
    return df

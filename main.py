import pandas as pd
# Importamos todas las funciones del archivo anterior
from limpieza_util import (
    limpiar_nombres_columnas,
    limpiar_clv,
    gestionar_nulos_y_duplicados,
    limpiar_texto,
    informe_detallado
)

def ejecutar_pipeline_limpieza(ruta_entrada, ruta_salida):
    print(f"Iniciando limpieza de: {ruta_entrada}")
    
    # 1. Cargar datos
    df = pd.read_csv(ruta_entrada)
    
    # 2. Aplicar funciones en orden
    df = limpiar_nombres_columnas(df)
    df = limpiar_clv(df)
    df = gestionar_nulos_y_duplicados(df)
    df = limpiar_texto(df)
    
    # 3. Mostrar informe en consola
    informe_detallado(df)
    
    # 4. Guardar el archivo limpio
    df.to_csv(ruta_salida, index=False)
    print(f"\n✅ Proceso completado. Archivo guardado como: {ruta_salida}")

if __name__ == "__main__":
    # Asegúrate de que el nombre del archivo coincida con el tuyo
    ejecutar_pipeline_limpieza('tu_archivo_original.csv', 'datos_limpios_2026.csv')


# Importas la función principal de tu script
from data_cleaning import ejecutar_pipeline_limpieza

# Ejecutas todo el flujo de golpe
df_limpio = ejecutar_pipeline_limpieza('customer_analysis.csv', 'customer_analysis_clean.csv')

# Compruebas el resultado directo en tu notebook
df_limpio.head()
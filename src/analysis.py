import os
import pandas as pd

# 1. Cargar el dataset
data_path = os.path.join("data", "StudentsPerformance.csv")
df = pd.read_csv(data_path)

# 2. Exploración inicial
print("=== EXPLORACIÓN INICIAL ===")
print(f"Número de registros: {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}")
print("\nTipos de datos y nulos:")
print(df.info())
print(f"\nRegistros duplicados: {df.duplicated().sum()}")
print("\nEstadísticas descriptivas:")
print(df.describe())

# 3. Limpieza y creación de variables requeridas
# Crear average_score (promedio de math, reading, writing)
df["average_score"] = df[
    ["math score", "reading score", "writing score"]
].mean(axis=1)


# Clasificación del rendimiento académico
def clasificar_rendimiento(promedio):
    if promedio < 60:
        return "Bajo"
    elif promedio < 80:
        return "Medio"
    else:
        return "Alto"


df["rendimiento"] = df["average_score"].apply(clasificar_rendimiento)

print("\n=== DISTRIBUCIÓN DE RENDIMIENTO ===")
print(df["rendimiento"].value_counts())
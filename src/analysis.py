import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configurar carpetas y cargar dataset
os.makedirs(os.path.join("outputs", "resultados"), exist_ok=True)
data_path = os.path.join("data", "StudentsPerformance.csv")
df = pd.read_csv(data_path)

# Crear variables de promedio y clasificación
df["average_score"] = df[
    ["math score", "reading score", "writing score"]
].mean(axis=1)


def clasificar_rendimiento(promedio):
    if promedio < 60:
        return "Bajo"
    elif promedio < 80:
        return "Medio"
    else:
        return "Alto"


df["rendimiento"] = df["average_score"].apply(clasificar_rendimiento)

print("=== 4 ANÁLISIS DEL RENDIMIENTO ACADÉMICO ===")

# 1. Área con promedio más alto
promedios = df[["math score", "reading score", "writing score"]].mean()
print("\n1. Promedio por área académica:")
print(promedios)

# 2. Impacto del curso de preparación
prep_course = df.groupby("test preparation course")["average_score"].mean()
print("\n2. Promedio general según curso de preparación:")
print(prep_course)

# 3. Rendimiento según nivel educativo de los padres
parent_edu = (
    df.groupby("parental level of education")["average_score"]
    .mean()
    .sort_values(ascending=False)
)
print("\n3. Promedio según educación de los padres:")
print(parent_edu)

# 4. Porcentaje por categoría de rendimiento
porcentajes = df["rendimiento"].value_counts(normalize=True) * 100
print("\n4. Porcentaje de estudiantes por nivel de rendimiento:")
print(porcentajes)

# === GENERACIÓN DE VISUALIZACIONES ===
sns.set_theme(style="whitegrid")

# Gráfico 1: Comparación de materias
plt.figure(figsize=(8, 5))
sns.barplot(x=promedios.index, y=promedios.values, palette="viridis")
plt.title("Promedio General por Materia")
plt.ylabel("Puntaje Promedio")
plt.savefig(
    os.path.join("outputs", "resultados", "01_promedio_por_materia.png")
)
plt.close()

# Gráfico 2: Impacto del curso de preparación
plt.figure(figsize=(7, 5))
sns.boxplot(
    x="test preparation course",
    y="average_score",
    data=df,
    palette="Set2",
)
plt.title("Impacto del Curso de Preparación en el Promedio")
plt.savefig(os.path.join("outputs", "resultados", "02_curso_preparacion.png"))
plt.close()

# Gráfico 3: Distribución del nivel de rendimiento
plt.figure(figsize=(7, 5))
df["rendimiento"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", colors=["#66b3ff", "#99ff99", "#ffcc99"]
)
plt.title("Distribución de Estudiantes por Criterio de Rendimiento")
plt.ylabel("")
plt.savefig(os.path.join("outputs", "resultados", "03_distribucion_nivel.png"))
plt.close()

print("\n¡Análisis y visualizaciones generadas exitosamente!")
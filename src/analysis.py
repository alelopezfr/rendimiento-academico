import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_dir = os.path.join(BASE_DIR, "outputs", "resultados")
os.makedirs(output_dir, exist_ok=True)

data_path = os.path.join(BASE_DIR, "data", "StudentsPerformance.csv")
df = pd.read_csv(data_path)

print("EXPLORACIÓN INICIAL DE LOS DATOS")
print(f"Número de registros (filas): {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}")

print("\nNombres de las variables y tipos de datos:")
print(df.dtypes)

print("\nValores faltantes por columna:")
print(df.isnull().sum())

print(f"\nRegistros duplicados: {df.duplicated().sum()}")

print("\nEstadísticas descriptivas de variables numéricas:")
print(df.describe())

df = df.drop_duplicates()

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

print("\nANÁLISIS DEL RENDIMIENTO ACADÉMICO")

promedios = df[["math score", "reading score", "writing score"]].mean()
print("\n1. Promedio por área académica:")
print(promedios)

prep_course = df.groupby("test preparation course")["average_score"].mean()
print("\n2. Promedio general según curso de preparación:")
print(prep_course)

parent_edu = (
    df.groupby("parental level of education")["average_score"]
    .mean()
    .sort_values(ascending=False)
)
print("\n3. Promedio según educación de los padres:")
print(parent_edu)

porcentajes = df["rendimiento"].value_counts(normalize=True) * 100
print("\n4. Porcentaje de estudiantes por nivel de rendimiento:")
print(porcentajes)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.barplot(x=promedios.index, y=promedios.values, hue=promedios.index, legend=False, palette="viridis")
plt.title("Promedio General por Materia")
plt.ylabel("Puntaje Promedio")
plt.savefig(os.path.join(output_dir, "01_promedio_por_materia.png"))
plt.close()

plt.figure(figsize=(7, 5))
sns.boxplot(
    x="test preparation course",
    y="average_score",
    hue="test preparation course",
    legend=False,
    data=df,
    palette="Set2",
)
plt.title("Impacto del Curso de Preparación en el Promedio")
plt.savefig(os.path.join(output_dir, "02_curso_preparacion.png"))
plt.close()

plt.figure(figsize=(7, 5))
df["rendimiento"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", colors=["#66b3ff", "#99ff99", "#ffcc99"]
)
plt.title("Distribución de Estudiantes por Criterio de Rendimiento")
plt.ylabel("")
plt.savefig(os.path.join(output_dir, "03_distribucion_nivel.png"))
plt.close()

print("\nRESPUESTAS A PREGUNTAS DE ANÁLISIS Y CONCLUSIONES")

print("\n1. ¿Cuál de las tres áreas tiene el promedio más alto?")
print("La materia con el promedio más alto es Lectura (69.17), seguida de Escritura (68.05) y Matemáticas (66.09).")

print("\n2. ¿Los estudiantes que realizaron el curso de preparación presentan mejores resultados?")
print("Sí. Quienes completaron el curso obtuvieron un promedio de 72.67 frente a 65.04 de quienes no lo hicieron, representando una ventaja de 7.63 puntos.")

print("\n3. ¿Existen diferencias en el rendimiento según el nivel educativo de los padres?")
print("Sí. Los estudiantes cuyos padres cuentan con maestría encabezan las notas con 73.60 de promedio, mientras que los de padres con preparatoria registran el promedio más bajo con 63.10.")

print("\n4. ¿Qué porcentaje de estudiantes alcanza determinado promedio / nivel de rendimiento?")
print("El 51.7% se posiciona en rendimiento Medio (60-79 puntos), el 28.5% en rendimiento Bajo (<60 puntos) y el 19.8% alcanza un rendimiento Alto (>=80 puntos).")

print("\n5. Conclusiones Generales:")
print("El nivel formativo del entorno familiar y los cursos preparatorios muestran una correlación directa e importante con el rendimiento académico.")
print("El área cuantitativa (Matemáticas) representa el mayor reto para los estudiantes en comparación con las competencias de lectura y escritura.")
# Proyecto 1: Análisis del Rendimiento Académico

## Descripción del Proyecto
Este proyecto realiza un análisis exploratorio de datos sobre los resultados académicos de un grupo de estudiantes en exámenes de matemáticas, lectura y escritura.

## Dataset
* **Nombre:** Students Performance in Exams
* **Fuente:** Kaggle
* **Descripción:** Contiene información demográfica y los puntajes de exámenes obtenidos por los estudiantes.

## Requisitos
* Python 3.9 o superior
* Entorno virtual de Python (`.venv`)
* Requirements, también incluidas en el acrhivo requirements.txt

contourpy==1.4.0
cycler==0.12.1
fonttools==4.65.0
kiwisolver==1.5.1
matplotlib==3.11.2
numpy==2.5.3
packaging==26.3
pandas==3.0.6
pillow==12.3.0
pyparsing==3.3.2
python-dateutil==2.9.0.post0
seaborn==0.13.2
six==1.17.0
tzdata==2026.4


## Instalación
Para ejecutar este proyecto de forma local, asegúrate de tener instalado Python y las bibliotecas necesarias:

1. Clonar el repositorio:
   git clone [https://github.com/alelopezfr/rendimiento-academico.git](https://github.com/alelopezfr/rendimiento-academico.git)
2. Entrar al proyecto
   cd rendimiento-academico
3. Crear entorno virtual
    python -m venv .venv
4. Instalar dependencias
   pip install -r requirements.txt

## Ejecución

Para ejecutar el análisis del proyecto, asegúrate de estar en la carpeta raíz y corre el siguiente comando en tu terminal:
    python src/analysis.py

## Análisis Realizados

Se evaluaron las calificaciones de los estudiantes considerando distintas variables socioeducativas:

1. Promedio por área académica: Comparativa general en Matemáticas (`math score`), Lectura (`reading score`) y Escritura (`writing score`).
2. Impacto del curso de preparación: Evaluación del desempeño académico entre quienes completaron el curso de preparación para exámenes y quienes no.
3. Influencia del nivel educativo de los padres: Análisis del desempeño general según el grado académico máximo de los padres.
4. Distribución por nivel de rendimiento: Clasificación de los alumnos en categorías de rendimiento académico (*Bajo*, *Medio* y *Alto*).

## Resultados y Conclusiones

* Áreas académicas: Los estudiantes obtuvieron el promedio más alto en Lectura (**69.17**) y Escritura (**68.05**), mientras que Matemáticas presentó el promedio más bajo (**66.09**).
* Cursos de preparación: Completar el curso de preparación tiene un impacto positivo notable, elevando el promedio general a **72.67**, en comparación con **65.04** de quienes no lo realizaron (+7.63 puntos).
* Nivel educativo de los padres: Existe una relación directa entre el grado académico de los padres y las calificaciones de los alumnos; los hijos de padres con maestría lideran con un promedio de **73.60**, mientras que los hijos de padres con preparatoria obtuvieron **63.10**.
* Nivel de rendimiento: La mayoría de los estudiantes se ubica en un nivel **Medio (51.7%)**, seguido por nivel **Bajo (28.5%)**, y solo un **19.8%** alcanza un rendimiento **Alto**.
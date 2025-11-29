# EDA_Extrovert_VS_Introvert_behaviour
El presente trabajo trata de analizar un conjunto de datos relacionado con los rasgos de personalidad de personas introvertidas y extrovertidas. Para ello se ha realizado un Análisis Exploratorio de Datos donde se han realizado tareas de:
- Exploración inicial.
- Transformación y liempieza.
- Análisis y visualizaciones.
- Extracción de conclusiones. 


## 📁 Estructura del proyecto
```
/
├── data/                       # Datos originales y transformados
│   ├── data_transformed.csv
│   └── personality_dataset.csv
│
├── img/                        # Imágenes utilizadas
│
├── notebooks/                  # Notebooks de trabajo
│   ├── exploracion.ipynb
│   ├── transformacion.ipynb
│   └── analisis-visualizacion.ipynb
│
├── src/                        # Funciones aplicadas en el proyecto
│   ├── __init__.py
│   ├── visualizaciones.py      # Funciones para análisis y gráficos
│   └── transformaciones.py     # Funciones de limpieza y transformación de datos
|
├── .gitignore                  # Archivo que indica que elementos debe ignorar Git
│
└── README.md                   # Documentación principal del repositorio      

```

## 🧩 Metodología
El proyecto siguió la siguiente frecuencia:
**1. Exploración del dataset.**

    En esta primera parte, el proyecto se centra en obtener las caracteristicas generales que caracterizan este dataset, las cuales son:
    - 8 columnas
    - 2900 filas
    - 8 columnas con nulos
    - 388 filas duplicadas

**2. Transformación y limpieza de datos.**

    A continuación se tomaron decisiones sobre el tratamiento de datos. Las cuales fueron:
    - Normalización de títulos de las columnas.
    - Normalización de variables categóricas.
    - Eliminación de nulos: dejan total de 347..

**3. Análisis y visualización de resultados obtenidos.**

    En esta última parte se dividió el análisis en tres subapartados para llevar a cabo los análisis necesarias en función del númerod e variables a analizar de forma conjunta. Así mismo, en cada uno de ellos se realizaron una serie de preguntas a responder.

        3.1 Análisis univariante
            - ¿Está equilibrado el dataset en base a su columna objetivo?
            - ¿Cómo se distribuyen las variables categóricas?
            - Las variables numéricas, ¿siguen una distribución normal?
            - ¿Existen valores atípicos en el número de amigos?

        3.2 Análisis bivariante
            - Las personas introvertidas ¿tienen pánico escénico?
            - ¿Las personas que más publican en redes sociales son         extrovertios o introvertidos? ¿Existen datos atípicos?
            - ¿Cuantos amigos tienen las personas que se sienten agotadas después de socializar? ¿Y las que no? 
            - ¿Existe alguna relación entre tiempo que pasan a solas y el número de amigos?
            - ¿Cuáles son las variables que explican mejor la variable objetivo? 

        3.3 Análisism multivariante
            - ¿Existe algún perfil multivariante, dentro de las variables numéricas, que defina la personalidad de un individuo?
            - ¿Cómo se relacionan simultaneamente el tiempo a solas, el número de amigos y la frecuencia de publicaciones?

     




## 📊 Conclusiones




## 🧰 Tecnologías utilizadas
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Jupyter Notebook



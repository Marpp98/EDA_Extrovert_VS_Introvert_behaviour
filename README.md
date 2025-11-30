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
El proyecto siguió la siguiente estructura:

### 1. Exploración del dataset.

En esta primera parte, el proyecto se centra en obtener las caracteristicas generales que caracterizan este dataset, las cuales son:
- 8 columnas
- 2900 filas
- 7 columnas con nulos
- 388 filas duplicadas

### 2. Transformación y limpieza de datos.

A continuación se tomaron decisiones sobre el tratamiento de datos. Las cuales fueron:
- Normalización de títulos de las columnas.
- Normalización de variables categóricas.
- Cambio tipo de datos a category para las categóricas e int64 para las numéricas.
- Eliminación de nulos: dejando un total de 2477 filas(85% de datos respecto al original)

### 3. Análisis y visualización de resultados obtenidos.

En esta última parte se dividió el análisis en tres subapartados para llevar a cabo los análisis necesarias en función del número de variables a analizar de forma conjunta. Así mismo, en cada uno de ellos se realizaron una serie de preguntas a responder.

**3.1 Análisis univariante**
- ¿Está equilibrado el dataset en base a su columna objetivo?
    - Sí, presenta el 51% de los datos en extrovertidos y el 49% para introvertidos.
- ¿Cómo se distribuyen las variables categóricas?
    - Se con un 50.1% para las personas sin pánico escénico y un 49.9% para las personas que sí lo tienen. Los mismos resultados presenta *drained_after_socializing* para las personas sin agotamiento y con agotamiento respectivamente.
- Las variables numéricas, ¿siguen una distribución normal?
    - No, ninguna variable sigue una distribución normal. Algunas  como *time_spent_alone* y *going_outside* presentan bimodalidad, lo que indica la existencia de subgrupos. Otras como *social_event_attendance*, *friends_circle_size* o *post_frecuency* muestran distribuciones sesgadas a la derecha.

**3.2 Análisis bivariante**
- Las personas introvertidas ¿tienen pánico escénico?
    - Sí, el 94% de las personas introvertidas tienen pánico escénico.
- ¿Las personas que más publican en redes sociales son extrovertios o introvertidos? ¿Existen datos atípicos?
    - Por lo general las personas extrovertidas publican más que las introvertidas. Sin embargo existen *outliers* hacia valores altos en las personas introvertidas indicando mayor variabilidad de comportamiento en este grupo.
- ¿Cuantos amigos tienen las personas que se sienten agotadas después de socializar? ¿Y las que no? 
    - Las personas que se sienten agotadas después de socializar tienen de media 3 amigos mientras que los que no tienen 10.
- ¿Existe alguna relación entre tiempo que pasan a solas y el número de amigos?
    - Sí, existe una relación negativa, es decir, a más amigos menos tiempo a solas y viceversa.
- ¿Cuáles son las variables que explican mejor la variable objetivo? 
    - A rasgos generales, todas las variables son capaces de discriminar entre grupos respecto a la personalidad.

**3.3 Análisism multivariante**
- ¿Existe algún perfil multivariante, dentro de las variables numéricas, que defina la personalidad de un individuo?
    - Sí, existen perfiles diferenciados según su tipo de personalidad en todas las variables.
- ¿Cómo se relacionan simultaneamente el tiempo a solas, el número de amigos y la frecuencia de publicaciones?
    - *Time_spent_alone* se correlaciona negativamente con *friends_circle_size* y *post_frecuency*, sin embargo estas dos lo hacen de forma positiva entre ellas.
     
## 📊 Conclusiones
El análisis indica que el dataset está balanceado respecto a la columna *personality*. Existen variables numéricas discretas y categóricas que permiten diferenciar perfiles distintos para los grupos de personalidad basándose en patrones multivariantes y los valores medios obtenidos  por grupos.
También se muestra la existencia de variables fuertemente correlacionadas entre ellas.

## 🧰 Tecnologías utilizadas
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Jupyter Notebook



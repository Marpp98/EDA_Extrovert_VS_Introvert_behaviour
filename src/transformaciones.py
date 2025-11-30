import pandas as pd
import numpy as np


def clasificador_variables(df,target):
    '''Función que clasifica las variables en numéricas, categóricas y la columna objetivo:
    df: dataframe del que queremos clasificar las columnas
    target: columna objetivo
    '''
    numericas = []
    categoricas = []
    for i in df.columns:
        if i == target:
            target = i    
        elif (df[i].dtype in ['int64', 'float64']) and (i!= target ):
            numericas.append(i)  
        elif (i not in numericas) and (i != target):
            categoricas.append(i)
            
    return target,numericas, categoricas


def contar_valores_categoricos(df,columnas):
    '''Función que realiza un conteo de los valores únicos de las variables categóricas incluyendo los nulos:
    df: dataframe del que queremos contar los valores únicos de las columnas
    columnas: lista de columnas
    '''
    for i in columnas:
        print(f'Columna {i}:')
        print(df[i].value_counts(dropna = False))
        print('\n')


def normalizar_valores_categoricos (df,columnas):
    '''Función para normalizar los valores de las columnas categóricas. 
    Elimina los posibles espacios que existan antes y después de cada valor y lo pasa todo a minúscula.

    df: dataframe del que queremos normalizar los valores
    columnas: lista de columnas
    '''
    for i in columnas:
        df[i] = df[i].str.lower().str.strip()
    return df


def cambiar_tipos(df,categoricas,numericas):
    '''Función que cambia los tipos de las columnas que representan categorías por category 
    e int64 para las variables numericas discretas.

    df: dataframe del que queremos modificar los tipos
    categoricas: columnas categóricas que queremos cambiar el tipo
    numericas: columnas numéricas que queremos cambiar el tipo
    '''
    df[categoricas]= df[categoricas].astype('category')

    for i in numericas:
        df[i] = pd.to_numeric(df[i], errors = 'coerce').astype('Int64')

    return df


def contar_nulos(df,columnas):
    for i in columnas:
        nulos = df[i].isna().sum()
        print(f'Valores nulos de {i} = {nulos}')


def comparativa_media_mediana_moda(df,columnas,target):
    '''Función que permite obtener la media, la media y la moda agrupada por la columna de preferencia.
    df: dataframe del que queremos obtener los valoes estadísticos agrupados.
    columnas: lista de columnas.
    target: columna mediante la cual se hará la agrupación
    '''

    for i in columnas:
        print(f'Media de {i} según {target}:')
        print(df.groupby(target)[i].mean().round())
        print('\n')

        print(f'Mediana de {i} según {target}:')
        print(df.groupby(target)[i].agg(lambda x: x.median()))
        print('\n')
        
        print(f'Moda de {i} según {target}:')
        print(df.groupby(target)[i].agg(lambda x: x.mode()))
        print('\n---------------------------------------------------------\n')

def imputar_mediana_grupos(df,columnas,target):
    for i in columnas:
        df[i] = df.groupby(target)[i].transform(lambda x:x.fillna(x.median()))
    return df


print('Funciones ejecutadas correctamente')
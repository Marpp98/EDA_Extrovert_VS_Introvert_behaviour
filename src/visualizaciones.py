import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind, chi2_contingency

def pintar_grafico_barras_uni(df,columnas):
    for i in columnas:
        plt.figure(figsize=(6,4))
        sns.countplot(data=df, x=i)
        plt.title(f'Distribución de {i}')
        plt.show()

def pintar_distrib_num_uni(df,columnas):
    for i in columnas:
        plt.figure(figsize=(6,4))
        sns.histplot(df[i], bins=8, kde=True)
        plt.title(f'Distribución de {i}')
        plt.xlabel(i)
        plt.show()

def grafico_barras_categoricas_target(df,categoricas,target):
    for i in categoricas:
        plt.figure(figsize=(7,5))
        sns.countplot(data=df, x=target, hue=i)
        plt.title(f'Distribución de {target} según {i}')
        plt.show()

def dibujar_boxplot(df,x,y):
    plt.figure(figsize=(6,4))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f'{y} según {x}')
    plt.xlabel(x)
    plt.ylabel(f'Frecuencia de {y}')
    plt.show()

def obtener_p_value (df,target,valor1,valor2,columnas):
    for i in columnas:
        target_1 = df[df[target]==valor1][i]
        target_2 = df[df[target]==valor2][i]
        t, p = ttest_ind(target_1, target_2, nan_policy="omit")

        print(f'P-value de {i} = {p}')

def dibujar_boxplot(df,target,columnas):
    for i in columnas:
        plt.figure(figsize=(6,4))
        sns.boxplot(data=df, x=target, y=i)
        plt.title(f'{i} según {target}')
        plt.xlabel(target)
        plt.ylabel(f'Frecuencia de {i}')
        plt.show()

def obtener_p_value (df,target,valor1,valor2,columnas):
    for i in columnas:
        target_1 = df[df[target]==valor1][i]
        target_2 = df[df[target]==valor2][i]
        t, p = ttest_ind(target_1, target_2, nan_policy="omit")

        print(f'P-value de {i} = {p}')


def calculo_tabla_contingencia_chi2(df,target,columnas):
    for i in columnas:    
        tabla_contingencia = pd.crosstab(df[target], df[i])
        chi2, p_value, d, e = chi2_contingency(tabla_contingencia)

        print (tabla_contingencia)
        print(f'\nP-value de {i} = {p_value}')
        print (f'--------------------------')
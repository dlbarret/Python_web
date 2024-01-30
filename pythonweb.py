# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:37:49 2024

@author: LENOVO
"""

import numpy as np
from scipy.stats import norm
import pandas as pd
from datetime import datetime, date, timedelta

import os
from scipy import stats

#os.chdir("D:/4to_Semestre/Series de Tiempo/Proyecto")
#cwd=os.getcwd()   # asigna a cwd el directorio de trabajo


def encontrar_pares(lista, objetivo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                pares.append((lista[i], lista[j]))
    return pares

# Ejemplo de uso
lista_numeros = [1, 9, 5, 0, 20,-4,12,16,7]
valor_objetivo = 12
pares_encontrados = encontrar_pares(lista_numeros, valor_objetivo)
print(pares_encontrados)
 
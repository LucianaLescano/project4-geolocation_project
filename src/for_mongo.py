# Funciones para notebook mongo
# -------------

import pandas as pd
import numpy as np

def only_sao_paulo(two):
    ''' Función que devuelve solo las empresas que están en Sao Paulo y que 
        tienen latitud y longitud diferentes a None.
        input = nada
        ouput = lista
    '''
    posibilities = ['Sao Paulo', 'SÃ£o Paulo', 'São Paulo', 'Salo Paulo', 'SÃ¢o Paulo']
    new_two_list = []
    for t in two:
        new_two = {}
        for o in t['offices']:
            if (o['city'] in posibilities) and (o['latitude'] != None or o['longitude'] != None):
                new_two['name'] = t['name']
                new_two['latitude'] = o['latitude']
                new_two['longitude'] = o['longitude']
                new_two_list.append(new_two.copy())
    return new_two_list

# -------------

def droping(data, lst):
    ''' Función que eliminar filas.
        input = dataframe del que se desea eliminar las filas y lista con los indices de las columnas
                a eliminar
        output = dataframe
    '''
    new_data = data.drop(lst).reset_index(drop=True)
    return new_data
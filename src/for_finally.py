# Funciones para notebook final data
# -------------

import pandas as pd
import math

def droping(data, lst):
    ''' Función que eliminar filas.
        input = dataframe del que se desea eliminar las filas y lista con los indices de las columnas
                a eliminar
        output = dataframe final
    '''
    new_data = data.drop(lst).reset_index(drop=True)
    return new_data

# -------------

def adding_type(data, type_):
    '''Función para clasificar diferentes filas de un dataframe.
        input = dataframe, 'etiqueta' de clasificación en forma de lista
        output = dataframe con filas clasificadas
    '''
    lst = list(type_ * len(data))
    data['type'] = lst
    return data

# -------------

def concating(lst):
    '''Función que concatena multiples dataframes.
        input = lista de dataframes
        output = dataframe
    '''
    new_data = pd.concat(lst, ignore_index=True)
    return new_data

# -------------

def haversine(coord1, coord2):
    '''Obtenida de: 
    url = https://janakiev.com/blog/gps-points-distance-python/
    '''
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a)) 

# -------------

def getting_numbers(coord, dict_of_coords):
    '''Función que calcula la distancia entre coordenadas.
        input = coordenadas unicas, diccionario de coordenadas con las que comparar
        output = lista de distancias
    '''
    new_coord_list = []
    new_coord_dict = {}
    for k,v in dict_of_coords.items():
        distance = haversine(coord, v)
        #print(k)
        new_coord_dict['name'] = k
        new_coord_dict['distance'] = distance
        new_coord_list.append(new_coord_dict.copy())
        #print ('Distance to', k, ': ', distance)
    return new_coord_list
  
# -------------

def final_df(list1, list2, list3):
    '''Función que conviertes tres listas en un dataframe.
        input = tres listas
        output = dataframe
    '''
    total = list1 + list2 + list3
    df = pd.DataFrame(total)
    return df
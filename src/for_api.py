# Funciones para notebook API
# -------------

import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
from functools import reduce
import operator
import numpy as np

def get_things(latitude, longitude, query):
    ''' Función que me devuelve un dataframe con de las coincidencias según la query.
        input = latitud, longitud y query
        output = dataframe con nombre, latitud y longitud
    '''

    # Url definida
    url ='https://api.foursquare.com/v2/venues/explore'

    # Tokens guardados en variable de entorno
    token1 = os.getenv("token1")
    token2 = os.getenv("token2")

    lst = []
    parameters = { "client_id" : token1,
          "client_secret" : token2,
          "v" : "20180323",
          "ll": f"{latitude},{longitude}",
          "query": query,
          "limit" : 1
        }
    #print(latitude, longitude)
    resp = requests.get (url = url, params = parameters)
    data = json.loads(resp.text)
    decoding_data = data.get("response")
    #print(decoding_data)
    decoded = decoding_data.get("groups")[0]
    things = decoded.get("items")
    #print(things)

    nombre = ["venue", "name"]
    latitud = ["venue", "location", "lat"]
    longitud = ["venue", "location", "lng"]

    def getFromDict(diccionario,mapa):
        return reduce(operator.getitem,mapa,diccionario)

    for diccionario in things:
        #if diccionario != {}:
        paralista = {}
        paralista["name"] = getFromDict(diccionario,nombre)
        paralista["latitud"] = getFromDict(diccionario,latitud)
        paralista["longitud"] = getFromDict(diccionario,longitud)
        lst.append(paralista)

    df = pd.DataFrame(lst)
    return df

# -------------

def concating(lst):
    '''Función que concatena multiples dataframes.
        input = lista de dataframes
        output = dataframe
    '''
    new_data = pd.concat(lst, ignore_index=True)
    return new_data
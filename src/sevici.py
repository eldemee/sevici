import csv
import math 
import folium
from collections import namedtuple


Coordenadas = namedtuple("Coordenadas",["latitud","longitud"])
Estacion = namedtuple("Estacion", ["nombre", "bornetas", "bornetas_vacias", "bicis_disponibles", "coordenadas"])

def lee_estaciones(fichero):
    info = []
    with open(fichero, encoding="UTF-8") as file:
        df = csv.reader(file)
        next(df)
        datos = [dato for dato  in df]
        for fila in datos:
            n = Estacion(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), Coordenadas(float(fila[4]), float(fila[5])))
            info.append(n)
        return(info)
    
def estaciones_bicis_libres(estaciones, k=5):
    verificadas = [(valores.bicis_disponibles, valores.nombre) for valores in estaciones]
    return verificadas

def calcula_distancia(coordenadas1, coordenadas2):
    distancia = math.sqrt((coordenadas1.latitud-coordenadas2.latitud)**2 + (coordenadas1.longitud-coordenadas2.longitud)**2)
    return distancia

def estaciones_cercanas(estaciones, coordenadas, k=5):
    print([valor.coordenadas for valor in estaciones])
    coordenadas_estaciones = [valor.coordenadas for valor in estaciones]
    distancias = calcula_distancia(coordenadas, coordenadas_estaciones)
    return distancias

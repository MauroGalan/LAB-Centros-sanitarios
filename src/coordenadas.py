import math
from collections import namedtuple
Coordenadas= namedtuple("Coordenadas","latitud,longitud")

def calcular_distancia(coor1,coor2): 
    """
    Recibe dos coordenadas de tipo Coordenadas(float, float) y devuelve un float 
    que representa la distancia euclídea entre esas dos coordenadas.
    """
    return (math.sqrt((coor1.latitud-coor2.latitud)**2+(coor1.longitud - coor2.longitud)**2))

def calcular_media_coordenadas(l_coor):
    """
    Recibe una lista de Coordenadas(float, float) y devuelve una tupla de tipo Coordenadas(float, float) 
    cuya latitud es la media de las latitudes de la lista y cuya longitud es la media de las longitudes de la lista.
    """
    latitud_t= 0
    longitud_t= 0
    for coor in l_coor:
        latitud_t += coor.latitud
        longitud_t += coor.longitud
    return Coordenadas(latitud_t/(len(l_coor)),longitud_t/len(l_coor))
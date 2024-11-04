import csv
from coordenadas import Coordenadas, calcular_distancia, calcular_media_coordenadas
from mapas import *
from collections import namedtuple
CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def leer_centros(ruta): 
    """
    Recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de tipo 
    CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool) conteniendo todos los datos almacenados 
    en el fichero.
    """
    with open (ruta, encoding="utf-8") as f:
        lector = csv.reader(f,delimiter=";")
        next(lector)
        centros = []
        for nombre,localidad,latitud,longitud,estado,num_camas,acceso_discapacitados,tiene_uci in lector:
            coordenadas = Coordenadas(float(latitud),float(longitud))
            num_camas = int(num_camas)
            if acceso_discapacitados.strip() == "true": acceso = True
            else: acceso = False
            if tiene_uci.strip() == "true": uci = True
            else: uci = False
            centros.append(CentroSanitario(nombre,localidad,coordenadas,estado,num_camas,acceso,uci))
        return centros

def calcular_total_camas_centros_accesibles(centros): 
    """
    Recibe una lista de tuplas de tipo CentroSanitario y produce como salida un entero 
    correspondiente al número total de camas de los centros sanitarios accesibles para discapacitados.
    """
    camas_t = 0
    for centro in centros:
        if centro.acceso_minusvalidos == True:
            camas_t += centro.num_camas
    return camas_t

def obtener_centros_con_uci_cercanos_a(centros, coordenadas,umbral): 
    """
    Recibe una lista de tuplas de tipo CentroSanitario; una tupla de tipo Coordenadas, 
    que representa un punto; y un float, que representa un umbral de distancia. 
    Produce como salida una lista de tuplas (str, str, Coordenadas(float, float)) con el nombre del centro, 
    la localidad y las coordenadas de los centros con uci situados a una distancia 
    de las coordenadas dadas como parámetro menor o igual que el umbral dado. 
    Observe la Figura 3 para entender mejor el resultado de la función.
    """
    centro_u = []
    for centro in centros:
        if calcular_distancia(centro.coordenadas,coordenadas)<=umbral and centro.tiene_uci == True:
            centro_u.append((centro.nombre,centro.localidad,centro.coordenadas))
    return centro_u

def generar_mapa(centros,rutah): 
    """
    recibe una lista de tuplas (str, str, Coordenadas(float, float)) con el nombre, del centro, la localidad y 
    las coordenadas del centro; y una cadena, que representa la ruta de un fichero html, que se generará 
    con los centros geolocalizados.
    """
    mapa = crea_mapa(calcular_media_coordenadas(centros))
    for centro in centros:
        agrega_marcador(mapa, centro[2], "Centro", "rojo")
    guarda_mapa(mapa,rutah)

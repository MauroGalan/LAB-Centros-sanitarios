from centros import leer_centros,calcular_total_camas_centros_accesibles,obtener_centros_con_uci_cercanos_a
from coordenadas import Coordenadas
coord = Coordenadas(36.189308321456515, -5.925475089376914)
if __name__ == "__main__":
    print(f"Diez de los centros son :{leer_centros("data/centrosSanitarios.csv")[:10]}")
    #print(f"Las camas totales son {calcular_total_camas_centros_accesibles(leer_centros("data/centrosSanitarios.csv"))}")
    #print(f"Los centros con uci cercanos a {coord} a un máximo de 0,5 de distancia son: {obtener_centros_con_uci_cercanos_a(leer_centros("data/centrosSanitarios.csv"),coord,0.5)}")
from coordenadas import calcular_distancia, calcular_media_coordenadas,Coordenadas
coor = Coordenadas(10,15)
coor_= Coordenadas(5,30)
coordenas = [coor,coor_]
if __name__ == "__main__":
    print(f"La distancia entre {coor} y {coor_} es {calcular_distancia(coor,coor_)}")
    print(f"La media entre ellas dos es: {calcular_media_coordenadas(coordenas)}")
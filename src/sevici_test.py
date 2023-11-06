from sevici import *

mis_coordenadas = (0,0)

def main():
    lista_estaciones = lee_estaciones("data/estaciones.csv")
    estaciones_bicis_libres(lista_estaciones)
    print(estaciones_cercanas(lista_estaciones,mis_coordenadas))

    return

if __name__ == "__main__":
    main()
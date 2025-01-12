from parsers import*
from compras import*

def test_leer_compras(ruta):
    print("EJERCICIO 1\n")
    print(f"Número de registros leídos: {len(lee_compras(ruta))}\n")
    print(f"Tres primero registros: {lee_compras(ruta)[:3]}\n")
    print(f"Tres últimos registros: {lee_compras(ruta)[-3:]}")

if __name__ == '__main__':
    #compras = lee_compras('data\\compras.csv')
    #print(compras)

    test_leer_compras("data\\compras.csv")
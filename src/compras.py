from parsers import *
from typing import Tuple, List, Dict
from collections import Counter #counter hace un diccionario de cada elemento y pone las veces que se repite
from datetime import *



#APARTADO 2 (1 punto)
def compra_maxima_minima_provincia(lista: List[Compra], provincia:str) -> Tuple[float, float]:
    #res = ()
    importes = [] #creo una lista y cojo el mas caro y el mas barato
    for compra in lista:
        if compra.provincia == provincia or provincia is None:
            importes.append(compra.total_compra)
    #importes = sorted(importes, reverse = True) # o bien se puede hacer return (max(importes), min(importes))
    res = (max(importes), min(importes)) # res = res + (algo, algo, etc...) para añadir elementos a una tupla ⭐⭐⭐
    return res


#APARTADO 3 (1,5 puntos)
def hora_menos_afluencia(lista: List[Compra]) -> Tuple[int, int]: #haces una lista con todas las horas de llegada, y la que menos se repita esa es
    horas =  []
    for compra in lista:
        horas.append(compra.fecha_llegada.hour) #para saber la hora de llegada
    conteo_horas = Counter(horas)
    hora_menos_frecuente = min(conteo_horas, key=conteo_horas.get)  # Encontrar la hora con menor frecuencia, el get vale para que mire el valor en lugar de la clave
    return (hora_menos_frecuente, conteo_horas[hora_menos_frecuente])


#APARTADO 4 (1,5 puntos) (medio difícil la última parte)
def supermercados_mas_facturacion(lista: List[Compra], numero = 3) -> List[Tuple[int, Tuple[str, float]]]:
    res: Dict[str, float] = {}
    resf = []
    for compra in lista:
        res[compra.supermercado] = res.get(compra.supermercado, 0) + compra.total_compra # el get() funciona para obtener la clave del dicc y el 0 es para darle valor 0 en caso de que no tenga nada
    ranking = sorted(res.items(), key = lambda x: x[1], reverse = True)
    for i, (supermercado, facturacion) in enumerate(ranking[:numero]):
        resf.append((i + 1, (supermercado, facturacion)))
    return resf


#APARTADO 5 (2 puntos)
from typing import List, Tuple

def clientes_itinerantes(lista: List['Compra'], numero = 2) -> List[Tuple[str, List[str]]]:
    res = {}  # diccionario para almacenar el dni y sus provincias
    for compra in lista:
        if compra.dni not in res:
            res[compra.dni] = set()  # Usamos un set para evitar dnis duplicados
        res[compra.dni].add(compra.provincia)
    
    clientes_filtrados = []
    for dni, provincias in res.items():
        if len(provincias) > numero:
            clientes_filtrados.append((dni, sorted(list(provincias))))
    return clientes_filtrados


#APARTADO 6 (2 puntos) (difícil pero no tanto)
def dias_estrella(lista: List[Compra], supermercado: str, provincia:str) -> List[datetime]:
    compras_filtradas = []
    for compra in lista:
        if compra.supermercado == supermercado and compra.provincia == provincia:
            compras_filtradas.append(compra)

    compras_ordenadas = sorted(compras_filtradas, key=lambda x: x.fecha_llegada)
    fechas_estrella = []
    for i in range(1, len(compras_ordenadas) - 1):  # no analizamos el primer ni el último día
        compra_anterior = compras_ordenadas[i - 1]
        compra_actual = compras_ordenadas[i]
        compra_siguiente = compras_ordenadas[i + 1]
        if compra_actual.total_compra > compra_anterior.total_compra and compra_actual.total_compra > compra_siguiente.total_compra:
            fechas_estrella.append(compra_actual.fecha_llegada.strftime('%d/%m/%Y')) # para escribirlo (para convertir un objeto datetime a un str), en lugar de strptime que es para 'analizarlo' (para convertir un str a un objeto datetime)
    
    return fechas_estrella


if __name__ == '__main__':
    ruta = "data/compras.csv"
    compras = lee_compras(ruta)
    #print(compras)

    #print(f"{compra_maxima_minima_provincia(compras, None)}")

    #print(f"{hora_menos_afluencia(compras)}")

    #print(f"{supermercados_mas_facturacion(compras, 3)}")

    #print(f"{clientes_itinerantes(compras, 7)}")

    print(f"{dias_estrella(compras, "Lidl", "Sevilla")}")


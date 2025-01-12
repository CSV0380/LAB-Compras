#PARCERITA DIME QUE HUBOOOOO 🧑‍🎤🧑‍🎤🧑‍🎤🧑‍🎤🧑‍🎤🧑‍🎤🧑‍🎤🧑‍🎤
from typing import List, NamedTuple
import csv
from datetime import datetime

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )


#APARTADO 1 (1 punto)
def lee_compras(ruta: str) -> List[Compra]:
    compras = []
    with open(ruta, mode = 'r', encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            dni = str(dni)
            supermercado = str(supermercado)
            provincia = str(provincia)
            fecha_llegada = datetime.strptime(fecha_llegada, "%d/%m/%Y %H:%M")
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y %H:%M")
            total_compra = float(total_compra)
            compras.append(Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra))
        return compras
    





#if __name__ == '__main__':
    
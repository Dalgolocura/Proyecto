"""
Parte 1 Proyecto DALGO 2022-1
Autores:
    Boris Reyes     - 202014743
    Daniel Aguilera - 202010592
    Juliana Galeano - 202012128
    William Mendez  - 202012662
"""

import sys
from timeit import default_timer as timer
from tracemalloc import start

def lectura():
    nMatriz = int(sys.stdin.readline())

    while nMatriz != 0:
        datos = sys.stdin.readline().split(" ")
        nPisos = int(datos[0])
        nHabitaciones = int(datos[1])
        nPortales = int(datos[2])
        gastoEnergia = [int(x) for x in sys.stdin.readline().split(" ")]
        portales = {}
        entradas = []
        salidas = []

        for i in range(nPortales):
            datos = sys.stdin.readline().split(" ")
            portales[(int(datos[0]), int(datos[1]))] = (int(datos[2]), int(datos[3]))
            entradas.append((int(datos[0]), int(datos[1])))
            salidas.append((int(datos[2]), int(datos[3])))

        # print(calcularMinEnergia(nPisos, nHabitaciones, nPortales, gastoEnergia, portales))
        # print(nPisos,nHabitaciones,nPortales)
        # print(gastoEnergia)
        # print(portales)

        nMatriz -= 1

def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, nPortales, gastoEnergia, portales):
    memoria = [[1000001 for i in range(nHabitaciones)] for j in range(nPisos)]
    visitados = []
    porVisitar = []


    pass

start = timer()
lectura()
elapsed_time = timer() - start
print("Tiempo: %.10f segundos." % elapsed_time)

# def dijkstra():
#     if (i,j) in portales.keys()

# comando: python ProblemaP1.py <2.in> salida.out

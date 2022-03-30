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
from queue import PriorityQueue as PQ

def lectura():

    file = open("1.in", "r")

    nCasos = int(file.readline())
    # nCasos = int(sys.stdin.readline())

    while nCasos != 0:
        datos = file.readline().split(" ")
        # datos = sys.stdin.readline().split(" ")
        nPisos = int(datos[0])
        nHabitaciones = int(datos[1])
        nPortales = int(datos[2])
        gastoEnergia = [int(x) for x in file.readline().split(" ")]
        # gastoEnergia = [int(x) for x in sys.stdin.readline().split(" ")]
        portales = {}

        for i in range(nPortales):
            datos = file.readline().split(" ")
            # datos = sys.stdin.readline().split(" ")
            portales[(int(datos[0])-1, int(datos[1])-1)] = (int(datos[2])-1, int(datos[3])-1)

        entradas = list(portales.keys())
        entradas.sort()


        start = timer() # TODO: Quitar esto
        print(calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales, entradas))
        elapsed_time = timer() - start # TODO: Quitar esto
        print("Caso:", 1001 - nCasos,"tamaño de la torre",nPisos,"x",nHabitaciones, "Tiempo:", elapsed_time) # TODO: Quitar esto
        nCasos -= 1

def binarySearch(array, x, low, high):
    high -= 1
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales, entradas):
    inicio = (0,0)
    memoria = {}
    memoria[inicio] = 0
    visitados = []
    # porVisitar = [inicio]

    j = 0

    pq = PQ()
    pq.put((inicio,0))

    while not pq.empty():
        (actual, dist) = pq.get()
        # print(actual, dist)
        visitados.append(actual)

        vecinos = []
        if actual[1] > 0 and (actual[0], actual[1] - 1) not in visitados:
            vecinos.append((actual[0], actual[1] - 1))
        if actual[1] < nHabitaciones - 1 and (actual[0], actual[1] + 1) not in visitados:
            vecinos.append((actual[0], actual[1] + 1))
        index = binarySearch(entradas, actual, 0, len(entradas))
        if index != -1 and portales[actual] not in visitados:
            vecinos.append(portales[actual])

        for vecino in vecinos:
            if vecino[0] > actual[0]:
                nuevoGasto = memoria[actual]
            else:
                nuevoGasto = gastoEnergia[vecino[0]] + memoria[actual]

            nuevo = vecino not in memoria.keys()
            if nuevo:
                memoria[vecino] = nuevoGasto
            else:
                viejoGasto = memoria[vecino]
                if nuevoGasto < viejoGasto:
                    pq.put((vecino, nuevoGasto))
                    memoria[vecino] = nuevoGasto
            if vecino not in visitados:
                pq.put((vecino, nuevoGasto))
                # porVisitar.append(vecino)

        j += 1
        if j % 10000 == 0:
            print(j, "elementos visitados")

    goal = (nPisos - 1, nHabitaciones - 1)

    if goal not in visitados:
        return "NO EXISTE"
    else:
        return memoria[(nPisos - 1,nHabitaciones - 1)]



start = timer()
lectura()
elapsed_time = timer() - start
print("Tiempo total: %.10f segundos." % elapsed_time)


# comando: python ProblemaP1.py <2.in> salida.out

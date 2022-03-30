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

    file = open("Proyecto/P1_casesFP.in", "r")

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
    # memoria = [[1000001 for i in range(nHabitaciones)] for j in range(nPisos)]
    memoria = {}
    memoria[(0,0)] = 0
    visitados = []
    porVisitar = [(0,0)]

    j = 0

    while len(porVisitar) > 0:

        actual = porVisitar.pop(0)
        vecinos = []
        if actual[1] > 0 and (actual[0], actual[1] - 1) not in visitados:
            vecinos.append((actual[0], actual[1] - 1))
        if actual[1] < nHabitaciones - 1 and (actual[0], actual[1] + 1) not in visitados:
            vecinos.append((actual[0], actual[1] + 1))
        index = binarySearch(entradas, actual, 0, len(entradas))
        if index != -1 and portales[actual] not in visitados:
            vecinos.append(portales[actual])

        for i in vecinos:
            if i[0] > actual[0]:
                nuevoGasto = memoria[actual]
            else:
                nuevoGasto = gastoEnergia[i[0]] + memoria[actual]

            nuevo = i not in memoria.keys()
            if nuevo:
                memoria[i] = nuevoGasto
            else:
                viejoGasto = memoria[i]
                if nuevoGasto < viejoGasto:
                    memoria[i] = nuevoGasto
            if i not in visitados and i not in porVisitar:
                porVisitar.append(i)
        visitados.append(actual)

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

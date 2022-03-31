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
# from queue import PriorityQueue as PQ

def lectura():

    # file = open("1.in", "r")
    # file = open("2.in", "r")
    # file = open("Proyecto/P1_casesFP.in", "r")

    # nCasos = int(file.readline())
    nCasos = int(sys.stdin.readline())

    while nCasos != 0:
        # datos = file.readline().split(" ")
        datos = sys.stdin.readline().split(" ")
        nPisos = int(datos[0])
        nHabitaciones = int(datos[1])
        nPortales = int(datos[2])
        # gastoEnergia = [int(x) for x in file.readline().split(" ")]
        gastoEnergia = [int(x) for x in sys.stdin.readline().split(" ")]
        portales = {}
        pisosNoVisitados = {x: 0 for x in range(1,nPisos)}

        for i in range(nPortales):
            # datos = file.readline().split(" ")
            datos = sys.stdin.readline().split(" ")
            portales[(int(datos[0])-1, int(datos[1])-1)] = (int(datos[2])-1, int(datos[3])-1)
            if inDict(pisosNoVisitados, int(datos[2])-1):
                pisosNoVisitados.pop(int(datos[2])-1)

        entradas = list(portales.keys())

        # start = timer() # TODO: Quitar esto
        if inDict(pisosNoVisitados, nPisos - 1):
            print("NO EXISTE")
        else:
            for i in entradas:
                if inDict(pisosNoVisitados, i[0]):
                    portales.pop(i)
            print(calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales))

        # elapsed_time = timer() - start # TODO: Quitar esto
        # print("Caso:", 1001 - nCasos,"tamaño de la torre",nPisos,"x",nHabitaciones, "Tiempo:", elapsed_time) # TODO: Quitar esto
        nCasos -= 1

        if nCasos  == 101:
            file = open("test.in", "w")
            file.write("1\n")
            file.write(str(nPisos) + " " + str(nHabitaciones) + " " + str(nPortales) + "\n")
            file.write("\n")




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

def inDict(dict, key) -> bool:
    try:
        dict[key]
        return True
    except KeyError:
        return False


def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales):
    inicio = (0,0)
    memoria = {}
    memoria[inicio] = 0
    visitados = {}
    porVisitar = {inicio: 0}

    # j = 0

    # pq = PQ()
    # pq.put((inicio,0))

    # while not pq.empty():
    while len(porVisitar) > 0:
        # (actual, dist) = pq.get()
        actual = list(porVisitar.keys())[0]
        porVisitar.pop(list(porVisitar.keys())[0])
        # porVisitar.pop(actual)

        # print(actual, dist)
        visitados[actual] = 0

        vecinos = []
        if actual[1] > 0 and not inDict(visitados, (actual[0], actual[1]-1)):
            vecinos.append((actual[0], actual[1] - 1))

        if actual[1] < nHabitaciones and not inDict(visitados, (actual[0], actual[1]+1)):
            vecinos.append((actual[0], actual[1] + 1))

        # if index != -1 and not inDict(visitados, portales[actual]):
        if inDict(portales, actual) and not inDict(visitados, portales[actual]):
            vecinos.append(portales[actual])

        for vecino in vecinos:
            if vecino[0] > actual[0]:
                nuevoGasto = memoria[actual]
            else:
                nuevoGasto = gastoEnergia[vecino[0]] + memoria[actual]

            nuevo = not inDict(memoria, vecino)
            if nuevo:
                memoria[vecino] = nuevoGasto

            viejoGasto = memoria[vecino]
            if nuevoGasto < viejoGasto:
                memoria[vecino] = nuevoGasto
            if not inDict(visitados, vecino) and vecino not in porVisitar:
                porVisitar[vecino] = 0
                # porVisitar.append(vecino)

        # j += 1
        # if j % 10000 == 0:
            # print(j, "elementos visitados")

    goal = (nPisos - 1, nHabitaciones - 1)

    # print(j, "elementos visitados")
    if not inDict(visitados, goal):
        return "NO EXISTE"
    else:
        return memoria[(nPisos - 1,nHabitaciones - 1)]



start = timer()
lectura()
elapsed_time = timer() - start
print("Tiempo total: %.10f segundos." % elapsed_time)


# comando: python ProblemaP1.py <2.in> salida.out

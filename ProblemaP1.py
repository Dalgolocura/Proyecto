"""
Parte 1 Proyecto DALGO 2022-1
Autores:
    Boris Reyes     - 202014743
    Daniel Aguilera - 202010592
    Juliana Galeano - 202012128
    William Mendez  - 202012662
"""

import sys
from pydoc import describe
from timeit import default_timer as timer
from tracemalloc import start

def lectura():

    # file = open("1.in", "r")
    # file = open("Proyecto/2.in", "r")
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

        for i in range(nPortales):
            # datos = file.readline().split(" ")
            datos = sys.stdin.readline().split(" ")
            portales[(int(datos[0])-1, int(datos[1])-1)] = (int(datos[2])-1, int(datos[3])-1)

        # start = timer() # TODO: Quitar esto
        print(calcularMinEnergiaRecorrido(nPisos, nHabitaciones, gastoEnergia, portales))
        # print(calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales, entradas))
        # elapsed_time = timer() - start # TODO: Quitar esto
        # print("Caso:", 1001 - nCasos,"tamaño de la torre",nPisos,"x",nHabitaciones, "Tiempo:", elapsed_time) # TODO: Quitar esto
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

def inDict(dict, key) -> bool:
    try:
        dict[key]
        return True
    except KeyError:
        return False

def calcularMinEnergiaRecorrido(nPisos, nHabitaciones, gastoEnergia, portales):
    memoria = {(0,0): 0}

    for piso in range(nPisos):
        for nHabitacion in range(nHabitaciones):
            vecinoIzq = None
            vecinoDer = None
            valorActual = None

            if inDict(memoria, (piso, nHabitacion)):
                valorActual = memoria[(piso, nHabitacion)]
            if inDict(memoria, (piso, nHabitacion-1)):
                vecinoIzq = memoria[(piso, nHabitacion-1)]
            if inDict(memoria, (piso, nHabitacion+1)):
                vecinoDer = memoria[(piso, nHabitacion+1)]

            if valorActual is not None:
                if vecinoIzq is not None:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion)] = min(vecinoIzq + gastoEnergia[piso], valorActual, vecinoDer + gastoEnergia[piso])
                    else:
                        memoria[(piso, nHabitacion)] = min(vecinoIzq + gastoEnergia[piso], valorActual)
                else:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion)] = min(vecinoDer + gastoEnergia[piso], valorActual)
                    else:
                        memoria[(piso, nHabitacion)] = valorActual
            else:
                if vecinoIzq is not None:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion)] = min(vecinoIzq + gastoEnergia[piso], vecinoDer + gastoEnergia[piso])
                    else:
                        memoria[(piso, nHabitacion)] = vecinoIzq + gastoEnergia[piso]
                else:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion)] = vecinoDer + gastoEnergia[piso]
                    else:
                        memoria[(piso, nHabitacion)] = None

            if inDict(portales, (piso, nHabitacion)):
                memoria[portales[(piso, nHabitacion)]] = memoria[(piso, nHabitacion)]

            nHabitacion2 = nHabitaciones - nHabitacion - 1
            vecinoIzq = None
            vecinoDer = None
            valorActual = None

            if inDict(memoria, (piso, nHabitacion2)):
                valorActual = memoria[(piso, nHabitacion2)]
            if inDict(memoria, (piso, nHabitacion2-1)):
                vecinoIzq = memoria[(piso, nHabitacion2-1)]
            if inDict(memoria, (piso, nHabitacion2+1)):
                vecinoDer = memoria[(piso, nHabitacion2+1)]

            if valorActual is not None:
                if vecinoIzq is not None:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion2)] = min(vecinoIzq + gastoEnergia[piso], valorActual, vecinoDer + gastoEnergia[piso])
                    else:
                        memoria[(piso, nHabitacion2)] = min(vecinoIzq + gastoEnergia[piso], valorActual)
                else:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion2)] = min(vecinoDer + gastoEnergia[piso], valorActual)
                    else:
                        memoria[(piso, nHabitacion2)] = valorActual
            else:
                if vecinoIzq is not None:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion2)] = min(vecinoIzq + gastoEnergia[piso], vecinoDer + gastoEnergia[piso])
                    else:
                        memoria[(piso, nHabitacion2)] = vecinoIzq + gastoEnergia[piso]
                else:
                    if vecinoDer is not None:
                        memoria[(piso, nHabitacion2)] = vecinoDer + gastoEnergia[piso]
                    else:
                        memoria[(piso, nHabitacion2)] = None

            if inDict(portales, (piso, nHabitacion2)):
                memoria[portales[(piso, nHabitacion2)]] = memoria[(piso, nHabitacion2)]
    goal = (nPisos - 1, nHabitaciones - 1)
    if inDict(memoria, goal):
        if memoria[goal] is not None:
            return memoria[goal]
        else:
            return "NO EXISTE"
    else:
        return "NO EXISTE"



def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales, entradas):
    inicio = (0,0)
    memoria = {}
    memoria[inicio] = 0
    visitados = {}
    porVisitar = [inicio]

    # j = 0

    # pq = PQ()
    # pq.put((inicio,0))

    # while not pq.empty():
    while len(porVisitar) > 0:
        # (actual, dist) = pq.get()
        actual = porVisitar.pop(0)
        # porVisitar.pop(actual)

        # print(actual, dist)
        visitados[actual] = 0

        vecinos = []
        if actual[1] > 0 and not inDict(visitados, (actual[0], actual[1]-1)):
            vecinos.append((actual[0], actual[1] - 1))

        if actual[1] < nHabitaciones and not inDict(visitados, (actual[0], actual[1]+1)):
            vecinos.append((actual[0], actual[1] + 1))

        index = binarySearch(entradas, actual, 0, len(entradas))

        if index != -1 and not inDict(visitados, portales[actual]):
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
                porVisitar.append(vecino)

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

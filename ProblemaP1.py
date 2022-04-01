"""
Parte 1 Proyecto DALGO 2022-1
Autores:
    Boris Reyes     - 202014743
    Daniel Aguilera - 202010592
    Juliana Galeano - 202012128
    William Mendez  - 202012662
"""

from sys import stdin
from timeit import default_timer as timer
#from queue import PriorityQueue as PQ
import heapq as boris

def lectura():

    # file = open("1.in", "r")
    # file = open("2.in", "r")
    # file = open("Proyecto/P1_casesFP.in", "r")

    # nCasos = int(file.readline())
    nCasos = int(stdin.readline())

    while nCasos != 0:
        # datos = file.readline().split(" ")
        datos = stdin.readline().split(" ")
        nPisos = int(datos[0])
        nHabitaciones = int(datos[1])
        nPortales = int(datos[2])
        # gastoEnergia = [int(x) for x in file.readline().split(" ")]
        gastoEnergia = [int(x) for x in stdin.readline().split(" ")]
        portales = {}
        pisosNoVisitados = {x: 0 for x in range(1,nPisos)}

        for i in range(nPortales):
            # datos = file.readline().split(" ")
            datos = stdin.readline().split(" ")
            portales[(int(datos[0])-1, int(datos[1])-1)] = (int(datos[2])-1, int(datos[3])-1)
            # if inDict(pisosNoVisitados, int(datos[2])-1):
            if pisosNoVisitados.get(int(datos[2])-1, -1) != -1:
                pisosNoVisitados.pop(int(datos[2])-1)

        entradas = list(portales.keys())

        # start = timer() # TODO: Quitar esto
        # if inDict(pisosNoVisitados, nPisos - 1):
        if pisosNoVisitados.get(nPisos - 1, -1) != -1:
            print("NO EXISTE")
        else:
            for i in entradas:
                # if inDict(pisosNoVisitados, i[0]):
                if pisosNoVisitados.get(i[0], -1) != -1:
                    portales.pop(i)
            print(calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales))

        # elapsed_time = timer() - start # TODO: Quitar esto
        # print("Caso:", 1001 - nCasos,"tamaño de la torre",nPisos,"x",nHabitaciones, "Tiempo:", elapsed_time) # TODO: Quitar esto
        nCasos -= 1

def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales):
    inicio = (0,0)
    memoria = {}
    memoria[inicio] = 0
    visitados = {}
    porVisitar = {inicio: 0}

    # j = 0
    listap=[]
    boris.heappush(listap, (0,inicio))
    #pq = PQ()
    #pq.put((0,inicio))
    
    while len(listap) != 0:
    #while not pq.empty():
        (dist, actual) = boris.heappop(listap)
        porVisitar.pop(actual)

        # print(actual, dist)
        visitados[actual] = 0

        vecinos = []
        # if actual[1] > 0 and not inDict(visitados, (actual[0], actual[1]-1)):
        if actual[1] > 0 and visitados.get((actual[0], actual[1]-1), -1) == -1:
            vecinos.append((actual[0], actual[1] - 1))

        # if actual[1] < nHabitaciones and not inDict(visitados, (actual[0], actual[1]+1)):
        if actual[1] < nHabitaciones and visitados.get((actual[0], actual[1]+1), -1) == -1:
            vecinos.append((actual[0], actual[1] + 1))

        # if inDict(portales, actual) and not inDict(visitados, portales[actual]):
        if portales.get(actual, -1) != -1 and visitados.get(portales[actual], -1) == -1:
            vecinos.append(portales[actual])

        for vecino in vecinos:
            if vecino[0] > actual[0]:
                nuevoGasto = memoria[actual]
            else:
                nuevoGasto = gastoEnergia[vecino[0]] + memoria[actual]

            # if not inDict(memoria, vecino):
            if memoria.get(vecino, -1) == -1:
                memoria[vecino] = nuevoGasto

            viejoGasto = memoria[vecino]
            if nuevoGasto < viejoGasto:
                memoria[vecino] = nuevoGasto
            # if not inDict(visitados, vecino) and not inDict(porVisitar, vecino):
            if visitados.get(vecino, -1) == -1 and porVisitar.get(vecino, -1) == -1:
                boris.heappush(listap, (nuevoGasto, vecino))
                #pq.put((nuevoGasto, vecino))
                porVisitar[vecino] = 0

        # j += 1
        # if j % 10000 == 0:
            # print(j, "elementos visitados")

    goal = (nPisos - 1, nHabitaciones - 1)

    # print(j, "elementos visitados")
    # if not inDict(visitados, goal):
    if visitados.get(goal, -1) == -1:
        return "NO EXISTE"
    else:
        return memoria[(nPisos - 1,nHabitaciones - 1)]



start = timer()
lectura()
elapsed_time = timer() - start
print("Time: %.10f segundos." % elapsed_time)


# comando: python ProblemaP1.py <P1_casesFP.in> salida.out

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
import heapq as hq

def lectura():

    nCasos = int(stdin.readline())

    while nCasos != 0:
        datos = stdin.readline().split(" ")
        nPisos, nHabitaciones, nPortales = int(datos[0]), int(datos[1]), int(datos[2])
        gastoEnergia = [int(x) for x in stdin.readline().split(" ")]
        portales, pisosNoVisitados = {}, {x: 0 for x in range(1,nPisos)}

        for i in range(nPortales):
            datos = stdin.readline().split(" ")
            portales[(int(datos[0])-1, int(datos[1])-1)] = (int(datos[2])-1, int(datos[3])-1)
            if pisosNoVisitados.get(int(datos[2])-1, -1) != -1:
                pisosNoVisitados.pop(int(datos[2])-1)

        entradas = list(portales.keys())

        if pisosNoVisitados.get(nPisos - 1, -1) != -1:
            print("NO EXISTE")
        else:
            for i in entradas:
                if pisosNoVisitados.get(i[0], -1) != -1:
                    portales.pop(i)
            print(calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales))
        nCasos -= 1

def calcularMinEnergiaDijkstra(nPisos, nHabitaciones, gastoEnergia, portales):
    inicio = (0,0)
    memoria, visitados, porVisitar = {inicio: 0}, {}, {inicio: 0}

    pq, entry = [], (0, inicio)
    hq.heappush(pq,entry)

    while len(pq)>0:
        (dist, actual) = hq.heappop(pq)
        porVisitar.pop(actual)

        visitados[actual] = 0

        vecinos = []
        if actual[1] > 0 and visitados.get((actual[0], actual[1]-1), -1) == -1:
            vecinos.append((actual[0], actual[1] - 1))

        if actual[1] < nHabitaciones and visitados.get((actual[0], actual[1]+1), -1) == -1:
            vecinos.append((actual[0], actual[1] + 1))

        if portales.get(actual, -1) != -1 and visitados.get(portales[actual], -1) == -1:
            vecinos.append(portales[actual])

        for vecino in vecinos:
            if vecino[0] > actual[0]:
                nuevoGasto = memoria[actual]
            else:
                nuevoGasto = gastoEnergia[vecino[0]] + memoria[actual]

            if memoria.get(vecino, -1) == -1:
                memoria[vecino] = nuevoGasto
            else:
                viejoGasto = memoria[vecino]
                if nuevoGasto < viejoGasto:
                    memoria[vecino] = nuevoGasto
            if visitados.get(vecino, -1) == -1 and porVisitar.get(vecino, -1) == -1:
                hq.heappush(pq,(nuevoGasto, vecino))
                porVisitar[vecino] = 0

    goal = (nPisos - 1, nHabitaciones - 1)

    if visitados.get(goal, -1) == -1:
        return "NO EXISTE"
    else:
        return memoria[(nPisos - 1,nHabitaciones - 1)]

lectura()


# comando: python ProblemaP1.py <2.in> salida.out
# comando: python ProblemaP1.py <P1_casesFP.in> salida.out

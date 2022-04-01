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
import multiprocessing as mp

def lectura():
    if __name__ == "__main__":
        nCasos = int(stdin.readline())
        nProcesadores, tCasos = mp.cpu_count(), nCasos
        casosPorProcesador= nCasos//nProcesadores + 1
        casos = [[] for i in range(nProcesadores)]
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

            # start = timer() # TODO: Quitar esto
            for i in entradas:
                if pisosNoVisitados.get(i[0], -1) != -1:
                    portales.pop(i)

            casos[(tCasos - nCasos)//casosPorProcesador].append((nPisos, nHabitaciones, gastoEnergia, portales))
            # elapsed_time = timer() - start # TODO: Quitar esto
            # print("Caso:", 1001 - nCasos,"tamaño de la torre",nPisos,"x",nHabitaciones, "Tiempo:", elapsed_time) # TODO: Quitar esto
            nCasos -= 1

        # print("Procesadores:", nProcesadores)
        # print("Total de casos:", tCasos)
        # print("Casos por procesador:", casosPorProcesador)
        # print(len(casos[0]))
        start = timer()
        pool = mp.Pool(processes=nProcesadores)
        print("\n".join(pool.map(calcularMinEnergiaDijkstra, casos)).strip())
        # print(calcularMinEnergiaDijkstra(caso))
        elapsed_time = timer() - start
        print("Time: %.10f" % elapsed_time)

def calcularMinEnergiaDijkstra(casos):
    # print(caso)
    resultados = []
    for caso in casos:
        if caso != []:
            (nPisos, nHabitaciones, gastoEnergia, portales) = caso[0], caso[1], caso[2], caso[3]
            inicio = (0,0)
            memoria, visitados, porVisitar = {inicio: 0}, {}, {inicio: 0}

            pq, entry = [], (0, inicio)
            hq.heappush(pq,entry)

            while len(pq)>0:
                (dist, actual) = hq.heappop(pq)
                porVisitar.pop(actual)

                visitados[actual], vecinos = 0, []

                if actual[1] > 0 and visitados.get((actual[0], actual[1]-1), -1) == -1:
                    vecinos.append((actual[0], actual[1] - 1))

                if actual[1] < nHabitaciones and visitados.get((actual[0], actual[1]+1), -1) == -1:
                    vecinos.append((actual[0], actual[1] + 1))

                if portales.get(actual, -1) != -1 and visitados.get(portales[actual], -1) == -1:
                    vecinos.append(portales[actual])

                for vecino in vecinos:
                    nuevoGasto = memoria[actual] if vecino[0] > actual[0] else gastoEnergia[vecino[0]] + memoria[actual]

                    if memoria.get(vecino, -1) == -1:
                        memoria[vecino] = nuevoGasto

                    viejoGasto = memoria[vecino]
                    if nuevoGasto < viejoGasto:
                        memoria[vecino] = nuevoGasto

                    if visitados.get(vecino, -1) == -1 and porVisitar.get(vecino, -1) == -1:
                        hq.heappush(pq,(nuevoGasto, vecino))
                        porVisitar[vecino] = 0

            if visitados.get((nPisos - 1, nHabitaciones - 1), -1) == -1:
                resultados.append("NO EXISTE")
            else:
                resultados.append(str(memoria[(nPisos - 1,nHabitaciones - 1)]))
    return "\n".join(resultados)



lectura()


# comando: python ProblemaP1.py <2.in> salida.out
# comando: python ProblemaP1.py <P1_casesFP.in> salida.out

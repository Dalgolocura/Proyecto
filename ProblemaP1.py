"""
Parte 1 Proyecto DALGO 2022-1
Autores:
    Boris Reyes - 202014743
    Daniel Aguilera - 202010592
    Juliana Galeano - 202012128
    William Mendez - 202012662
"""

import sys

def lectura():
    nMatriz = int(sys.stdin.readline())

    while nMatriz != 0:
        datos = sys.stdin.readline().split(" ")
        n = int(datos[0])
        m = int(datos[1])
        p = int(datos[2])
        gastoEnergia = sys.stdin.readline().split(" ")
        portales = []

        for i in range(p):
            datos = sys.stdin.readline().split(" ")
            portales.append([(int(datos[0]), int(datos[1])), (int(datos[2]), int(datos[3]))])

        nMatriz -= 1

def main():
    pass

main()

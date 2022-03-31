file1 = open("resultadoSinPQ.out", "r")
file2 = open("P2_casesFP.out", "r")
fileSalida = open("compararResultados.txt", "w")
diferentes = 0
caso = 1


linea1 = file1.readline().replace("\n", "")
linea2 = file2.readline().replace("\n", "")
fileSalida.write("Casos mal:\n")

while linea1 != "" or linea2 != "":
    if linea1 != linea2:
        diferentes += 1
        lineaSalida = "Caso " + str(caso) + ": Nuestro " + linea1 + " Profe " + linea2 + "\n"
        fileSalida.write(lineaSalida)
    linea1 = file1.readline().replace("\n", "")
    linea2 = file2.readline().replace("\n", "")
    caso += 1

fileSalida.write("Casos diferentes:" + str(diferentes))
file1.close()
file2.close()
fileSalida.close()

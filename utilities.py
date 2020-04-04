from random import randrange

def damematriz(numcol, numfil):

    matriz = []

    for i in range(numcol):
        matriz.append([])
        for j in range(numfil):
            matriz[i].append(randrange(9))

    for i in range(numcol):
        aux = ""
        for j in range(numfil):
            aux2 = str(matriz[i][j])
            aux = aux + aux2 + " "
        print(aux)
    return matriz

def printmatriz(matriz, numcol, numfil):
    for i in range(numfil):
        aux = ""
        for j in range(numcol):
            aux2 = str(matriz[i][j])
            aux = aux + aux2 + " "
        print(aux)
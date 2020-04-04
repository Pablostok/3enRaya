import utilities

numcol = 3
numfil = 3

matriz = utilities.damematriz(numcol, numfil)

# -------------------------------------------------------------

# j1 = input("Introduzca el nombre del jugador 1: ")
# j2 = input("Introduzca el nombre del jugador 2: ")
#
# print(Jugador 1 + ": O")
# print(Jugador 2 + ": X")

# -------------------------------------------------------------
listanegra = []
listaAux = []

ok = False
jugada = 0

while ok == False:
    print("")
    print("   ---Turno del Jugador 1---   ")
    print("")

    posis = input("Introduzca la ~i~ de la posición a utilizar: ")
    posjs = input("Introduzca la ~j~ de la posición a utilizar: ")

    posi = int(posis)
    posj = int(posjs)

    listanegra.append([])
    listanegra[jugada].append(posi)
    listanegra[jugada].append(posj)
    jugada = jugada + 1

    for i in range(numfil):
        for j in range(numcol):
            if i == posi and j == posj:
                matriz[i][j] = "O"

    utilities.printmatriz(matriz, numcol, numfil)

    ook = False
    while ook == False:
        print("")
        print("   ---Turno del Jugador 2---   ")
        print("")

        ok = False

        while ok == False:
            posis = input("Introduzca la ~i~ de la posición a utilizar: ")
            posjs = input("Introduzca la ~j~ de la posición a utilizar: ")

            posi = int(posis)
            posj = int(posjs)

            listaAux = [posi, posj]
            ok = utilities.comprobaruso(listanegra, listaAux)

        listaAux = []
        listanegra.append([])
        listanegra[jugada].append(posi)
        listanegra[jugada].append(posj)
        jugada = jugada + 1

        for i in range(numfil):
            for j in range(numcol):
                if i == posi and j == posj:
                    matriz[i][j] = "X"

        utilities.printmatriz(matriz, numcol, numfil)

        salir = utilities.comprobarganador(matriz)

        if salir == True:
            ook = True

        print("")
        print("   ---Turno del Jugador 1---   ")
        print("")

        ok = False

        while ok == False:
            posis = input("Introduzca la ~i~ de la posición a utilizar: ")
            posjs = input("Introduzca la ~j~ de la posición a utilizar: ")

            posi = int(posis)
            posj = int(posjs)

            listaAux = [posi, posj]
            ok = utilities.comprobaruso(listanegra, listaAux)

        listaAux = []
        listanegra.append([])
        listanegra[jugada].append(posi)
        listanegra[jugada].append(posj)
        jugada = jugada + 1

        for i in range(numfil):
            for j in range(numcol):
                if i == posi and j == posj:
                    matriz[i][j] = "O"

        utilities.printmatriz(matriz, numcol, numfil)

        salir = utilities.comprobarganador(matriz)

        if salir == True:
            ook = True

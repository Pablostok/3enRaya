import utilities

def juego():
    jugadores = utilities.recogidadatos()
    j1 = jugadores[0]
    j2 = jugadores[1]

    print(j1 + ": O")
    print(j1 + ": X")

    numcol = 3
    numfil = 3

    matriz = utilities.damematriz(numcol, numfil)

    # listanegra = []
    # listaAux = []
    jugador = ""

    ok = False
    jugada = 1

    while ok == False:

        if jugada % 2 != 0:
            print("")
            print("   ---Turno del Jugador 1 (" + j1 + ") ---   ")
            print("")
        else:
            print("")
            print("   ---Turno del Jugador 2 (" + j2 + ") ---   ")
            print("")

        casautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
        print("")

        pos = utilities.sacarpos(casautilizar)

        while pos[0] == 3:
            print("")
            print("   ---Error: Casilla inexistente---   ")
            print("")
            casautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
            print("")

            pos = utilities.sacarpos(casautilizar)

        ficha = utilities.sacarficha(jugada)

        matriz[pos[0]][pos[1]] = ficha

        utilities.printmatriz(matriz, numcol, numfil)

        jugada = jugada + 1

        salir = utilities.comprobarganador(matriz)

        if salir == True:
            ok = True

        # ook = False
        # while ook == False:
        #     print("")
        #     print("   ---Turno del Jugador 2 (" + j2 + ") ---   ")
        #     print("")
        #
        #     ok = False
        #
        #     while ok == False:
        #         posis = input("Introduzca la ~i~ de la posición a utilizar: ")
        #         posjs = input("Introduzca la ~j~ de la posición a utilizar: ")
        #         print("")
        #
        #         posi = int(posis)
        #         posj = int(posjs)
        #
        #         listaAux = [posi, posj]
        #         ok = utilities.comprobaruso(listanegra, listaAux)
        #
        #     listaAux = []
        #     listanegra.append([])
        #     listanegra[jugada].append(posi)
        #     listanegra[jugada].append(posj)
        #     jugada = jugada + 1
        #
        #     for i in range(numfil):
        #         for j in range(numcol):
        #             if i == posi and j == posj:
        #                 matriz[i][j] = "X"
        #
        #     utilities.printmatriz(matriz, numcol, numfil)
        #
        #     salir = utilities.comprobarganador(matriz)
        #
        #     if salir == True:
        #         ook = True
        #
        #     print("")
        #     print("   ---Turno del Jugador 1 (" + j1 + ") ---   ")
        #     print("")
        #
        #     ok = False
        #
        #     while ok == False:
        #         posis = input("Introduzca la ~i~ de la posición a utilizar: ")
        #         posjs = input("Introduzca la ~j~ de la posición a utilizar: ")
        #
        #         posi = int(posis)
        #         posj = int(posjs)
        #
        #         listaAux = [posi, posj]
        #         ok = utilities.comprobaruso(listanegra, listaAux)
        #
        #     listaAux = []
        #     listanegra.append([])
        #     listanegra[jugada].append(posi)
        #     listanegra[jugada].append(posj)
        #     jugada = jugada + 1
        #
        #     for i in range(numfil):
        #         for j in range(numcol):
        #             if i == posi and j == posj:
        #                 matriz[i][j] = "O"
        #
        #     utilities.printmatriz(matriz, numcol, numfil)
        #
        #     salir = utilities.comprobarganador(matriz)
        #
        #     if salir == True:
        #         ook = True

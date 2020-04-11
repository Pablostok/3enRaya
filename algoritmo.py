import utilities

def juego():
    numcol = 3
    numfil = 3

    jugadores = utilities.recogidadatos()
    j1 = jugadores[0]
    j2 = jugadores[1]

    print(j1 + ": O")
    print(j2 + ": X")

    # ----------------------------------------------------
    matriz = utilities.damematriz(numcol, numfil)  # Hacer matriz e imprimirla
    # -----------------------------------------------------

    jugador = ""
    jugada = 1

    salir = False
    while salir == False:

        if jugada % 2 != 0:
            jugador = j1
        else:
            jugador = j2

        print("")
        print("   ---Turno de " + jugador + " ---   ")
        print("")

        casillaautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
        print("")

        pos = utilities.sacarpos(casautilizar)

        while pos[0] == 3:
            print("")
            print("   ---Error: Casilla inexistente---   ")
            print("")
            casillaautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
            print("")

            pos = utilities.sacarpos(casillaautilizar)

        ficha = utilities.sacarficha(jugada)

        matriz[pos[0]][pos[1]] = ficha

        utilities.printmatriz(matriz, numcol, numfil)

        jugada = jugada + 1

        salir = utilities.comprobarganador(matriz, ficha, jugador)

        if jugada == 9 and salir == False:
            print("   /\/---Gana gato---\/\   ")

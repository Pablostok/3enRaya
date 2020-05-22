import utilities
import menu

def juego():
    numcol = 3
    numfil = 3

    jugadores = utilities.recogidadatos()
    j1 = jugadores[0]
    j2 = jugadores[1]

    # ----------------------------------------------------
    matriz = utilities.damematriz(numcol, numfil)  # Hacer matriz e imprimirla
    # -----------------------------------------------------

    jugador = ""
    jugada = 1
    ficha = ""

    salir = False
    while salir == False:

        if jugada % 2 != 0:
            jugador = j1
            ficha = "O"
        else:
            jugador = j2
            ficha = "X"

        print("")
        print("   ---Turno de " + jugador + "---   ")
        print("")

        casillaautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
        print("")

        pos = utilities.sacarpos(casillaautilizar)

        while pos[0] == 3:
            print("   ---Error---   ")
            print("")
            casillaautilizar = input("Introduzca la posición en el teclado numérico de la casilla libre a utilizar: ")
            print("")

            pos = utilities.sacarpos(casillaautilizar)

            if pos[0] != 3:
                if matriz[pos[0]][pos[1]] != "#":
                    pos[0] = 3

        matriz[pos[0]][pos[1]] = ficha

        utilities.printmatriz(matriz, numcol, numfil)

        salir = utilities.comprobarganador(matriz, ficha, jugador)

        if jugada == 9 and salir == False:
            print("")
            print("   /\/---Gana gato---\/\   ")
            salir = True

        jugada = jugada + 1

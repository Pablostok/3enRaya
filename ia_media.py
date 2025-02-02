import utilities
import menu

def juego():
    numcol = 3
    numfil = 3

    print("")
    j1 = input("Introduce tu nombre: ")
    print("")

    listalibre = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # ----------------------------------------------------
    tablero = utilities.damematriz(numcol, numfil)  # Hacer matriz e imprimirla
    # -----------------------------------------------------

    jugador = ""
    jugada = 1
    ficha = ""

    salir = False
    while salir == False:

        if jugada % 2 != 0:
            jugador = j1
            ficha = "O"

            print("")
            print("   ---Turno de " + jugador + "---   ")
            print("")

            casillaautilizar = input("Introduzca la posición en el teclado numérico de la casilla a utilizar: ")
            print("")

            pos = utilities.sacarpos(casillaautilizar)

            while pos[0] == 3:
                print("   ---Error---   ")
                print("")
                casillaautilizar = input(
                    "Introduzca la posición en el teclado numérico de la casilla libre a utilizar: ")
                print("")

                pos = utilities.sacarpos(casillaautilizar)

                if pos[0] != 3:
                    if tablero[pos[0]][pos[1]] != "#":
                        pos[0] = 3

            tablero[pos[0]][pos[1]] = ficha
            listalibre.remove(casillaautilizar)

            utilities.printmatriz(tablero, numcol, numfil)

            salir = utilities.comprobarganador(tablero, ficha, jugador)

        else:
            ficha = "X"

            print("")
            print("   ---Turno de la IA---   ")
            print("")

            ok = utilities.versigano(tablero, listalibre)

            if ok == True:
                salir = True
                exit()

            ook = utilities.versiganajugador(tablero, listalibre)

            if ok == False and ook[3] == False:
                indice = utilities.ponerenaleatorio(listalibre)
                tablero[indice[0]][indice[1]] = ficha
                posaborrar = str(indice[2])
                listalibre.remove(posaborrar)

                utilities.printmatriz(tablero, numcol, numfil)

                utilities.comprobarganadoriatonta(tablero)
            elif ook[3] == True:
                tablero[ook[0]][ook[1]] = ficha
                posaborrar = str(ook[2])
                listalibre.remove(posaborrar)

                utilities.printmatriz(tablero, 3, 3)

            else:
                salir = True

        if jugada == 9 and salir == False:
            print("")
            print("   /\/---Gana gato---\/\   ")
            salir = True

        jugada = jugada + 1

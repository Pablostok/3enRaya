def sacarpos(num):
    if num == "7":
        pos = [0, 0]
        return pos

    elif num == "8":
        pos = [0, 1]
        return pos

    elif num == "9":
        pos = [0, 2]
        return pos

    elif num == "4":
        pos = [1, 0]
        return pos

    elif num == "5":
        pos = [1, 1]
        return pos

    elif num == "6":
        pos = [1, 2]
        return pos

    elif num == "1":
        pos = [2, 0]
        return pos

    elif num == "2":
        pos = [2, 1]
        return pos

    elif num == "3":
        pos = [2, 2]
        return pos

    else:
        pos = [3, 3]
        return pos

def sacarficha(jugada):
    if jugada % 2 == 0:
        return "X"
    else:
        return "O"

def damematriz(numcol, numfil):
    matriz = []

    for i in range(numcol):
        matriz.append([])
        for j in range(numfil):
            matriz[i].append("#")

    for i in range(numcol):
        aux = ""
        for j in range(numfil):
            aux2 = str(matriz[i][j])
            aux = "   " + aux + aux2 + "  "
        print(aux)
    print("")
    print("         7  8  9")
    print("         4  5  6")
    print("         1  2  3")
    print("")
    return matriz

def printmatriz(matriz, numcol, numfil):
    for i in range(numfil):
        aux = ""
        for j in range(numcol):
            aux2 = str(matriz[i][j])
            aux = "    " + aux + aux2 + "  "
        print(aux)

def recogidadatos():
    print("")
    print("")
    j1 = input("Introduzca el nombre del jugador 1: ")
    j2 = input("Introduzca el nombre del jugador 2: ")
    print("")
    print(j1 + ": O")
    print(j2 + ": X")
    print("")

    lista = [j1, j2]

    return lista

def comprobarganador(matriz, ficha, jugador):
    gana = False

    # horizontales
    if matriz[0][0] == ficha and matriz[0][1] == ficha and matriz[0][2] == ficha:
        gana = True
    elif matriz[1][0] == ficha and matriz[1][1] == ficha and matriz[1][2] == ficha:
        gana = True
    elif matriz[2][0] == ficha and matriz[2][1] == ficha and matriz[2][2] == ficha:
        gana = True

    # verticales
    elif matriz[0][0] == ficha and matriz[1][0] == ficha and matriz[2][0] == ficha:
        gana = True
    elif matriz[0][1] == ficha and matriz[1][1] == ficha and matriz[2][1] == ficha:
        gana = True
    elif matriz[0][2] == ficha and matriz[1][2] == ficha and matriz[2][2] == ficha:
        gana = True

    # diagonales
    elif matriz[0][0] == ficha and matriz[1][1] == ficha and matriz[2][2] == ficha:
        gana = True
    elif matriz[2][0] == ficha and matriz[1][1] == ficha and matriz[0][2] == ficha:
        gana = True

    if gana == True:
        print("")
        print("\/\/\/--- Gana ~" + jugador + "~ ---\/\/\/")

    return gana


def comprobarganadoria(matriz):
    gana = False

    # horizontales
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
        gana = True
    elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
        gana = True
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
        gana = True

    # verticales
    elif matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
        gana = True
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
        gana = True
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        gana = True

    # diagonales
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        gana = True
    elif matriz[2][0] == "X" and matriz[1][1] == "X" and matriz[0][2] == "X":
        gana = True

    return gana


def versigano(matriz, listalibre):
    leido = len(listalibre)
    k = 0
    gana = False

    while gana == False and k < leido:
        pos = sacarpos(listalibre[k])
        i = pos[0]
        j = pos[1]
        matriz[i][j] = "X"

        ok = comprobarganadoria(matriz)

        if ok == True:
            print("   /\/---Gana gato---\/\   ")
            gana = True
        else:
            k = k + 1
            gana = False
            matriz[i][j] = "#"

    return gana

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
    return matriz

def printmatriz(matriz, numcol, numfil):
    for i in range(numfil):
        aux = ""
        for j in range(numcol):
            aux2 = str(matriz[i][j])
            aux = "    " + aux + aux2 + "  "
        print(aux)

def comprobarganador(matriz):
    # Combinaciones O

    # horizontales
    if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O":
        print("--- Gana ~O~ ---")
        return True
    elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
        print("--- Gana ~O~ ---")
        return True
    elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")
        return True

    # verticales
    elif matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
        print("--- Gana ~O~ ---")
        return True
    elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
        print("--- Gana ~O~ ---")
        return True
    elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")
        return True

    # diagonales
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")
        return True
    elif matriz[2][0] == "O" and matriz[1][1] == "O" and matriz[0][2] == "O":
        print("--- Gana ~O~ ---")
        return True

    # Combinaciones X

    # horizontales
    elif matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
        print("--- Gana ~X~ ---")
        return True
    elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
        print("--- Gana ~X~ ---")
        return True
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")
        return True

    # verticales
    elif matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
        print("--- Gana ~X~ ---")
        return True
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
        print("--- Gana ~X~ ---")
        return True
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")
        return True

    # diagonales
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")
        return True
    elif matriz[2][0] == "X" and matriz[1][1] == "X" and matriz[0][2] == "X":
        print("--- Gana ~X~ ---")
        return True

    else:
        return False

def comprobaruso(listanegra, listaAux):
    leido = len(listanegra)

    for i in range(0, leido + 1):
        if listaAux in listanegra:
            print("")
            print("--- Error --- Casilla ocupada ---")
            print("")
            return False
        else:
            return True

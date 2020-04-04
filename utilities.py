from random import randrange

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
    if matriz[0][0] and matriz[0][1] and matriz[0][2] == "O":
        print("--- Gana ~O~ ---")
    if matriz[1][0] and matriz[1][1] and matriz[1][2] == "O":
        print("--- Gana ~O~ ---")
    if matriz[2][0] and matriz[2][1] and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")

    # verticales
    if matriz[0][0] and matriz[1][0] and matriz[2][0] == "O":
        print("--- Gana ~O~ ---")
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == "O":
        print("--- Gana ~O~ ---")
    if matriz[0][2] and matriz[1][2] and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")

    # diagonales
    if matriz[0][0] and matriz[1][1] and matriz[2][2] == "O":
        print("--- Gana ~O~ ---")
    if matriz[2][0] and matriz[1][1] and matriz[0][2] == "O":
        print("--- Gana ~O~ ---")

    # Combinaciones X

    # horizontales
    if matriz[0][0] and matriz[0][1] and matriz[0][2] == "X":
        print("--- Gana ~X~ ---")
    if matriz[1][0] and matriz[1][1] and matriz[1][2] == "X":
        print("--- Gana ~X~ ---")
    if matriz[2][0] and matriz[2][1] and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")

    # verticales
    if matriz[0][0] and matriz[1][0] and matriz[2][0] == "X":
        print("--- Gana ~X~ ---")
    if matriz[0][1] and matriz[1][1] and matriz[2][1] == "X":
        print("--- Gana ~X~ ---")
    if matriz[0][2] and matriz[1][2] and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")

    # diagonales
    if matriz[0][0] and matriz[1][1] and matriz[2][2] == "X":
        print("--- Gana ~X~ ---")
    if matriz[2][0] and matriz[1][1] and matriz[0][2] == "X":
        print("--- Gana ~X~ ---")


def comprobaruso(listanegra, posi, posj):
    leido = len(listanegra)
    ok = False
    o = 0

    for i in range(0, leido):
        if posi == listanegra[i][o] and posj == listanegra[i][o + 1]:
            print("--- Error --- Casilla ocupada ---")
            return False
        else:
            return True

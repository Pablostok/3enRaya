import algoritmo


# Mejoras:
# Tablero con numeros
# Mostrar tablero numerico
# Mostrar nombre ganador
# Mostrar nombre de quien le toque
# Más brilli - brilli
# Antes de stringear, comprobar que es número
# Si el tablero se acaba, no hacer más
# Variable del jugador para comprobarganador

def caratula():
    print("###################################")
    print("#                                 #")
    print("#            T R E S              #")
    print("#              E N                #")
    print("#            R A Y A              #")
    print("#                                 #")
    print("#                                 #")
    print("#             · By Pablo y Amanda #")
    print("###################################")

    menu()


def menu():
    print("")
    print("   ---¿Qúe quieres hacer?---   ")
    print("")
    print("1.- Jugar")
    print("2.- Salir")
    print("")

    res = input("Introduzca número: ")

    if res == "1":
        print("")
        print("")
        algoritmo.juego()

    elif res == "2":
        exit()


caratula()

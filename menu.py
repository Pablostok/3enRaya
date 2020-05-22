import algoritmo
import ia_tonta
import ia_facil
import ia_media


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
    print("   ---¿Qué quieres hacer?---   ")
    print("")
    print("1.- Elegir modalidad")
    print("2.- Salir")
    print("")

    res = input("Introduzca número: ")

    if res == "1":
        print("")
        print("")
        print("   ---Elija modalidad---   ")
        print("")
        print("")
        print("1.- IA Fácil")
        print("2.- IA Media")
        print("3.- IA Difícil")
        print("4.- Dos jugadores")
        print("5.- Atrás")
        print("")
        print("")
        elegirmodalidad()

    elif res == "2":
        exit()

def elegirmodalidad():

    resp = input("Introduzca número: ")
    if resp == "1":
        ia_tonta.juego()
    elif resp == "2":
        ia_facil.juego()
    elif resp == "3":
        ia_media.juego()
    elif resp == "4":
        algoritmo.juego()
    elif resp == "5":
        menu()


caratula()

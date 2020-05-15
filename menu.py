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
        print("1.- IA Tonta")
        print("2.- IA Fácil")
        print("3.- IA Intermedia")
        print("4.- IA Difícil")
        print("5.- Dos jugadores")
        print("6.- Atrás")
        print("")
        print("")
        resp = input("Introduzca número: ")
        if resp == "1":
            ia_tonta.juego()
        elif resp == "2":
            ia_facil.juego()
        elif resp == "3":
            ia_media.juego()
            menu()
        elif resp == "4":
            print("")
            print("")
            print("   --- Esta función todavía no está disponible, disculpe las molestias ---   ")
            print("")
            print("")
            menu()
        elif resp == "5":
            algoritmo.juego()
        elif resp == "6":
            menu()

    elif res == "2":
        exit()


caratula()

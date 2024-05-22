from os import system

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu()->str:
    limpiar_pantalla()
    print("      Menu de Opciones")
    print("1-Saludar")
    print("2-Brindar")
    print("3-Despedir")
    print("4-Salir")

    return  input("Ingrese opcion: ")

def saludar():
    print("Hola")

def brindar():
    print("Chin Chin")

def despedir():
    print("Chau. Nos vemos")


#-----------------------------------

flag_saludo = False
flag_brindis = False


while True:
    
    match menu():
        case "1":
            saludar()
            flag_saludo = True
        case "2":
            if flag_saludo:
                brindar()
                flag_brindis = True
            else:
                print("Antes de brindar, primero saludemonos")
        case "3":
            if flag_brindis:
                despedir()
            elif flag_saludo == False:
                print("No nos podemos despedir, porque no nos saludamos")
            else:
                print("No nos despidamos sin brindar")
            flag_saludo = False
            flag_brindis = False
        case "4":
            print("1-SI")
            print("2-NO")
            confirmacion = input("¿Estas seguro? ")
            if confirmacion == "1":
                break
            elif confirmacion == "2":
                print("Gracias")
                continue
    pausar()
    # input("Presiones enter para continuar...")


print("Fin del programa")

#Salir -> confirmar para salir. 
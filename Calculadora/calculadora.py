from os import system
from operadores import *

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu()->str:
    limpiar_pantalla()
    print("        Calculadora")
    print("1-Ingresar primer valor ")
    print("2-Ingresar segundo valor ")
    print("3-Elegir operador ")
    print("4-Salir ")
    return  input("Ingrese opcion: ")



# --------------------------
    
bandera_primer_valor = True
bandera_segundo_valor = True
bandera_operador = True
bandera_division_0 = True
bandera_factorial = True

while True:
    match menu():
        case "1":
            if bandera_primer_valor == True:
                limpiar_pantalla()
                A = int(input("Ingrese el primer valor "))
                bandera_primer_valor = False
            elif bandera_primer_valor == False:
                limpiar_pantalla()
                print("Ya ingresaste el primer valor ")

        case "2":
            if bandera_primer_valor == True:
                limpiar_pantalla()
                print("Primero debes ingresar el primer valor ")
            elif bandera_segundo_valor == True:
                limpiar_pantalla()
                B = int(input("Ingrese el segundo valor "))
                bandera_segundo_valor = False
            elif bandera_segundo_valor == False:
                limpiar_pantalla()
                print("Ya ingresaste el segundo valor ")

        case "3":
            limpiar_pantalla()
            if bandera_primer_valor == False and bandera_segundo_valor == False:
                limpiar_pantalla()
                print("        Operador")
                print(f"1-Sumar ({A} + {B}) ")
                print(f"2-Restar ({A} - {B})")
                print(f"3-Dividir ({A} / {B})")
                print(f"4-Multiplicar ({A} * {B})")
                print(f"5-Factorial ({A}! y {B}!)")
                operador = input("Ingrese opcion: ")
                match operador:
                    case "1":
                        resultado = sumar(A, B)
                        s_operador = "+"
                    case "2":
                        resultado = resta(A, B)
                        s_operador = "-"
                    case "3":
                        if B != 0:
                            resultado = division(A, B)
                            s_operador = "/"
                        elif B == 0:
                            bandera_division_0 = False
                        
                    case "4":
                        resultado = multiplicacion(A, B)
                        s_operador = "*"
                    case "5":
                        bandera_factorial = False
                        resultadoF1 = factorial(A)
                        resultadoF2 = factorial(B)
                        s_operador = "!"
                bandera_operador =False
                break
            elif bandera_primer_valor == True or bandera_segundo_valor == True:
                print("Primero debes ingresar todos los valores a operar")

        case "4":
            limpiar_pantalla()
            print("¿Seguro?")
            print("1-SI")
            print("2-NO")
            confirmacion = input("Ingrese opcion: ")
            if confirmacion == "1":
                break
            elif confirmacion == "2":
                print("Gracias")
                continue
    pausar()

limpiar_pantalla()

if bandera_division_0 == False:
    print(f"No se puede dividir por 0")
elif bandera_factorial == False:
    print(f"El resultado de {A}{s_operador} es {resultadoF1}, y el resultado de {B}{s_operador} es {resultadoF2}")
elif bandera_operador == False:
    print(f"El resultado de {A}{s_operador}{B} es: {resultado}")
    
print("Fin del Programa")
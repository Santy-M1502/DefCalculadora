from math import pi

def calcular_perimeto_circuferencia(radio: int)->float:
    return 2 * radio * pi

def calcular_perimeto_rectangulo(base:int, altura:int)->int:
    return 2*(base * altura)

def calcular_perimero_cuadrado(lado):
    return 4*lado

#codigo de calidad, usar otras funciones para resolver otro
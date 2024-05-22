def sumar(valor1, valor2):
    """_summary_

    Args:
        valor1 (_type_): Primer valor a sumar
        valor2 (_type_): Segundo valor a sumar

    Returns:
        _type_: Retornara el resultado de la suma
    """
    return valor1 + valor2

def resta(valor1, valor2):
    """_summary_

    Args:
        valor1 (_type_): Primer valor a restar
        valor2 (_type_): Segundo valor a restar

    Returns:
        _type_: Retornara el resultado de la resta
    """
    return valor1 - valor2

def division(valor1, valor2):
    """_summary_

    Args:
        valor1 (_type_): Primer valor a dividir
        valor2 (_type_): Segundo valor a restar

    Returns:
        _type_: Retornara el resultado de la division
    """
    return valor1 / valor2

def multiplicacion(valor1, valor2):
    """_summary_

    Args:
        valor1 (_type_): Primer valor a multiplicar
        valor2 (_type_): Segundo valor a multiplicar

    Returns:
        _type_: Retornara el resultado de la multiplicacion
    """
    return valor1 * valor2

def factorial(valor1:int)->int:
    """_summary_

    Args:
        valor1 (int): Valor a factorizar

    Raises:
        ValueError: Lanza exception si no es un numero natural

    Returns:
        int: Retornara el resultado de la factorizacion
    """
    if valor1 < 0:
        raise ValueError("El factorial es solo para numeros naturales")
    n = 1
    for i in range(2, valor1 + 1):
        n *= i
    return n
"""
--->Aqui estamos implementando el doctest dentro de un script
    ya sea en el primer comentario o, dentro del doctring de las funciones
>>> fibonacci(20)
6765
"""

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number -1) + fibonacci(number-2)

def resta (num_1, num_2):
    """
    La suma de 10 + 20 es igual a 30
    >>> 20 - 10
    10
    """
    return num_1 - num_2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testfile('prueba.py')

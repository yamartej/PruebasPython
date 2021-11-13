def suma (a, b):
    """
    >>> from algoritmo import fibonacci

    Retorna la suma de 2 + 2 es 4
    >>> 2 + 2
    4

    La suma de 10 + 20 es igual a 30
    >>> 10 + 20
    30

    >>> def suma_prueba(*args):
    ...     return sum(args)

    La suma de 10 + 20 + 30 debe ser igual a 60
    >>> suma_prueba(10, 20, 30)
    60
    
    >>> fibonacci(20)
    6765

    """

    return a + b
'''
Con esta lineas de codigo hacemos las pruebas de este script.
Y si queremos hacer pruebas de otro archivo hacemos uso de
doctest.testfile("nombre_de_archivo")
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testfile('prueba.py')

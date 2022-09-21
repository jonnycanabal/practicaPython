def sumar1(a,b):
    return a+b


def sumar2(a:int,b:int)->int:
    """Esta función me suma dos numeros enteros
    Args:
        a (int): Número uno a sumar
        b (int): Número dos a sumar
    Returns:
        int: resultado de la suma 
    """
    return a+b

print(sumar1(5,6))
print(sumar2(5,6))
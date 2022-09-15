# (14/09/2022)
"""# El comando IF
num = int (input("Ingrese un número:\n"))

if num == 100:
    print("Usted escribió el 100")
elif num > 100:
    print("Usted escribió un número mayor a 100")
else:
    print("Usted escribió un numero menor a 100")
"""

# Condicionales multiples
"""x = 5
if 0 < x:
    if x < 10:
        print("x es un numero positivo de un solo dígito") # No recomendable

if 0 < x and  x <10:
    print("x es un número positivo de un solo dígito.") # Recomendable

if 0 < x <10:
    print("x es un número positivo de un solo dígito.") 
"""

# Ejercicio

"""
El profesor le indica a Diego que durante el curso se sacaron 4 notas y todas tienen el mismo valor. Además le
solicita que debe elaborar un programa que le ayude a calcular si aprobó o debe recuperar la materia no solo a él
sino a todos sus compañeros.
Para esto debe planificar correctamente un código en python que les ayude a automatizar este proceso.
"""
"""nota1 = 3.5
nota2 = 2.9
nota3 = 3.2
nota4 = 3.0

# round (funcion de Python para redonder la cifra round("condicion","Cantidad de Digitos"))
# promedio = round((nota1 + nota2 + nota3 + nota4) /4,1)
promedio = (nota1 + nota2 + nota3 + nota4) /4

if promedio >= 3:
    print(f"Su nota fue de {promedio}, usted aprobó")
else:
    print(f"Su nota fue de {promedio}, usted reprobó")
"""

"""# round
print(round(3.14159265,2))
"""

# Ejercicio 2
"""De los tiempos de dos competidores cual fue el mas rapido"""
corredor1 = 60
corredor2 = 45

if corredor1 < corredor2:
    print("El corredor 1 es mas rapido que el corredor 2")
else:
    print("El corredor 2 es mas rapido que el corredor 1")

print("El corredor mas rapido tuvo un tiempo de ", min(corredor1,corredor2))



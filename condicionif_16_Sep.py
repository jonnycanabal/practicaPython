# Escribir un programa que pregunte la edad de un usuario y muestra por pantalla si es mayor de edad o no.

"""edad = int(input("\nIngresa tu edad: "))

if edad >= 18:
    print (f"Es mayor de edad, tienes {edad} años")

else:
    print (f"El ususario es menor de edad, tienes {edad} años")"""


#***********************************************************************************************************

"""Escribir un programa que pregunte la edad de un usuario y muestra 
por pantalla si es mayor de edad o no y si es mayor de edad debe
evaluar si pertenece a la tercera edad."""

"""edad = int(input("\nEscribe tu edad: "))

if edad < 18:
    print(f"es menor de edad, tienes {edad} años")
elif edad >= 60:
    print (f"Es mayor de edad, tienes {edad} años")
    print ("Ademas perteneces a la tercera edad")
else:
    print (f"Es mayor de edad, tienes {edad} años")"""


#***********************************************************************************************************

# Pedir 3 numeros por teclado e imprimir cual es el mayor de los 3
""" Pedir tres números por teclado e imprimir cuál es el menor de los tres, validando si los tres
número son iguales."""

"""num1 = int(input("Ingrese el primer numero: ")) #30
num2 = int(input("Ingrese el primer numero: ")) #20
num3 = int(input("Ingrese el primer numero: ")) #10

if num1 > num2 and num1 > num3:
    print (f"El numero {num1} Es mayor que {num2} y {num3}")

elif num2 > num1 and num2 > num3:
    print (f"El numero {num2} Es mayor que {num1} y {num3}")

elif num3 > num1 and num3 > num2:
    print (f"El numero {num3} Es mayor que {num1} y {num2}")


if num1 < num2 and num1 < num3:
    print (f"El numero {num1} Es menor que {num2} y {num3}")

elif num2 < num1 and num2 < num3:
    print (f"El numero {num2} Es menor que {num1} y {num3}")

elif num3 < num1 and num3 < num2:
    print (f"El numero {num3} Es menor que {num1} y {num2}")
"""

"""
if num1 == num2 and num1 == num3:
    print (f"Los numeos son iguales")

elif num1 == num2 and num1 == num3:
    print (f"Los numeos son iguales")

elif num1 == num2 and num1 != num3:
    print (f"Los numeros {num1} y {num2} son iguales y diferentes de {num3}")

elif num1 == num3 and num1 != num2:
    print (f"los numeros {num1} y {num3} son iguales y diferentes de {num2}")

elif num2 == num1 and num2 != num3:
    print (f"Los numeros {num2} y {num1} son iguales y diferentes de {num3}")

elif num2 == num3 and num2 != num1:
    print (f"Los numeros {num2} y {num3} son iguales y diferentes de {num1}")

elif num3 == num1 and num3 != num2:
    print (f"Los numeros {num3} y {num1} son iguales y diferentes de {num2}")

elif num3 == num2 and num3 != num1:
    print (f"Los numeros {num3} y {num2} son iguales y diferentes de {num1}")"""


# Ejercicio de ciclos

"""numero = float(input('Ingrese un número. 0 para terminar: '))

while (numero !=0):
    numero = float(input('Ingrese un número. 0 para terminar: '))

print ('Fin del programa')"""

cont = 0
for i in range (500,1000,2):
    print(i)
    cont +=1

print (f"iteraciones {cont}")


# Ciclo iterativo while
"""
manzanas = 5
contador = 0

print (f"Se ha iniciado el carrito. En total hay {contador} manzanas")

while(contador < manzanas):
    contador = contador+1
    print(f"Se ha agregado una manzana a la canasta. Ahora hay {contador} manzanas.")
"""

# Ciclo iterativo for controlado por cantidad

"""print ("Se ha iniciado el carrito. En total hay 0 manzanas")
for i in range(1,6):
    print(f"Se ha agregado una manzana a la canasta. Ahora hay {i} manzanas")
"""

cantidad_estudiantes = "0"
suma= 0
promedio = 0
estudiante = None
nota = 0
contador = 0


while cantidad_estudiantes.isdigit() == True:

    cantidad_estudiantes = input("\nIngrese la cantidad de estudiantes: ")

    if cantidad_estudiantes.isdigit() == True:

            for x in range(1,int(cantidad_estudiantes)+1):
                estudiante = input(f"\nIngrese el nombre del estudiante #{x}: ")
                for y in range(1,4):
                    nota = input(f"Ingrese la nota #{y} del estudiante {estudiante}: ")
                    if nota.isdigit() == True: # INTENAR INCLUIR UN CICLO WHILE PARA HACER EL PROCESO DE VERIFICACION SI INGRESA UN NUMERO O UNA LETRA CON EL ISDIGIT()
                        suma += int(nota)
                    else:
                        print("No digitaste una Nota, Por favor Ingresa un numero")
                        nota = "0"

                promedio = round(suma / 3,1)
                print(f"\nEl promedio del estudiante {estudiante} es de: {promedio}")
                suma=0

                contador +=1

            cantidad_estudiantes = "l"
    else:
        print("\nError, No digitaste un número")
        cantidad_estudiantes = "0"










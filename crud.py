# menú principal
"""
opcion = None
producto = None

while opcion != "5":
    print("\nMENU PRINCIPAL PRODUCTOR")
    print("1. Crear productor")
    print("2. Ver productor")
    print("3. Actualizar productor")
    print("4. Eliminar productor")
    print("5. Salir \n")

    opcion = input("\nDigite la opción: ")

    if opcion == "1":
        producto = input("\nIngrese el producto: ")

    elif opcion == "2":
        if producto == None:
            print("\nNo hay producto en el sistema, Ingrese uno por favor ")
        else:
            print("\nEl producto ingresado fue: " + producto)

    elif opcion == "3":
        producto = input("\nIngrese el nuevo producto: ")
        print("El nuevo producto ingresado fue: " + producto)

    elif opcion == "4":
        producto = None
        print("\nEl producto se Eliminó de forma exitosa")
    
    else:
        print("\nopción no valida")
"""

# ********************************************** EJERCICIO CON UN POCO MAS DE COMPLEJIDAD *******************************************************

""" 
AGREGAR NUEVO ESUDIANTE, REMOVER Y CONSULTAR.
HACER EL EJERCICIO ANTEIOR CON UN MENU PARA PODER REGISTRAR ESTUDIANTES CON DIFERENTES DATOS. 
ALMACENANDO DATOS, PARA MOSTRAR, EDITAR, ELIMINAR POR MEDIO DE DICCIONARIO, LISTA, TUPLA O CONJUNTO SEGUN SU PREFERENCIA.
"""


# Variable y diccionario principal declarados.

import keyword


opcion = None
estudiantes = {'123': {'nombre': 'jonny', 'apellido': 'canabal', 'edad': '28', 'telefono': '3183865455'}, '456': {'nombre': 'diego', 'apellido': 'briñez', 'edad': '25', 'telefono': '15987532'}, '789': {'nombre': 'zamir', 'apellido': 'acevedo', 'edad': '30', 'telefono': '1478523699'}}
contador = 0

# FUNCIONES ----------------------------------------------------------------------------
def mostrar (id): # FOR PARA RECORRER LAS LLAVES DEL DICCIONARIO PARA QUE LOS CAMPOS SEAN DINAMICOS
    if id in estudiantes:
        print("########################")
        print(f"#       id: {id}        #") 
        print("########################\n")
        print("Nombre:", estudiantes[id]["nombre"])
        print("Apellido:",estudiantes[id]["apellido"])
        print("Edad:",estudiantes[id]["edad"])
        print("Teléfono:",estudiantes[id]["telefono"],"\n")
        print("########################")
        print("////////////////////////")

    else:
        print("El estudiante no existe")

"""def mostrar2(id):
    if id in estudiantes:
        for x in estudiantes:
            print("Nombre:", estudiantes[id]["nombre"])

    else:
        print("El estudiante no existe")"""

while opcion != "7":
    # Menu de opciones.
    print("\nMENU PRINCIPAL PRODUCTOR")
    print("1. Ingresar un nuevo Estudiante.")
    print("2. Consultar cuantos estudiante estan registrados.")
    print("3. Consultar el estudiante por su identificacion.")
    print("4. Eliminar un Estudiante.")
    print("5. Ingresar un dato nuevo al estudiante")
    print("6. Modificar un dato del Estudiante.")
    print("7. Salir \n")

    # Ingresar la opcion que desea realizar segun el menu.
    opcion = input("\nDigite la opción: ")

    if opcion == "1":
        # datos del nuevo estudiante
        # el dato "identificacion" queda tambien establecido como una clave en el diccionario.
        identificacion= input ("Ingrese la identificacion del estudiante: ")

        while identificacion in estudiantes:
            print("El estudiante ya se encuentra regitrado, intentelo nuevamente")
            identificacion= input ("Ingrese la identificacion del estudiante: ")

        else:
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            edad = input(f"ingrese la edad del estudiante {nombre}: ")
            telefono = input(f"ingrese el telefono del estudiante {nombre}: ")
        
        # Se agrega el diccionario principal una clave con el nombre del estudiante y cuyo valor sera otro diccionario con sus datos.
        estudiantes.update({identificacion:{'nombre': nombre, 'apellido': apellido, 'edad': edad, 'telefono': telefono}})
    
    elif opcion == "2":
        # con el (len) se cuenta las llaves principales del diccionario y asi se sabe cuantos estudiantes estan registrados
        # con el otro print imprimimos las llaves principales que tiene el diccionario y sabemos la identificacion de los estudiantes registrados.
        print(f"En total en el sistema se encuentra registrados: ({len(estudiantes)}) estudiantes")
        print("Los estudiantes registrados en el sistema son: " + str(estudiantes.keys()))
        #recorro el diccionario y por medio de una funcion muestro todos los datos con un formato.
        for estudiante in estudiantes:
            mostrar(estudiante)

    elif opcion == "3":
        # Aqui consultamos los datos segun el ID del estudiante que solicitemos
        consultarEstudiante = input("Ingrese el ID del estudiante que desea consultar: ")
        mostrar(consultarEstudiante)

    elif opcion == "4":
        eliminarEstudiante = input("Ingrese el ID del estudiante que desea eliminar: ")
        estudiantes.pop(eliminarEstudiante)

    elif opcion == "5":
        nombreEstudiante = input("Ingrese el ID del estudiante a quien desea agregar un dato: ")
        print (f"Selecciono al estudiante {estudiantes.get(nombreEstudiante)}")
        dato = input("Ingrese el nombre del dato que desea agregar: ")
        informacion = input(f"Ingrese la informacion del {dato}: ")
        estudiantes[nombreEstudiante][dato]=informacion # esta estructura tambien me sirve para modificar un dato ya existente.
    elif opcion == "6":
        print("")

    elif opcion == "7":
        print("Hasta la proxima.")

    else:
        print("\nopción no valida")
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
opcion = None
estudiantes = {'123': {'nombre': 'jonny', 'apellido': 'canabal', 'edad': '28', 'telefono': '3183865455'}, '456': {'nombre': 'diego', 'apellido': 'briñez', 'edad': '25', 'telefono': '15987532'}, '789': {'nombre': 'zamir', 'apellido': 'acevedo', 'edad': '30', 'telefono': '1478523699'}}

# FUNCIONES ----------------------------------------------------------------------------

"""
# Primera funcion realizada para (mostrar)
def mostrar (id):
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
"""

# Funcion de (formato) que dara un marco para la funcion mostrar2
def formato (id: str, contenido: str = ""):
    marco = "#"*37
    print(marco)
    print(f"###      Identifición: {id}      ###")
    print(marco)
    if len(contenido)>0:
        print("\n"+contenido+f"\n" + marco + f"\n")

# Segundo intento de la funcion (mostrar) recorriendo por medio de for e implementando la funcion formato
def mostrar2 (id: str):
    if id in estudiantes:  
        contenido = ""   
        for key in estudiantes[id]:
            valor = estudiantes[id][key]
            contenido += (f"{key}: {valor}\n")
        formato(f"{id}", contenido)

    else:
        print("\nEl estudiante no existe!!!!!!!")

# Funcion (Eliminar) / Colocando condiciones si existe, upper() y si ingresa una identificacion no valida.
def eliminar (id):
    if id in estudiantes:
        confirmar = input(f"Seguro que desea eliminar al estudiante con identificacion {id} (Y / N): ")
        if confirmar.upper() == "Y":
            estudiantes.pop(id)
            print(f"\nEl estudiante con identificación -{id}-, Se elimino de forma EXITOSA!!!")
        
        elif confirmar.upper() == "N":
            print("\nEliminacion cancelada.")

        else:
            print("Opcion no valida!!!!, Intentelo de nuevo.")

    else:
        print(f"\nNo se encontro ningun estudiantes con la identificacion -{id}- ")
        print("VUELVA A INTENTARLO!!!")

# Inicio del Programa ------------------------------------------------------------------------------------------
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

        # Sub menu de la opcion 1
        sub1 = None
        while sub1 != "2":
            print("\nMENU INGRESAR ESTUDIANTE")
            print("1. Ingresar")
            print("2. Cancelar")

            sub1 = input("Ingrese la opcion")
            if sub1 == "1":
                # datos del nuevo estudiante
                # el dato "identificacion" queda establecido como una clave en el diccionario estudiantes.
                identificacion= input ("Ingrese la identificacion del estudiante: ")

                #Validamos si la identificacion ingresada esta o no en el diccionario estudiantes.
                if identificacion in estudiantes:
                    print("El estudiante ya se encuentra regitrado, intentelo nuevamente")
        
                else:
                    nombre = input("Ingrese el nombre del estudiante: ")
                    apellido = input("Ingrese el apellido del estudiante: ")
                    edad = input(f"ingrese la edad del estudiante {nombre}: ")
                    telefono = input(f"ingrese el telefono del estudiante {nombre}: ")
                
                    # Se agrega el diccionario principal una clave con el nombre del estudiante y cuyo valor sera otro diccionario con sus datos.
                    estudiantes.update({identificacion:{'nombre': nombre, 'apellido': apellido, 'edad': edad, 'telefono': telefono}})

            elif sub1 == "2":
                print("\nSalio del menu (Ingresar Estudiante)!!!!!")
            
            else:
                print("\nOpción no valida!!!!!!")

        
    elif opcion == "2":
        # con el (len) se cuenta las llaves principales del diccionario y asi se sabe cuantos estudiantes estan registrados
        # con el otro print imprimimos las llaves principales que tiene el diccionario y sabemos la identificacion de los estudiantes registrados.
        print(f"En total en el sistema se encuentra registrados: ({len(estudiantes)}) estudiantes")
        print("Los estudiantes registrados en el sistema son: " + str(estudiantes.keys()))
        #recorro el diccionario y por medio de una funcion muestro todos los datos con un formato.
        for estudiante in estudiantes:
            mostrar2(estudiante)

    elif opcion == "3":
        # Aqui consultamos los datos segun el ID del estudiante que solicitemos
        consultarEstudiante = input("Ingrese el ID del estudiante que desea consultar: ")
        mostrar2(consultarEstudiante)

    elif opcion == "4":
        print (f"La identificación de los estudiantes registrados en el sistema son: {estudiantes.keys()}")
        eliminarEstudiante = input("Ingrese el ID del estudiante que desea eliminar: ")
        eliminar(eliminarEstudiante)

    elif opcion == "5":
        nombreEstudiante = input("Ingrese el ID del estudiante a quien desea agregar un dato: ")
        print (f"Selecciono al estudiante {estudiantes.get(nombreEstudiante)}")
        dato = input(f"Ingrese el dato que desea agregar del estudiante con identificación {nombreEstudiante}: ")
        informacion = input(f"Ingrese la informacion del {dato}: ")
        estudiantes[nombreEstudiante][dato]=informacion # esta estructura tambien me sirve para modificar un dato ya existente.
    
    elif opcion == "6":
        nombreEstudiante = input("Ingrese el ID del estudiante a quien desea agregar un dato: ")
        print (f"Selecciono al estudiante {estudiantes.get(nombreEstudiante)}")
        dato = input(f"Ingrese el dato que desea modificar del estudiante con identificación {nombreEstudiante}: ")
        informacion = input(f"Ingrese la informacion del {dato}: ")
        estudiantes[nombreEstudiante][dato]=informacion # esta estructura tambien me sirve para modificar un dato ya existente.

    elif opcion == "7":
        print("Hasta la proxima.")

    else:
        print("\nopción no valida")
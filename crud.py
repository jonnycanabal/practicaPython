# menú principal
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









"""
[] corchetes
{} llaves
() parentesis
<> parentesis angular
"""

#Listas
###################################
#           Definición      []    #
###################################
frutas1= ["pera","mango","papaya"]
frutas2= list() 
###################################
print("Lista:",frutas1[1])
###################################
#           Modificar      []     #
###################################
frutas2.append("coco")
frutas2.append("kiwi")
frutas1.extend(frutas2)
print("Agregado a lista:",frutas1)
###################################
#           operaciones    []     #
###################################
print("posición del coco:",frutas1.index("coco")) # devuelve la posición


frutas1.insert(3,"fresa") # ingresar un valor en posición especifica
print("ingresar en posición 3:",frutas1[3] )

frutas1.remove("fresa")
print("remover en posición 3:",frutas1[3] )

frutas1[3]="banano"
print("modificar:",frutas1)


print("pop:",frutas1.pop(3))
print(frutas1)
###################################
#           recorrerlo     []     #
###################################
print("############recorrido lista###############")
for fruta in frutas1:
    print(fruta)
print("###########################")

#Diccionarios
###################################
#           Definición      {}    #
###################################
canasta1={"bolsa1":["pera","mango","papaya"],
         "bolsa2":5}
canasta2= dict()
##################################
print("Dicionario:",canasta1["bolsa1"])

print("Dicionario:",canasta1["bolsa1"][2]) #si quisiera acceder a un elemento en especifico de la lista 
###################################
#           operaciones    {}     #
###################################
print("listar llaves:",canasta1.keys())
print("listar valores:",canasta1.values())
print("listarlos tupla:",canasta1.items())
print("Existe bolsa2","bolsa2" in canasta1)

canasta1["bolsa3"]= False
print("agregar a diccionario:", canasta1)
###################################
#           recorrerlo     {}     #
###################################
print("############recorrido diccionario###############")
for key in canasta1:
    print(key)
print("###########################")
#Tuplas
###################################
#           Definición            #
###################################
tiempos=(5,3,4)
t=(1,)
print("Tipo:",type(t))
##################################
print("Tupla:",tiempos[1])


#Conjuntos(Set)
###################################
#           Definición            #
###################################
lista=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print("Ejemplo de uso set:", set(lista))

#String
###################################
#           Definición            #
###################################
palabra= "hola mundo!"
palindromo="Reconocer"
print("String:",palabra[0])
print("String:",palabra[:3])
print("String:",palabra[3:])
print("String:",palabra[-1])
print("String:",palabra[::2])
print("String:",palabra[::-1])
print("String:",palindromo[::-1])

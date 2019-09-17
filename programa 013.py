#Comparacion entre listas

def cmp (a,b):
    return (a>b)-(a<b) #Regresa un valor numerico

lista1=[100,"Hola"]
lista2=[30,"Bye"]

prueba=cmp(lista1,lista2)

#Obtencion del valor maximo y minimo de una lista
lista3=[50,70,23,57,90,10,-45.5,23,23,23]
maximo=max(lista3)
minimo=min(lista3)

#Conteo de un elemento en la misma lista
print (lista3.count(200))

#Indice de la primera aparicion de una variable
print (lista3.index(-45.5))

#Agregar mas elementos a la listas
lista1.extend(["Pedro",2,3,"Juan"])

"""
Operacion de pop en python, extrae el elemento y 
se elmina de la lista
"""

print (lista1)
Prueba2=(lista1.pop(2))
print (Prueba2)
print (lista1)

#Hacer reversa
lista1.reverse()
print(lista1)

#Ordenar lista
lista3.sort()

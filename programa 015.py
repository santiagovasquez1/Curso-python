# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:04:46 2019

@author: santi
"""

#Estructura de datos asociativa no sequencial
#Las llaves deben de ser inmutables(no es posible modificar), si se puede modificar el valor de la llave
#Un solor valor por datos

#Creacion del diccionario
productos={"ft01":"manzana","ft02":"pera","ft03":"Platano"} #Se guarda una dupla asi: llave:valor,
prueba=""
print (productos["ft02"])
print (productos)


for n in productos: #Recorre cada una de las llaves
    prueba+=n+" "+productos[n] +"\n"
    
print (prueba)

#Actualizar entrada
productos["ft02"]=8

#Adicion
productos["ft04"]=91

#Convertir dicc a cadena
cadena=str(productos)
cadena2="->"+cadena+"<-"
print(cadena2)

#Conocer si la llave existe
prueba= "ft05" in productos

if prueba == False:
    productos["ft05"]=40
else:
     productos["ft05"]=20
     
print (productos["ft05"])

#Lista de objetos en el diccionario
print(productos.items())

#Lista de llaves y valores
print (productos.keys)
print(productos.values())

#Setdefaultm se usa como get, pero damos un valor a colocar
#Default si la llave no existe

print(productos.setdefault("ft02","No hay")) #Verifica si un valor existe, si este no existe agrega el par al diccionario, si existe no pasa nada
print (productos.setdefault("ft06","Algo"))

#Otra forma de adicionar una entrada con update
productos.update({"ft07":45,"ft08":"Banano"}) #Puede agregar rangos de pares

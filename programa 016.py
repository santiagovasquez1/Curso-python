# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:43:33 2019

@author: santi
"""

#Conjuntos -Sets
#Es una coleccion no ordenada de objetos unicos e inmutables 
#Son similares a los conjuntos en matematicas

#Creacion de conjuntos usando set

letras=set("Hola a todos")
print (letras)

meses=set(["Enero","Febrero","Marzo"]) #Coleccion no ordenada de objetos
print (meses)

#No pueden obtener objetos mutables

#Adicion de elementos
meses.add("Abril")
print(meses)

nuevo=letras.union(meses)
print (nuevo)

#Frozen set, crea un conjunto inmutable
dias=frozenset(["Lunes","Martes","Miercoles"])
print(dias)
#dias.add("Jueves")

#Operaciones con sets
#Creacion con llaves

colores={"rojo","verde","Azul"}
print(type(colores))

#Creacion de copia
mascolores=colores.copy()
print(mascolores)

#Remover todos los elementos
mascolores.clear() #Conjunto vacio
print(mascolores)

#Eliminacion del objeto
del mascolores

#Opercaiones de conjuntos

a={1,2,3,4,5,6}
b={1,3,5}
c=a.difference(b)
d=b.difference(a)
e=a.union(b)
f={10,11,12}
print(c,d,e)
print("-"*20)

#Diference update, actualiza el conjunto sin necesidad de almacenarlo en otra variable
e.difference_update(d)

print(c,d,e)
print("-"*20)

#Uso del discard
b.discard(3)
b.discard(9)

print(b)
print (a.intersection(d)) #Elementos comunes entre dos conjuntos
print (a.isdisjoint(e)) #False, ya que poseen elementos en comun
print (a.isdisjoint(f)) #True, ya que no poseen elementos en 

print("-"*20)

print(b.issubset(a)) #Saber si un conjunto es subconjunto de otro

#SuperSet
print (a.issuperset(b))
print (b<a) #Subcojunto propio
print (a<a)

s={1,2,3,4,5,6,7,8,9,10,11,12}
print (s>a) #Supercojunto de a 

#Uso del popm obtiene y remueve un elemento
prueba=s.pop()


#d.remove(9) , marca un error al no encontrar el elemento dentro del conjunto
 
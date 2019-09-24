# -*- coding: utf-8 -*-
"""
Created on Sep 23 

@author: santi
"""

#Uso de variables locales y globales dentro de python

g=5 #Variable global

def funcion (mensaje):
    local=3 #Variable local, unicamente conocida en la seccion
    print(mensaje*3)
    print (local)
    print('-'*g)

#Paso por copia con objeto inmutable
def mostrar(a):
    print ("Id objeto",id(a),"Valor del objeto ",a)
    a=100
    print ("Id objeto",id(a),"Valor del objeto ",a)

funcion('hola')
print (g)

numero=5
print ("Antes ",numero)
mostrar(5)
print ("Desde fuera ",numero)
print ('-'*100)

#Paso por referencia con objeto mutable

def mostrar_lista(lista):
    print ("Id objeto",id(lista),"Valor del objeto ",lista)
    lista=["Hola"," a todos"]
    print ("Id objeto",id(lista),"Valor del objeto ",lista)

def mostrar_lista2(lista):
    print ("Id objeto",id(lista),"Valor del objeto ",lista)
    lista+=["Hola"," a todos"] #Concatenacion de la lista
    print ("Id objeto",id(lista),"Valor del objeto ",lista)

palabras=["pizza","auto","programacion"]
print ("Antes",palabras)
mostrar_lista(palabras)
print("Desde afuera ",palabras)

print ("== Ahora actua como referencia")
print ("Antes",palabras)
mostrar_lista2(palabras)
print("Desde afuera ",palabras)

print ('-'*100)
palabras=["pizza","auto","programacion"]
print ("== Ahora actua como referencia pero con copia superficial")
print ("Antes",palabras,id(palabras))
mostrar_lista2(palabras[:])
print("Desde afuera ",palabras,id(palabras))
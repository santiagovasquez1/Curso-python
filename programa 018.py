# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:37:45 2019

@author: santi
"""

#Definicion de funciones

def mostrar(numero): #Variable de entrada
    "Esta funcion imprime el numero" #Dockstring opcional, descripcion de la funcion
    print (numero)
    
def adicionar(nombre):
    nombre="Hola "+nombre
    print(nombre)

#Uso de return     
def suma(a,b):
    r=a+b
    return r
  
def multi(a,b=3): #b es un parametro opcional, que se debe de inicializar
    r=a*b
    print (r)    

def muestra(a=1,b=2,c=3):
    print ("A es ", a)
    print ("B es ", b)
    print ("C es ", c)

#Funciones con numero arbitrarios de parametros
def sumatoria(a,*mas): #Cuando un parametro posee un arteriscom queire decir que puede tener n paramatros
    sum=a
    if len(mas)>0:
        for n in mas:
            sum+=n
    print(sum)
    
#Codigo del programa
mostrar(1)
mostrar(2)
mostrar(3)
print(mostrar.__doc__)

adicionar("Shago")
suma(100,2)

multi(5)
multi(4,8)

#Uso de los keywords
print (muestra(b=6,a=8,c=20)) #No importa el orden de como se entran las variables a la funcion
print (muestra(b=20))

sumatoria(5)
sumatoria(5,3,1)
sumatoria(1,2,3,4,5)

s=suma(9,2)
print(s)

print ('-'*20)

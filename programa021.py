#Importamos el modulo re
#Trabajo con cadenas en python

import re

a=re.search("casa","La casa del casamentero") #Nos indica si encuentra la palabra o el caracter
print(a)

#implementacion de search

def Encontrar_palabra(texto1,texto2,Valor_exacto):

    if Valor_exacto==True:
        texto1=" "+ texto1+" " #Se agrega espacios al inicio y al final para encontrar la palabra exacta
    if re.search(texto1,texto2):
        print ("Se encontro la palabra en la oracion")
    else:
        print ("No se encuentra la palabra en la oracion")

Encontrar_palabra("casa","El estudiante es un casanova",False)
Encontrar_palabra("casa","El estudiante es un casanova",True)
Encontrar_palabra("casa","La casa del casanova",True)

#Uso del espacio+.+expresion Palabras que inician
 
if re.search(" ca.","Saludos al mas cabal"): #Palabras que inician
    print ("Hay palabra que inicia con ca")
else:
    print ("No hay palabra que inicie con ca")

#Uso de clases de caracteres, se usa [] para contener los caracteres
#Uso de alteraciones ejemplo re.search ("c|java|python","Python")

if re.search("N[ie]c","Hola Nico"): #Busca un caracter u otro
    print("Se encontro")
else:
    print ("No se encontro")

if re.search("N[ie]c","Hola NSico"):
    print("Se encontro")
else:
    print ("No se encontro")

#Busqueda de un rango de palabras

if re.search("N[a-u]c","Hola Ndco"):
    print ("Se encontro") #Busca los caracteres desde la a a la u
else:
    print ("No se encontro")

#Uso de complemento ^

if re.search("N[^ie]c","Hola Nico"): #Busca los caracteres diferentes de i o e
    print ("Se encontro")
else:
    print ("No se encontro")

#Uso del match para saber si una cadena inicia con una expresion
if re.match("N[ie]c","De youtube nicosiorede es mi canal favorito"):
    print ("Inicia")
else:
    print ("No incia")

if re.match("N[ie]c","Nicosiorede es mi canal favorito"):
    print ("Inicia")
else:
    print ("No incia")

#Para saber si una cadena finaliza con una expresion, se usa $
#Uso de elemento no opcional se usa caracter1? puede o no puede existir
#El manejo del split es igual que en c#

#Cuantificador
#Buscar que existan dos digitos

if re.search("[0-9]{2}","Hola 45 nico"):
    print ("Se encontro")
else:
    print("No se encontro")

if re.search("[0-9]{2}","Hola nico 21"):
    print ("Se encontro")
else:
    print("No se encontro")

if re.search("n{2}","Hola santi"):
    print ("Se encontro")
else:
    print("No se encontro")

if re.search("n {2}","Hola santi el n"):
    print ("Se encontro")
else:
    print("No se encontro")

prueba=re.findall("[nu]","nuevo santi nico") #Devuelve una lista con los caracteres
print (len (prueba))

#Reemplazo de caracteres

mensaje="Yo hablo ingles y no soy ingles"
sust=re.sub("ingles","español",mensaje) 

print (mensaje," || ", sust)

#Metodos utiles
#capitalize, vuelve el primer caracte en mayuscula
#Center, centrar un palbra dentro de unos caracteres que nosotros queramos, util para escribir encabezados

#Reconocer cadendas
texto="345a"
print(texto.isalnum()) #Alphanumerico
print(texto.isalpha()) #Solo alpha
print (texto.isdigit()) #Solo numero
#Uso de lista en python, estructura de datos fundamentales en python
#Posee propiedades polimorficas

#Creacion de listas

frutas=["Pera","Manzana","Ciruela","Platano"]
califs=[8,7,10,9,8]
varios=["internet",14.5,"Estrella",5,True]

#Acceder a las listas por indices

print (frutas[0])
print (frutas[-3]) #Uso de indice negativo para recorrer la lista de derecha a izquierda

#Borrado del elemento
 
del frutas[2] #Borro elemento de frutas en la pos 2
print (frutas[2])

frutas.append("Mango") #Añadir elemento a una lista
frutas.insert(3,"Maracuya") #Inserta un elemento en una determinada pos
print (frutas)


#Operaciones y funciones sobre las listas

#Longitud de lista
print (len (frutas))
print ("--"*20)

#Concatenacion de lista
lista2=califs+varios

for elemento in lista2:
    print (elemento)
    
print ("--"*20)

#Membresia, indica si un elemento existe en la lista
print (7 in lista2)
print ("manzana" in lista2)
print ("--"*20)

#Repeticion de listas
lista3=frutas*2
print(lista3)

#Slicing, recortar lista y obtener una sublista

lista4=lista2[3:9]
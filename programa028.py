#Serializacion
#Tres protocolos, 0-ascii, 1-compacto, 2-clases optimizadas 

import pickle

#Objeto a serializar
lista1=[5,"Hola"]
lista2=[7.8,"Python",True]

#Abrimos para escritura
archivo=open("misdatos.datos","wb")

#Serializamos
pickle.dump(lista1,archivo,2)
pickle.dump(lista2,archivo,2)


#Cerramos
archivo.close

#Deserializacion
archivo=open("misdatos.datos","rb")
list1=pickle.load(archivo)
list2=pickle.load(archivo)

print (list1)
print(list2)

archivo.close


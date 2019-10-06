archivo=open("mitexto.txt","w")

#Recorrer el arrchivo linea por linea
"""
for linea in archivo:
    print(linea.rstrip())
"""


#Info acerca del archivo
print ("Nombre " ,archivo.name)
print ("Estado " ,archivo.close)
print ("Modo apertura", archivo.mode)

n=0
while n<5:
    texto=input("Dame un texto")
    archivo.write(texto+"\n")
    n+=1
    
archivo.close()
print("-"*20)


#Abrir archivo a una lista
lista=open("mitexto.txt","r").readlines()
print(lista)

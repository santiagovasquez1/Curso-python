Valor=5
print Valor

precio=18.5
print precio

#Lo definimos con un constructor
saldo=float(14)
print  saldo

total=precio+saldo
print total

#Variables de tip string

nombre="Shago"
print nombre

#Tipo bool
acierto=True
print acierto

#Se pueden hacer asignaciones multiples
calif1,calif2=float(8),float(14)
print calif1
print calif2

#Diferentes formas de usar print en python
print "-"*20

#Tipo 1
print "El alumno tiene la calif de ", calif1, " y el dos de  ", calif2
print "-"*20

#Uso de formateadores: Sirve para indicar el lugar de la variable en la cadena
# %d : imprime en enteros
#%f: Imprime floats
#%s: imprime cadenas
#%r: imprimir el cotenido de una variable en formato raw (crudo), no importa el tipo de variable

print "El primer alumno tiene la calif de  %.0f y el segundo de %.0f" %(calif1,calif2)
print "-"*20
print "%s el precio es de %.2f por articulo " %(nombre,precio)
print "-"*20

#Creacion de cadena con fomato
formato="Una variable %r, otra variable %r"
print formato %(precio,saldo)
print formato %(nombre,acierto)
print formato %(total,calif1)
print "-"*20

#impresion de varias lineas al tiempo

print """
Aqui vamos a imprimir multiples lineas
a la vez.
Python lo permite
"""

# Python tambien tiene codigos de escape "Buscar en documentacion de python"
print "Voy a imprimit una \\ aqui"
print "\t Con salto de tab" 
print "Una linea \nOtra linea"

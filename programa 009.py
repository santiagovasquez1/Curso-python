#Uso de operadores logicos
"""
a=float(raw_input("Ingresa el numero "))

if a>=5 and a<=10:
    print a, " esta entre 5 y 10"

b=float(raw_input("Ingresa el numero "))
if b==1 or b==2 or b==4 or b==8:
    print "Correcto"
else:
    print "Incorrecto"

if not(b==1):
    print "El uno divide a todos exactamente"

print "-"*20
"""

#Uso de is, compara las instacias no los valores
"""
a=["Shago","Juan","Pedro"]
nombre =str(raw_input("Ingresa el nombre "))

if nombre in a:
    print "Conozco el nombre"
else:
    print "No Conozco el nombre"

print "-"*20
"""

#Comparacion entre listas

a=[2,3,5]
b=[2,3,3]
c=a

if a==b:
    print "a y b tienen el mismo valor"
else:
    print " a y b no son la mismo"
if a is b:
    print "a y b son la misma instacia"
else:
    print "a y b no son la mismo"

if c is a:
    print "a y c son la misma instacia"
else:
    print "a y c no son lo mismo"

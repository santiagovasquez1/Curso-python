#Uso de modulos de python, conceptualmente es similar a las librerias en C#

print ('-'*20)
print ("Has importado el modulo del curso basico")
x=100
print ("En el modulo x= ",x)
print ('-'*20)

def suma(a,b):
    r=a+b
    return r

def resta(a,b):
    r=a-b
    return r

def multi(a,b=3): #b es un parametro opcional, que se debe de inicializar
    r=a*b
    return r

def div(a,b=1):
    r=a/b
    return r

def imprimir():
    print("X desde el modulo",x)
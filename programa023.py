def cuadrado(a):
    r=0

    def par(x):
        return x%2==0

    if par(a):
        print ("Se puede hacer cuadrados")
        r=a*a

    else:
        print ("No se puede hacer el cuadrado")
        r=0

    return r
            

def parImpar(a):
    if (a%2==0):
        print("par")
    else:
        print("Impar")

def imprimemucho(a):
    valor=str(a)
    print((valor+"-")*a)

def potencia(func,x): #Funcion como parametro de otra funcion
    r=x**x
    func(r)
    print("La potencia es ",r)

#Las funciones tambien pueden regresar funciones

def f(x):
    def g(y):
        print("Estoy en g, este es x: ",x," este es y: ",y)
        return x+y

    print("Estoy en f, este es x: ",x)
    return g

##potencia2=cuadrado #Nombre que hace referencia a la instancia de la funcion

#Definimos la funcion decorada

def miDecorador(func):
    #Defiinoms la funcion que envuelve
    def decorador(a):
        print("Antes de llamar al decorador")
        print ("Her recibido a: ".a)
        func(a)
        #Regeresamos de la ejecucion del decorado 
        print ("Ya regrese de la ejecucion del decorador")

#Decoramos la funcion
@miDecorador
def mifuncion(x):
    print("Estoy en mi funcion con x: ",x)

#print(cuadrado(16))
##print (potencia2(105))

potencia(parImpar,5)
potencia(imprimemucho,4)

nf1=f(1)
nf2=f(3)

print (nf1(5))
print (nf2(7))

print ("-"*20)

#Invocamos la funcion
mifuncion(nf1)
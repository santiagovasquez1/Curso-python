#Uso de clases en python

#Definicion de clases

class Persona:
    "Esta es la clase de ejemplo en python" #Doc string

    #Variable de clase
    cantidad=0; #Se puede modificar desde cualquier instancia

    #Atributo publico
    valor=0

    #Atributo privado, no coincidir con ningun metodo reservado
    __dato=20

    #Creamos funciones de interfaz para el atributo privado __dato
    def get_dato(self):
        return self.__dato
    def set_dato(self,pDato):
        self.__dato=pDato

    #Creacion de propiedades para nombre
    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,pDato):
        self.__Nombre=pDato

    #Definicion de un constructor de la clase
    def __init__(self, nombre,edad):
        print("Estamos en _init_")
        self.Nombre=nombre
        self.Edad=edad

    #Definicion de un metodo
    def muestra(self):
        print("Mi nombre es: ",self.Nombre)
        print("Mi edad es: ",self.Edad)
        print ("El valor guardado es :",self.valor)
        print ("El dato es: ",self.__dato)
        print("La cantidad es: ",Persona.cantidad)
    
    def muestra_Saludo(self):
        print ("Hola soy: ",self.Nombre)

    #Metodo para modificar la cantidad
    def ponCantidad(self,cant):
        Persona.cantidad=cant

    #Metodos estaticos en python
    @staticmethod
    def mensaje(msg):
        print ("Tienes un mensaje: ",msg)

    #Metodos de clases
    #Se usan cuando no son especificios en una instancia en particular
    @classmethod
    def autor(cls):
        print("La clase",cls.__name__)
        print("Fue creado por shago")
    

#Uso de herencia en pyton
class Empleado(Persona):

    #Atributo propio
    sueldo=0

    #Override a un metodo
    def __init__(self, nombre,edad,salario):
        print("Estamos en _init_")
        self.Nombre=nombre
        self.Edad=edad
        self.sueldo=salario

    #Metodo que aprovecha el metodo de la clase padre
    def muestra_empleado(self):
        Persona.muestra(self)
        print("El sueldo es: ",self.sueldo)

    #Override a un metodo
    def muestra_Saludo(self):
        print("Hola tengo trabajo",self.Nombre)

#Uso de la clase dentro de un programa

persona1=Persona("Shago",27)
persona2=Persona("Ana",20)

persona1.set_dato(67)
#Invocacion de un metodo
persona1.muestra()
print ("-"*20)
persona2.muestra()

print ("-"*20)
persona1.ponCantidad(100) #Modifica la cantidad en cada una de las instancias

print ("-"*20)
persona1.muestra()

#Hacemos uso de las propiedades
p=persona1
p.Nombre="Victor"
print (p.Nombre)
p.muestra()


#Uso de los metodos
Persona.mensaje("Saludes a todos")
Persona.autor()
Empleado.autor()
"""
print ("-"*20)
persona2.muestra()

#Uso de la herencia
print ("-"*20)
Empleado1=Empleado("Juan",25,5*10**6)
Empleado1.muestra_empleado()
Empleado1.muestra_Saludo()

persona1.mensaje("Cabron")

#Manejo de atributos privados, se debe de hacer mediante una interfaz
persona1.__dato=3
print ("Intento imprimir dato",persona1.__dato)
print ("-"*20)
"""

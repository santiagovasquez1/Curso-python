class Persona(object):
    "Esta es la clase de ejemplo en python" #Doc string

    #El uso del mecanismo slots impide que se creen atributos dinamicos
    __slots__=("Nombre","Edad")

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

    """
    #Creacion de propiedades para nombre
    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,pDato):
        self.__Nombre=pDato
    """

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


#Programa
Persona1=Persona("Shago",27)
Persona1.ponCantidad(14)
Persona1.muestra()

#Creamos un atributo dinamico
Persona1.peso=60 
print (Persona1.peso)
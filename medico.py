import random

class Medico:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    direccion = ""
    rfc = ""
    
    def __init__(self, nombre, ano_nacimiento, direccion, rfc):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.direccion = direccion
        self.rfc = rfc
        
    def mostrar_informacion(self):
        print("ID: ",  self.id)
        print("Nombre: ",  self.nombre)
        print("Año de Nacimiento: ", self.ano_nacimiento)
        print("Direccion: ",  self.direccion)
        print("RFC: ",  self.rfc)
        
    # Getters regresan el valor de los atributos
    # @property
    # def  id(self):
    #     return self.id
    
    # @property
    # def  nombre(self):
    #     return self.nombre
    
    # @property
    # def  ano_nacimiento(self):
    #     return self.ano_nacimiento
    
    # @property
    # def  rfc(self):
    #     return self.rfc
        
    # @property
    # def  direccion(self):
    #     return self.direccion
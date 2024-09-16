import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("ID: ",  self.id)
        print("Nombre: ",  self.nombre)
        print(f"Año de Nacimiento: ", {self.ano_nacimiento})
        print(f"Peso: ",  {self.peso})
        print(f"Estatura: ",  {self.estatura})
        print(f"Direccion: ",  {self.direccion})
        
        
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
    # def  peso(self):
    #     return self.peso
    
    # @property
    # def  estatura(self):
    #     return self.estatura
    
    # @property
    # def  direccion(self):
    #     return self.direccion
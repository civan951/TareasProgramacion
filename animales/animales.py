from datetime import datetime
from typing import List
from enfermedades.enfermedades import Enfermedades

class Animal:
    id: str
    tipo_animal: str
    nombre: str
    especie: str
    fecha_llegada:datetime
    fecha_nacimiento_animal: datetime
    tipo_alimentacion: str
    frecuencia_alimentacio: str
    peso:float
    lista_enfermedades: List[Enfermedades] = []
    cuenta_vacunas:str
    
    #agregue el constructor
    def __init__ (self,id: str, tipo_animal: str, nombre: str, especie: str, fecha_llegada: datetime, fecha_nacimiento: datetime, tipo_alimentacion: str, frecuecia_alimentacion: str,  peso: float, lista_enfermedades: List[Enfermedades],  cuenta_vacunas: str):
        self.id = id
        self.tipo_animal = tipo_animal
        self.nombre = nombre
        self.especie = especie
        self.fecha_llegada = fecha_llegada
        self.fecha_nacimiento_animal = fecha_nacimiento
        self.tipo_alimentacion = tipo_alimentacion
        self.frecuencia_alimentacio = frecuecia_alimentacion
        self.peso = peso
        self.lista_enfermedades = lista_enfermedades
        self.cuenta_vacunas = cuenta_vacunas
        
        
    
    def mostrar_info(self):
        info = f"ID:{self.id}, Tipo: {self.tipo_animal}, Especie: {self.especie}, Nombre: {self.nombre}, Fecha de llegada: {self.fecha_llegada}, Alimentacion: {self.tipo_alimentacion}, Frecuencia de alimentacion: {self.frecuencia_alimentacio}, Peso: {self.peso}, Vacunas: {self.cuenta_vacunas}"
        return info
        
         

        
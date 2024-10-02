from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestres.semestre import Semestres
from random import randint

class Carrera:
    matricula: str
    nombre: str
    numero_semestre: int = 0
    semestres: List[Semestres] = []
    
    def __init__ (self, nombre: str):    
        self.matricula = self.generar_id(nombre)
        self.nombre = nombre
        
    def generar_id(self, nombre: str) -> str:
        return f"{nombre}-{randint(0,100000)}-{randint(0,100000)}"
    
    def registrar_semestre (self, semestre: Semestres):
        self.numero_semestre += 1
        self.semestres.append(semestre)
        
    def mostrar_info(self):
        print("Matricula: ", self.matricula)
        print("Nombre: ", self.nombre)
        print("Numero de Semestres: ", self.numero_semestre)
        print("\n")       
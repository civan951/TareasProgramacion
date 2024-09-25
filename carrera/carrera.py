from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestres.semestre import Semestres

class Carrera:
    matricula: str
    nombre: str
    numero_semestre: int
    semestres: List[Semestres] = []
    
    
    
    
    
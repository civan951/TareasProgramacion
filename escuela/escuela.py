from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
   lista_estudiantes: List[Estudiante] = []
   lista_grupos: List[Grupo] = []
   lista_maestros: List[Maestro] = []
   lista_materias: List[Materia] = []
   
   def registrar_estudiante(self, estudiante_regis: Estudiante):
      self.lista_estudiantes.append(estudiante_regis)
       
   def generar_numero_control(self):
       #L - 2024 - 09 - longitud +1 - random 0-10000
       #cadena formateada
       ano = datetime.now().year
       mes = datetime.now().month
       longitud_mas_uno = len(self.lista_estudiantes) + 1
       aleatorio = randint(0,10000)
       numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
       #numero_control = "L" + (datetime.year())str + (datetime.month())str + (len(self.lista_estudiantes) + 1)str + (randint(0,10000))str
       return numero_control
   
   def registrar_maestro(self, maestro_regis: Maestro):
      self.lista_maestros.append(maestro_regis)
   
   def generar_numero_control_maestros(self, año: int, nombre: str, rfc: str):
      ano = año
      dia = datetime.now().day
      aleatorio = randint(500, 5000)
      letras_inicio = nombre [:2].upper()
      letras_final = rfc [-2:].upper()
      longitud_mas_uno = len(self.lista_maestros) + 1
      
      numero_control = f"M{ano}{dia}{aleatorio}{letras_inicio}{letras_final}{longitud_mas_uno}"
      return numero_control
      
   def registrar_materia(self, materia_regis: Materia):
      self.lista_materias.append(materia_regis)
   
   def listar_estudiantes(self):
      print("***ESTUDIANTES***")
      
      for estudiante in self.lista_estudiantes:
         print(estudiante.mostrar_info_estudiante())
         
   def eliminar_estudiante(self, numero_eliminar: str):
      for estudiante in self.lista_estudiantes:
         if estudiante.numero_control == numero_eliminar :
            self.lista_estudiantes.remove(estudiante)
            print("Estudiante Eliminado")
            return
      print(f"No se encontro el estudiante con numero de control: {numero_eliminar}")
       
       
   def listar_maestros(self):
      print("**MAESTROS**")
      
      for maestro in self.lista_maestros:
         print(maestro.mostrar_info_maestro())
         
   def eliminar_maestro (self, numero_eliminar: str):
      for maestro in self.lista_maestros:
         if maestro.numero_control == numero_eliminar:
            self.lista_maestros.remove(maestro)
            print("Maestro eliminado")
            return
      print(f"No se encontro al maestro con numero de control: {numero_eliminar}")
      
   def listar_materias(self):
      print("**MATERIAS**")
      
      for materia in self.lista_materias:
         print(materia.mostrar_info_materia())
         
   def eliminar_materia(self, numero_eliminar: str):
      for materia in self.lista_materias:
         if materia.numero_control == numero_eliminar:
            self.lista_materias.remove(materia)
            print("Materia eliminada")
            return
      print(f"No se encontro la materia con numero de control: {numero_eliminar}")
         
   def generar_numero_control_materia(self, nombre:str, semestre: int, creditos: int):
      letras_final = nombre [-2:].upper()
      aleatorio = randint(1, 1000)
      
      numero_control = f"MT{letras_final}{semestre}{creditos}{aleatorio}"
      return numero_control
   
   
      
      
      
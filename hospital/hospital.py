from typing import List
from paciente.paciente import Paciente
from consulta.consultas import Consulta
from medico.medico import Medico

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []
    
    def registrar_consulta(self, id_paciente, id_medico):
        if self.validar_cantidad_usuarios() == False:
        #if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el medico o el paciente")
            return
        print("Continuamos con el registro")
    
        
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def eliminar_paciente(self, id):
        for paciente in self.pacientes:
            if paciente.id == id :
                self.pacientes.remove(paciente)
                return
        
        print("\nSe elimino el paciente")
        
    def registrar_medico(self,medico):
        self.medicos.append(medico)    
    
    def eliminar_medico (self,id):
        for medico in self.medicos:
            if medico.id == id :
                self.medicos.remove(medico)
                return
            
        print("\nSe elimino el Medico")
    
    def mostrar_pacientes(self):
        print("***Pacientes en el Sistema***")
        if len(self.pacientes) == 0:
            print("\nNo hay pacientes para mostrar")
            
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
            
    def mostrar_pacientes_menores_edad(self):
        print("***Pacientes Menores de Edad en el Sistema***")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) < 18: 
                paciente.mostrar_informacion()
                
    def mostrar_pacientes_mayores_edad(self):
        print("***Pacientes Mayores de Edad en el Sistema***")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) >= 18: 
                paciente.mostrar_informacion()
    
    def mostrar_medicos(self):
        print("***Medicos en el Sistema***")
        for medico in self.medicos:
            medico.mostrar_informacion()
    
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
       
        return False    
        
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
       
        return False    
        
        
    def validar_cantidad_usuarios(self):
        if (len(self.pacientes) == 0):
            print("No puedes registrar una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registrar una consulta, no existen medicos")
            return False
        
        return True
    
            
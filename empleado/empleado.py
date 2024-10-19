from .utils.roles import Rol
from datetime import datetime

class Empleado:
        nombre : str
        apellido : str
        fecha_nacimiento : datetime
        fecha_ingreso: datetime
        salario: float
        horario: str
        curp: str
        rol: Rol
        
        def __init__(self, nombre:str, apellido: str, fecha_nacimiento: datetime, fecha_ingreso: datetime, salario: float, horario: str, curp:str, rol: Rol):
            self.nombre = nombre
            self.apellido = apellido
            self.fecha_nacimiento = fecha_nacimiento
            self.fecha_ingreso = fecha_ingreso
            self.salario = salario
            self.horario = horario
            self.curp = curp
            self.rol = rol  
            
        
        
        def mostrar_info(self):
         info = f"Nombre: {self.nombre} {self.apellido}, Fecha De Nacimiento: {self.fecha_nacimiento}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario},Horario: {self.horario}, Curp: {self.curp}, Rol: {self.rol}"
         return info
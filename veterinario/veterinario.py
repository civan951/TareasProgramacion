from empleado.empleado import Empleado
from empleado.utils.roles import Rol
from datetime import datetime


class Veterinario(Empleado):
    
    
    def __init__(self, nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp):
        super().__init__(nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp, 
        rol = Rol.VETERINARIO)

    def mostrar_info(self):
        info = f"-Nombre: {self.nombre} {self.apellido}, Fecha Nacimiento: {self.fecha_nacimiento}, Fecha de Ingreso: {self.fecha_ingreso}, Salario: {self.salario}, Horario: {self.horario}, Curp: {self.curp}, Rol: {self.rol.value}"
        return info
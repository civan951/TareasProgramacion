from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

#Indica herencia 
class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime
    
    def __init__ (self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasena: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasena=contrasena, rol=Rol.ESTUDIANTE)
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n-Numero de control: {self.numero_control}, -Nombre Completo: {nombre_completo}, -Curp: {self.curp}, -Fecha de Nacimiento: {self.fecha_nacimiento}, -Rol: {self.rol.value}"
        return info
    
    
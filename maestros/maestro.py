from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    
    rfc: str
    sueldo: float
    
    def __init__ (self, numero_control, nombre: str, apellido: str, rfc: str, sueldo: float, contrasena: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasena=contrasena, rol=Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n-Numero de control: {self.numero_control}, -Nombre Completo: {nombre_completo}, -RFC: {self.rfc}, -Sueldo: {self.sueldo}, -Rol: {self.rol.value}"
        return info
    
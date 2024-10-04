from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    antiguedad: int
    
    def __init__ (self, sueldo:float, rfc: str, antiguedad: int, numero_control: str, nombre: str, apellido: str, contrasena: str, rol: Rol):
        super().__init__(numero_control=numero_control, 
                         nombre=nombre, 
                         apellido=apellido, 
                         contrasena=contrasena, 
                         rol= Rol.COORDINADOR.value)
        self.sueldo = sueldo
        self.rfc = rfc
        self.antiguedad = antiguedad
         
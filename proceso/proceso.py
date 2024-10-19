from empleado.empleado import Empleado
from empleado.utils.roles import Rol
from datetime import datetime

class Proceso:
    empleado: str
    id_animal: str
    proceso: str
    fecha: datetime
    observaciones: str
    
    def __init__(self, empleado: Empleado, id_animal:str, proceso: str, fecha: datetime, observaciones: str):
        self.empleado = empleado
        self.id_animal = id_animal
        self.fecha = fecha
        self.proceso = proceso
        self.observaciones = observaciones

    def mostrar_info_proceso(self):
        info = f"Empleado de mantenimiento: {self.empleado}, Id del animal: {self.id_animal}, Proceso: {self.proceso}, Observaciones: {self.observaciones}"
        return info
    
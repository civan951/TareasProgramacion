
class Enfermedades:
    nombre: str

    def __init__(self, nombre:str):
        self.nombre = nombre

    def mostrar_info(self):
        info = f"{self.nombre}"
        return info
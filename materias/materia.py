class Materia:
    
    numero_control: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__ (self, numero_control: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion 
        self.semestre = semestre
        self.creditos = creditos
        
    def mostrar_info_materia(self):
        info = f"-Numero de control: {self.numero_control} -Nombre: {self.nombre} -Descripcion: {self.descripcion} -Semestre: {self.semestre} -Creditos: {self.creditos}"
        return info
    
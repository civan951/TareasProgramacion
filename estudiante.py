class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    
    def __init__ (self, nombre, edad, id_estudiante):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        self.curso = []
        
    def agregar_curso(self, curso):
        self.curso.append(curso)
        
    def mostrar_info(self):
        print("\n------Datos del estudiante------\n")
        
        print("Nombre: ", self.nombre)
        print("id : ", self.id_estudiante)
        print("Cursos inscritos:")
        
        if len(self.curso) == 0:
                print("\nNo hay cursos para mostrar")
                return
           
        for curso in self.curso:
            print("\n")
            print("Nombre del curso: ", curso.nombre_curso)
            print("Codigo del curso: ", curso.codigo_curso)
            print("Instructor del curso: ", curso.instructor)
               
        
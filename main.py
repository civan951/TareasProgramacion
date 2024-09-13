from estudiante import Estudiante
from cursos import Cursos

estudiante_uno = Estudiante("Kevin", 20, 78979)
estudiante_dos = Estudiante("Ian", 20, 70423)

mecanismos = Cursos("Mecanismos", "ETC-987", "Jose Gerardo")
programacion = Cursos("Programacion", "IJK-465", "Eder Rivera")
dinamica = Cursos("Dinamica", "JNP-091", "Nicolas Ponciano")


estudiante_uno.agregar_curso(mecanismos)
estudiante_uno.agregar_curso(programacion)


estudiante_dos.agregar_curso(dinamica)
estudiante_dos.agregar_curso(programacion)



estudiante_uno.mostrar_info()
estudiante_dos.mostrar_info()

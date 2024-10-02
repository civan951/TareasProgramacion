from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from carrera.carrera import Carrera
from semestres.semestre import Semestres
from grupos.grupo import Grupo

escuela = Escuela()

while True:
    print("""
          -----**MINDBOX**-----
          1.- Registrar Estudiante
          2.- Registrar maestro
          3.- Registrar materia
          4.- Registrar grupo
          5.- Registrar horario
          6.- Mostrar estudiantes
          7.- Mostrar maestros 
          8.- Mostrar materia 
          9.- Mostrar grupos
          10.- Mostrar Carreras
          11.- Mostrar Semestres
          12.- Eliminar Estudiante
          13.- Eliminar Maestro 
          14.- Eliminar Materia 
          15.- Registrar Carrera
          16.- Registrar Semestre
          17.- Salir
          """)
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar un estudiante")
        
        numero_control = escuela.generar_numero_control()
        print ("Numero de Control: ", numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimieto = datetime(ano, mes, dia)
        
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimieto)
        escuela.registrar_estudiante(estudiante_regis=estudiante)
        
        print("Estudiante Registrado")
        
    elif opcion == "2":
        print("\nSeleccionaste la opcion para regitrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa la rfc del maestro: ")
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        numero_control = escuela.generar_numero_control_maestros(año=ano_nacimiento, nombre=nombre, rfc=rfc)
        print("Numero de control: ", numero_control)
        
        maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
        escuela.registrar_maestro(maestro_regis=maestro)
        
    elif opcion == "3":
        print("\nSeleccionaste la opcion de registrar materias")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripcion: ")
        semestre = int(input("Ingresa el semestre: "))
        creditos = int(input("Ingresa la cantidad de creditos: "))
        numero_control = escuela.generar_numero_control_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print("Numero de control: ", numero_control)
        
        materia = Materia(numero_control=numero_control, nombre=nombre, descripcion=descripcion, semestre=semestre, creditos=creditos)
        escuela.registrar_materia(materia_regis=materia)
    
    elif opcion == "4":
        print("\Seleccionaste la opcion para registrar grupo")
        
        tipo = input("Ingresa el tipo de grupo (A/B): ")
        id_semestre = input("Ingresa el id del semestre al que pertenece:")
        
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        
        escuela.registrar_grupo(grupo=grupo)
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        escuela.listar_estudiantes()
    
    elif opcion == "7":
        escuela.listar_maestros()
    
    elif opcion == "8":
        escuela.listar_materias()
    
    elif opcion == "9":
        escuela.listar_grupos()

    elif opcion == "10":
        escuela.listar_carreras()

    elif opcion == "11":
        escuela.listar_semestres()
    
    elif opcion == "12":
        print("\nSeleccionaste la opcion para eliminar un estudiante")
        
        numero_control = input("Ingresa el numero de control del estudiante:")
        escuela.eliminar_estudiante(numero_eliminar=numero_control)
        print("Estudiante eliminado")
    
    elif opcion == "13":
        print("\nSeleccionaste la opcion de eliminar maestro")
        
        numero_control = input("Ingresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_eliminar=numero_control)
        print("Maestro eliminado")
    
    elif opcion == "14":
        print("\nSeleccionaste la opcion de eliminar materias")
        
        numero_control = input("Ingresa el numero de control de la materia: ")
        escuela.eliminar_materia(numero_eliminar=numero_control)
        print("Se elimino la materia")
        
    elif opcion == "15":
        print("\nSeleccionaste la opcion de registrar carrera")
        
        nombre = input("Ingresa el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre)
        
        escuela.registrar_carrera(carrera=carrera)
        
    elif opcion == "16":
        print("\nSeleccionaste la opcion de registrar semestre")
        
        numero = input("Ingresa el numero del semestre: ")
        id_carrera = input("Ingresa el id de la carrera: ")
        
        semestre = Semestres(numero=numero, id_carrera=id_carrera)
        
        escuela.registrar_semestre(semestre=semestre)
        
    elif opcion == "17":
        print("\n Hasta luego")
        break
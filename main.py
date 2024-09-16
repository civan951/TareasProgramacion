"""
    -Pacientes
    -Medicos
    -Habitaciones
    -Consultas
    -Medicamentos    
"""

from paciente import Paciente
from hospital import Hospital
from medico import Medico

hospital = Hospital()

while True:
    print("""
          ***BIENVENIDO AL SISTEMA***
          Selecciona una opcion:
          
          1.- Registrar paciente
          2.- Registrar medico
          3.- Registrar consulta
          4.- Eliminar paciente
          5.- Eliminar medico
          6.- Mostrar pacientes
          7.- Mostrar pacientes menores de edad
          8.- Mostrar pacientes mayores de edad
          9.- Salir
          
          """)
    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del paciente: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del paciente: "))
        peso = float(input("Ingresa el peso del paciente: "))
        estatura = float(input("Ingresa la estatura del paciente: "))
        direccion = input("Ingresa la direccion del paciente: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado")
        
    elif opcion == "2":
        nombre = input("Ingresa el nombre del medico: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del medico: "))
        rfc = input("Ingresa el peso del medico: ")
        direccion = input("Ingresa la direccion del medico: ")
        
        medico = Medico(nombre = nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\nMedico regitrado")
        
    elif opcion == "3":
        pass
    
    elif opcion == "4":
        id = int(input("Ingresa el id del paciente a eliminar: "))
        hospital.eliminar_paciente(id)
        print("\nPaciente eliminado")
    
    elif opcion == "5":
        id = int(input("Ingresa el id del medico a eliminar: "))
        hospital.eliminar_medico(id=id)
        print("\nMedico eliminado")
       
    elif opcion == "6":
        hospital.mostrar_pacientes()
        
    elif opcion == "7":
        hospital.mostrar_pacientes_menores_edad()
        
    elif opcion == "8":
        hospital.mostrar_pacientes_mayores_edad()
        
    else:
        print("\nSalio del sistema")
        
        




# paciente = Paciente("Juan", 2018, 76, 1.78, "Av. Madero") #5
# paciente_dos = Paciente("Jonathan", 2004, 70, 1.90, "Av. Madero") #5
# hospital.registrar_paciente(paciente=paciente)
# hospital.registrar_paciente(paciente=paciente_dos)

# medico = Medico("Alberto", 1987, "Av. Periodismo", "AL897575465FFD" ) #8
# hospital.registrar_medico(medico=medico)


# hospital.mostrar_medicos()
# hospital.mostrar_pacientes()
# hospital.mostrar_pacientes_menores_edad()
# hospital.mostrar_pacientes_mayores_edad()

#hospital.registrar_consulta(id_paciente=1, id_medico=1)

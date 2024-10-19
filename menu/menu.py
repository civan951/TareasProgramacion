from datetime import datetime
from zoologico.zoologico import Zoologico
from visitantes.visitantes import Visitante
from veterinario.veterinario import Veterinario
from guia.guia import Guia
from mantenimiento.mantenimiento import Mantenimiento
from director.director import Director
from animales.animales import Animal
from enfermedades.enfermedades import Enfermedades
from proceso.proceso import Proceso

class Menu:

    zoologico: Zoologico = Zoologico()

    def login(self):
        intentos = 0
        while intentos < 5:
            print("""----BIENVENIDO----
                  Inicia sesion para continuar:
                  """)
            curp = input("Ingresa tu Curp del empleado: ")
            contrasena = input("Ingresa tu contraseña: ")
            
            user = self.zoologico.validar_incio_sesion(curp=curp, contrasena=contrasena)
            
            if user is None:
                intentos += 1
                print("Incorrecto, numero intentos ", intentos)
                if intentos == 5:
                    print("\nSISTEMA BLOQUEADO\n")
            else: 
                self.menu()


    def menu(self):

        while True:
            print("\nZOOLOGICO")
            print("1.- Registrar Veterinario")
            print("2.- Registrar Guia")
            print("3.- Registrar empleado de mantenimiento")
            print("4.- Registrar Director")
            print("5.- Registrar Visitante")
            print("6.- Registrar Visita")
            print("7.- Registrar Animal")
            print("8.- Registrar Proceso de Mantenimiento")
            print("9.- Mostrar Empleados")
            print("10.- Mostrar Visitantes")
            print("11.- Mostrar Animales")
            print("12.- Mostrar Visitas")
            print("13.- Mostrar Procesos de Mantenimiento")
            print("14.- Eliminar empleado")
            print("15.- Eliminar visitante")
            print("16.- Eliminar animal")
            print("17.- Modificar empleado")
            print("18.- Modificar visitante")
            print("19.- Modificar animal")
            print("20.- salir")

        #agregue opciones al menu

            opcion = input("\nElige una opcion: \n")

            if opcion == "1":
                print("Registrar Veterinario")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                veterinario = Veterinario(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(veterinario)


            if opcion == "2":
                print("Registrar Guía")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                guia = Guia(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(guia)


            if opcion == "3":
                print("Registrar Empleado de Mantenimiento")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apelllido: ")
                dia_nacimiento = int(input("Ingresa el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento,mes_nacimiento,dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                fecha_registro = datetime.now()       
                
                mantenimiento = Mantenimiento(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,fecha_ingreso=fecha_registro, salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(mantenimiento)
            
            if opcion == "4":
                print("Registrar Director")
                nombre = input("Ingresa el nombre: ")
                apellido = input("Ingresa el apellido: ")
                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
                fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                salario = float(input("Ingresa el salario: "))
                horario = input("Ingresa el horario: ")
                curp = input("Ingresa la curp: ")
                usuario = input("Ingresa el nombre de usuario: ")
                contrasena = input("Ingresa la contraseña: ")
                fecha_registro = datetime.now()       

                director = Director(usuario=usuario, contrasena=contrasena, nombre=nombre, apellido=apellido, 
                                    fecha_nacimiento=fecha_nacimiento, fecha_ingreso=fecha_registro, 
                                    salario=salario, horario=horario, curp=curp)
                self.zoologico.registrar_empleado(director)

                print("\nRegistrado correctamente")

            elif opcion == "5":
                zoologico: Zoologico = Zoologico()

                cantidad_visitante = int(input("Cuantas personas quieres registrar: \n"))
                for cantidad in range(cantidad_visitante):

                    print("Registrar Vistante NUMERO ", (cantidad+1), ": " )
                    
                    nombre_visitante= input("Ingresa Nombre del visitante: ")
                    apellido_visitante=input("Ingresa Apellido del visitante: ")
                    dia= int(input("Ingresa dia de nacimiento del visitante: "))
                    mes= int(input("Ingresa mes de nacimiento del visitante: "))
                    año= int(input("Ingresa mes de nacimiento año del visitante: "))
                    fecha_nacimiento_visitante=datetime(año, mes, dia)
                    curp_visitante=input("ingresa curp del visitante: ")
                    numero_visitas_visitante = 0
                    fecha_registro_visitante=datetime.now()

                    visitante = Visitante(nombre = nombre_visitante,
                                            apellido = apellido_visitante, 
                                            fecha_nacimiento= fecha_nacimiento_visitante, 
                                            curp=curp_visitante, 
                                            numero_visitas=numero_visitas_visitante, 
                                            fecha_registro=fecha_registro_visitante)
                    
                    self.zoologico.registrar_visitante(visitante)
                
            elif opcion == "6":
                
                zoologico: Zoologico = Zoologico
                
                print("Registrar Visita ")
                
                curp = input("ingresa curp del guia: ")
                self.zoologico.datos_visita(curp)
                
                
            elif opcion == "7":
                print("Registrar Animal")
                
                
                tipo = input("Ingrese el tipo: ")
                nombre = input("Ingrese el nombre: ")
                especie = input("Ingrese la especie: ")
                dia = int(input("Ingrese el dia de llegada: "))
                mes = int(input("Ingrese el mes de llegada: "))
                ano = int(input("Ingrese el año de llegada: "))
                fecha_llegada = datetime(ano,mes,dia)
                dia_nacimiento = int(input("Ingrese el dia de nacimiento: "))
                mes_nacimiento = int(input("Ingrese el mes de nacimietno: "))
                ano_nacimiento = int(input("Ingrese el año de nacimiento: ")) 
                fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
                alimentacion = input("Ingrese el tipo de alimentacion: ")
                frecuencia_alimentacion = input("Ingrese la frecuencia de la alimentacion: ")
                peso = float(input("Ingrese el peso en kg: "))
                #lista de enfermedades
                vacunas = input("Cuenta con vacunas: SI-NO: ")
                validar_enfermedades = input("Tiene enfermedades: SI-NO: ")
                
                self.zoologico.registrar_animal(tipo=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada, ano=ano_nacimiento, fecha_nacimiento=fecha_nacimiento, alimentacion=alimentacion, frecuencia_alimentacion=frecuencia_alimentacion, peso=peso, vacunas=vacunas, validar_enfermedades=validar_enfermedades)
                
                print("\nRegistrado correctamente")
                
            elif opcion == "8":
                print("\nRegistrar mantenimiento")
                validar_empleado_de_mantenimeinto = None
                while validar_empleado_de_mantenimeinto is None:
                    curp_empleado = input("Ingrese la curp del empleado: ")
                    validar_empleado_de_mantenimeinto = self.zoologico.buscar_empleado_mantenimeinto(curp_empleado)
                    if validar_empleado_de_mantenimeinto is None:
                        
                        print("Empleado no encontrado, intenta de nuevo")
                    else:
                        empleado = validar_empleado_de_mantenimeinto
                        break
                    
                validar_animal_mantenimeinto = None
                while validar_animal_mantenimeinto is None:
                    id_animal = input("Ingrese el id del animal: ")
                    validar_animal_mantenimeinto = self.zoologico.buscar_animal(id_animal)
                    if validar_animal_mantenimeinto is None:
                        print("Animal no encontrado, intenta de nuevo")
                    else:
                        break

                tipo_proceso = input("Ingrese el proceso a realizar: ")
                dia_proceso = int(input("Ingrese el dia del proceso: "))
                mes_proceso = int(input("Ingrese el mes del proceso: "))
                ano_proceso = int(input("Ingrese el año del proceso: "))
                fecha_proceso = datetime(ano_proceso, mes_proceso, dia_proceso)
                observaciones = input("Ingrese observaciones si las hay: ")
                
                proceso = Proceso(empleado=empleado, id_animal=id_animal, proceso=tipo_proceso, fecha=fecha_proceso, observaciones=observaciones)
                
                self.zoologico.registrar_proceso(proceso)
                
            elif opcion == "9":
                validacion = self.zoologico.validacion_empleados()
                if validacion is None:
                    print("No hay empleados registrados\n")
                else:
                    print("------EMPLEADOS-----")
                    self.zoologico.mostrar_empleados()
                
            elif opcion == "10":
                validacion = self.zoologico.validacion_visitantes()
                if validacion is None:
                    print("No hay visitantes registrados\n")
                else:
                    print("------VISITANTES------")
                    self.zoologico.mostrar_visitantes()
                
            elif opcion == "11":
                validacion = self.zoologico.validacion_animales()
                if validacion is None:
                    print("No se ha registrado un animal\n")
                else:
                    print("-----ANIMALES-----")
                    self.zoologico.mostrar_animales()

            elif opcion == "12":
                validacion = self.zoologico.validacion_visitas()
                if validacion is None:
                    print("No hay visitas registradas\n")
                else:
                    print("\nVisitas registradas")
                    self.zoologico.mostrar_visitas()

            elif opcion == "13": #mostrar proceso mantenimiento
                validacion = self.zoologico.validacion_animales()
                if validacion is None:
                    print("No hay procesos registradas\n")
                else:
                    print("\nProceso registradas")
                    self.zoologico.mostrar_procesos()
            
            elif opcion == "14":
                print("Eliminar empleado")
                curp = input("Ingresa curp del empleado a eliminar: ")
                self.zoologico.eliminar_empleado(curp=curp)

            elif opcion == "15":
                print("Eliminar visitante")
                curp = input("Ingresa curp del visitante a eliminar: ")
                self.zoologico.eliminar_visitante(curp=curp)

            elif opcion == "16":
                print("Eliminar animal")
                id = input("Ingresa Id del animal a eliminar: ")
                self.zoologico.eliminar_animal(id=id)
            
            elif opcion == "17":
                print("Modificar empleado")
                validacion = self.zoologico.validacion_empleados()
                if validacion is None:
                    print("No hay empleados registrados\n")
                else:
                    print("------EMPLEADOS-----")
                    self.zoologico.mostrar_empleados()
                    nueva_curp = input("Ingresa curp del empleado para modificar datos: ")
                    self.zoologico.modificar_empleado(curp= nueva_curp)
                
            
            elif opcion == "18":
                print("Modificar Visitante")
                validacion = self.zoologico.validacion_visitantes()
                if validacion is None:
                    print("No hay empleados registrados\n")
                else:
                    print("------EMPLEADOS-----")
                    self.zoologico.mostrar_visitantes()
                    nueva_curp = input("Ingresa curp del empleado para modificar datos: ")
                    self.zoologico.modificar_visitante(curp= nueva_curp)

            elif opcion == "19":
                print("Modificar Animales")
                validacion = self.zoologico.validacion_animales()
                if validacion is None:
                    print("No se ha registrado un animal\n")
                else:
                    print("-----ANIMALES-----")
                    self.zoologico.mostrar_animales()
                    nueva_curp = input("Ingresa Id del animal para modificar datos: ")
                    self.zoologico.modificar_animal(id = nueva_curp)

            elif opcion == "20":
                print("\nHasta luego...")
                break

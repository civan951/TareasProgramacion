from datetime  import datetime
from empleado.empleado import Empleado
from mantenimiento.mantenimiento import Mantenimiento
from visitantes.visitantes import Visitante
from visita.visita import Visita
from animales.animales import Animal
from typing import List
from empleado.utils.roles import Rol
from guia.guia import Guia
from veterinario.veterinario import Veterinario
from enfermedades.enfermedades import Enfermedades
from director.director import Director
from proceso.proceso import Proceso

class Zoologico:
    Lista_empleados: List[Empleado] = []
    Lista_visitantes: List[Visitante] = []
    Lista_visitas: List[Visita] = []
    lista_animales: List[Animal] = []
    lista_guiaas : List[Guia] = []
    Lista_visitantes_de_visita: List[Visitante] = []  
    Lista_enfermedades_animal: List[Enfermedades] = []
    Lista_proceso: List[Proceso] = [] 
     
    def __init__(self):
        
        director = Director(
            usuario= "Admin",
            contrasena=123, 
            nombre= "Admin",
            apellido= "uno",
            fecha_nacimiento= datetime(2000,9,7),
            fecha_ingreso= datetime.now(),
            horario= "8:00am - 8:00pm",
            curp= "ADMIN123",
            salario= 100.00
            #contrasena = "123"
        )
        self.Lista_empleados.append(director)
        
        empleado1 = Guia (
            nombre="Juan",
            apellido= "Alcaraz",
            fecha_nacimiento= datetime(1995,5,9),
            fecha_ingreso=datetime(2023,3,9),
            salario= 20.50,
            horario="7:30am-2:00pm",
            curp= "JAZ95",
            #rol=Rol.GUIA
            )
        self.Lista_empleados.append(empleado1)
        
        
        empleado2 = Veterinario (
            nombre="Daniel",
            apellido= "Guzman",
            fecha_nacimiento= datetime(1999,3,12),
            fecha_ingreso=datetime(2023,5,5),
            salario= 21.50,
            horario="2:00pm-7:00pm",
            curp= "DAG99",
            #rol=Rol.VETERINARIO
            )
        self.Lista_empleados.append(empleado2)
        
        empleado3 = Mantenimiento (
            nombre="Dennise",
            apellido= "Anchoa",
            fecha_nacimiento= datetime(1990,3,15),
            fecha_ingreso=datetime(2024,10,14),
            salario= 50.50,
            horario="7:30am-8:00pm",
            curp= "DEAN90",
            #rol=Rol.MANTENIMIENTO
            )
        self.Lista_empleados.append(empleado3)
    
        
        visitante1 = Visitante (
            nombre= "Carlos",
            apellido=  "Rubio",
            fecha_nacimiento = datetime (2004, 9, 7),
            curp = "CRA24",
            numero_visitas= 1,
            fecha_registro=datetime (2024,5,2)
            
            )
        
        self.Lista_visitantes.append(visitante1)
        
        visitante2 = Visitante(
            nombre= "Kevin",
            apellido=  "Garcia",
            fecha_nacimiento = datetime (2019, 12, 20),
            curp = "KGAR12",
            numero_visitas= 0,
            fecha_registro=datetime (2024,1,5)
            
        )
        
        self.Lista_visitantes.append(visitante2)
            
        
    def validar_incio_sesion(self, curp, contrasena):
            for empleado in self.Lista_empleados:
                if empleado.curp == curp:
                    if empleado.rol == Rol.DIRECTOR:
                        if contrasena == "123":
                                return empleado
            return None
    
    
    def registrar_empleado(self, empleado: Empleado):
        self.Lista_empleados.append(empleado)
        print("\nRegistrado correctamente")

    def registrar_visitante(self, visitante: Visitante):
        self.Lista_visitantes.append(visitante)
        print("\nRegistrado correctamente")
        
    def registrar_proceso(self,proceso):
        self.Lista_proceso.append(proceso)
        print("Proceso Registrado Correctamente")

    def mostrar_empleados(self):
        for empleado in self.Lista_empleados:
            print(empleado.mostrar_info())
        
    
    def mostrar_visitantes(self):
        for visitante in self.Lista_visitantes:
            print(visitante.mostrar_info())
            
    def mostrar_visitas(self):
        for visita in self.Lista_visitas:
            print(visita.mostrar_inform_visita())

            print("VISITANTES DE ESA VISITA")
            for visitante in visita.Lista_visitantes:
                print(visitante.mostrar_info())
            print("\n")

    def mostrar_procesos(self):
        for proceso in self.Lista_proceso:
            print(proceso.mostrar_info_proceso())
        print("\n")    
    
    def mostrar_animales(self):
        for animal in self.lista_animales:
            print(animal.mostrar_info())

            if not animal.lista_enfermedades:
                print("Este animal no tiene enfermedades")
            else:
                for enfermedad in animal.lista_enfermedades:
                    print("Enfermedad: ",enfermedad.mostrar_info())
                    
                
            print("\n")
            
    #agregue la funcion agregar animal 
    def registrar_animal(self, tipo,nombre,especie,fecha_llegada,ano,fecha_nacimiento,alimentacion,frecuencia_alimentacion, peso, vacunas, validar_enfermedades):
        ano_nacimiento = ano
        if validar_enfermedades == "SI":
            cantidad_enfermedades = int(input("Ingrese cantidad de enfermedades: "))
            for cantidad in range(cantidad_enfermedades):
                nombre_enfermedades = input("Ingrese nombre de enfermedades: ")
                enfermedades = Enfermedades(nombre= nombre_enfermedades)
                self.Lista_enfermedades_animal.append(enfermedades)
        else:
            #lista de enfermedades esta vacia
            print("animal sano")
            self.Lista_enfermedades_animal = []
        
        id_animal = self.generar_id(especie=especie, ano_nacimiento=ano_nacimiento)
        animal = Animal(id=id_animal, tipo_animal=tipo, nombre=nombre, especie=especie, fecha_llegada=fecha_llegada,
                        fecha_nacimiento=fecha_nacimiento, tipo_alimentacion=alimentacion, frecuecia_alimentacion=frecuencia_alimentacion, peso=peso,lista_enfermedades=self.Lista_enfermedades_animal, cuenta_vacunas=vacunas)
        self.lista_animales.append(animal)
        print("Se animal registrado correctamente ")
        #self.lista_animales.append(animal)
        self.Lista_enfermedades_animal=[]
            
    # def contador_visitas(self,curp):
    #     for visitante in self.Lista_vistantes:
    #         if curp == visitante.curp:
    #             visitante.numero_visitas +=1
    #         elif visitante.numero_visitas == 6:
    #             visitante.numero_visitas = 0 
   
    # def mostrar_numero_visitas(self):
    #     for visitante in self.Lista_vistantes:
    #         print(visitante.mostrar_numero_visitas())s

    def datos_visita(self,curp):
        # curp = input("ingresa curp del guia: ")
        for empleado in self.Lista_empleados:
            if curp == empleado.curp:
                if empleado.rol == Rol.GUIA:
                    nombre = empleado.nombre
                    apellido = empleado.apellido
                    fecha_nacimiento = empleado.fecha_nacimiento
                    fecha_ingreso = empleado.fecha_ingreso
                    salario = empleado.salario
                    horario = empleado.horario
                    curp = empleado.curp

                    guia = Guia(nombre, apellido, fecha_nacimiento, fecha_ingreso, salario, horario, curp)
                    guia_a_cargo = nombre
                        
                    numero_de_niños = 0
                    numero_de_adultos = 0
                    costo_boleto_adulto = 0
                    costo_boleto_niño = 0
                    costo_total = 0

                    cantidad_visitantes_en_visita = int(input("Ingresa la cantidad de los visitanes: ")) 


                    for cantidad in range(cantidad_visitantes_en_visita):
                        print("Ingresa curp del visitante numero", cantidad+1, ": ")
                        curp_visitantes = input("Curp: ")
                        for visitante in self.Lista_visitantes:
                            if curp_visitantes == visitante.curp:
                                nombre_visitante = visitante.nombre
                                apellido_visitante = visitante.apellido
                                fecha_nacimiento_visitante = visitante.fecha_nacimiento
                                curp_visitantes = visitante.curp
                                numero_visitas_visitante = visitante.numero_visitas
                                fecha_registro_visitante = visitante.fecha_registro
                                
                                visitante = Visitante(nombre=nombre_visitante, apellido = apellido_visitante, fecha_nacimiento = fecha_nacimiento_visitante, curp=curp_visitantes, numero_visitas=numero_visitas_visitante ,fecha_registro=fecha_registro_visitante)
                                #visita.Lista_visitantes.append(visitante)
                                self.Lista_visitantes_de_visita.append(visitante)
                                numero_visitas_visitante +=1

                                print("Visitante registrado NUMERO ", (cantidad+1),"\n" )
                                
                                año_visitante = fecha_nacimiento_visitante.year
                                
                                if año_visitante >= 2012: #comparacion de año 
                                    #visitante es niño
                                    numero_de_niños += 1
                                    costo_boleto_niño = 50
                                    
                                    if numero_visitas_visitante != 1 and (numero_visitas_visitante-1) % 5 == 0:
                                        costo_boleto_niño = numero_de_niños*costo_boleto_niño*0.8
                                        
                                    else:
                                        costo_boleto_niño = numero_de_niños*costo_boleto_niño
                                else:
                                    numero_de_adultos += 1
                                    costo_boleto_adulto= 100
                                    if (numero_visitas_visitante-1) % 5 == 0:
                                        costo_boleto_adulto = numero_de_adultos*costo_boleto_adulto*0.8
                                    else:
                                        costo_boleto_adulto = numero_de_adultos*costo_boleto_adulto
                                        
                                costo_total = costo_boleto_adulto+costo_boleto_niño
                                print("COSTO ADULTO: ", costo_boleto_adulto)      
                                print("COSTO NIÑO: ", costo_boleto_niño)      
                                print("COSTO TOTAL: ", costo_total)      
                                print("NIÑOS:", numero_de_niños)      
                                print("ADULTOS:", numero_de_adultos)      

                                fecha_visita = datetime.now()
                                visita = Visita(guia_acargo=guia_a_cargo, cantidad_niños=numero_de_niños, cantidad_adultos=numero_de_adultos, Lista_visitantes=self.Lista_visitantes_de_visita, costo_total= costo_total, fecha_visita=fecha_visita) 
                                #self.Lista_visitas.append(visita)
                                if (cantidad+1) == cantidad_visitantes_en_visita:
                                    self.Lista_visitas.append(visita)
                                    print("Visita registrada correctamente")
                                    self.Lista_visitantes_de_visita = []
                                    break
                            else:
                                print("Visitante no encontrado")
                                
                else:
                    print("Empleado no es guia")
                
        print("Saliendo del sistema")
    
    def generar_id(self, especie:str, ano_nacimiento: int):
        id = f"AN{especie[2:]}{ano_nacimiento}"
        return id
        
    def validacion_visitas(self):
        for visita in self.Lista_visitas:
            return visita
        return None    
    
    def validacion_empleados(self):
        for empleado in self.Lista_empleados:
            return empleado
        return None
    
    def validacion_procesos(self):
        for proceso in self.Lista_proceso:
            return proceso
        return None
    
    def buscar_empleado_mantenimeinto(self,curp_empleado):
        for empleado in self.Lista_empleados:
            if curp_empleado == empleado.curp:
                if empleado.rol == Rol.MANTENIMIENTO:
                    print("Empleado encontrado: ", empleado.nombre )
                    return empleado.nombre
        return None

    def buscar_animal(self,id_animal):
        for animal in self.lista_animales:
            if id_animal == animal.id:
                    print("Animal encontrado:", animal.nombre, animal.especie )
                    return animal
        return None 
    
            


    def validacion_visitantes(self):
        for visitante in self.Lista_visitantes:
            return visitante
        return None
    
    def validacion_animales(self):
        for animales in self.lista_animales:
            return animales
        return None
    
    def eliminar_empleado(self,curp):
        for empleado in self.Lista_empleados:
            if curp == empleado.curp:
                self.Lista_empleados.remove(empleado)
                print("Empleado eliminado:", empleado.nombre)
                return
        print("No se encuantra empleado")

    def eliminar_visitante(self, curp):
        for visitante in self.Lista_visitantes:
            if curp == visitante.curp:
                self.Lista_visitantes.remove(visitante)
                print("Visitante eliminado:", visitante.nombre)
                return
        print("No se ha encontrado visitante")
    
    def eliminar_animal(self, id):
        for animal in self.lista_animales:
            if id == animal.id:
                self.lista_animales.remove(animal)
                print("Animal eliminado:", animal.nombre,animal.especie)
                return
        print("No se ha encontrado animal")

#----------------
    def modificar_empleado(self, curp):
        for empleado in self.Lista_empleados:
            if curp == empleado.curp:
                print("Dato a reemplazar: ")
                print("1.- Salario")
                print("2.- Horario")
                print("3.- Curp")
                numero_dato = input("Ingresa numero: ")
                if numero_dato == "1":
                    dato_nuevo = float(input("Nuevo salario: "))
                    empleado.salario = dato_nuevo
                    return
                    
                elif numero_dato == "2":
                    dato_nuevo = input("Nuevo Horario: ")
                    empleado.horario = dato_nuevo
                    return
                
                elif numero_dato == "3":
                    dato_nuevo = input("Nueva curp: ")
                    empleado.curp = dato_nuevo
                    return
                else: 
                    print("No ingresaste opcion valida")
                    return

                # salario: float
                # horario: str
                # curp: str
        print("no se encontro empleado con esa curp")

    def modificar_visitante(self, curp):
        for visitante in self.Lista_visitantes:
            if curp == visitante.curp:
                print("Dato a reemplazar: ")
                print("1.- Nombre")
                print("2.- Apellido")
                print("3.- Curp")
                numero_dato = input("Ingresa numero: ")
                if numero_dato == "1":
                    dato_nuevo = input("Nuevo Nombre: ")
                    visitante.salario = dato_nuevo
                    return
                    
                elif numero_dato == "2":
                    dato_nuevo = input("Nuevo Apellido: ")
                    visitante.horario = dato_nuevo
                    return
                
                elif numero_dato == "3":
                    dato_nuevo = input("Nueva Curp: ")
                    visitante.curp = dato_nuevo
                    return
                else: 
                    print("No ingresaste opcion valida")
                    return
                # salario: float
                # horario: str
                # curp: str
        print("No se encontro visitante con esa curp")

    def modificar_animal(self, id):
        for animal in self.lista_animales:
            if id == animal.id:
                print("Dato a reemplazar: ")
                print("1.- Tipo ")
                print("2.- Nombre")
                print("3.- Id")
                print("4.- Tipo de alimentacion")
                print("5.- Frecuencia de alimentacion")
                print("6.- Peso")
                print("7.- Vacunas")
                # tipo_animal: str
                # id: str
                # nombre: str
                # especie: str
                # fecha_llegada:datetime
                # fecha_nacimiento_animal: datetime
                # tipo_alimentacion: str
                # frecuencia_alimentacio: str
                # peso:float
                # lista_enfermedades: List[Enfermedades] = []
                # cuenta_vacunas:str
                numero_dato = input("Ingresa numero: ")
                if numero_dato == "1":
                    dato_nuevo = input("Nuevo Tipo: ")
                    animal.tipo_animal = dato_nuevo
                    return
                    
                elif numero_dato == "2":
                    dato_nuevo = input("Nuevo Nombre: ")
                    animal.nombre = dato_nuevo
                    return
                
                elif numero_dato == "3":
                    dato_nuevo = input("Nueva Id: ")
                    animal.id = dato_nuevo
                    return
                
                elif numero_dato == "4":
                    dato_nuevo = input("Nueva Tipo de alimentacion: ")
                    animal.tipo_alimentacion = dato_nuevo
                    return
                
                elif numero_dato == "5":
                    dato_nuevo = input("Nueva Frecuencia de alimentacion: ")
                    animal.frecuencia_alimentacio = dato_nuevo
                    return
                
                elif numero_dato == "6":
                    dato_nuevo = float(input("Nueva : Peso"))
                    animal.peso = dato_nuevo
                    return
                elif numero_dato == "7":
                    dato_nuevo = input("Nueva Vacunas: ")
                    animal.cuenta_vacunas = dato_nuevo
                    return
                else: 
                    print("No ingresaste opcion valida")
                    return
                # salario: float
                # horario: str
                # curp: str
        print("No se encontro animal con ese Id")
        


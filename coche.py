class Coche:
    marca = ""
    modelo = ""
    año = 0
    
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    
    def mostrar_info(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
        
    def calcular_edad_coche(self):
       print("Edad del coche: ", 2024 - self.año, "años")
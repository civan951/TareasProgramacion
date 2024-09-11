class Circulo:
    radio = 0
    
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = 3.1416 * (self.radio*self.radio) 
        print("\nEl area es: ", area)
        
    def calcular_perimetro(self):
        perimetro = 2*3.1416*self.radio
        print("\nEl perimetro es: ", perimetro)
        
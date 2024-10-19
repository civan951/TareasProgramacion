from typing import List
from datetime import datetime
from visitantes.visitantes import Visitante


class Visita:
    guia_acargo:str #supongo que alguno de los empleads guia
    cantidad_niños: int #se puede calcular con fecha de nacimiento
    cantidad_adultos: int #se puede calcular con fecha de nacimiento
    Lista_visitantes: List[Visitante] = []
    costo_total:int
    fecha_visita: datetime


    def __init__(self, guia_acargo:str, cantidad_niños:int, cantidad_adultos:int, Lista_visitantes: List[Visitante], costo_total:int, fecha_visita:datetime):
        self.guia_acargo = guia_acargo
        self.cantidad_niños = cantidad_niños
        self.cantidad_adultos = cantidad_adultos
        self.Lista_visitantes = Lista_visitantes
        self.costo_total = costo_total
        self.fecha_visita = fecha_visita



    def mostrar_inform_visita(self):
        infor= f" \nGuia a cargo: {self.guia_acargo}, cantidad niños: {self.cantidad_niños}, cantidad_adultos: {self.cantidad_adultos}, Costo total de la visita: {self.costo_total}, fecha de la visita: {self.fecha_visita}"    
        return infor
    #podemos agregar un def para agregar visitantes a la lista de aqui, un def identico al de Zoologico





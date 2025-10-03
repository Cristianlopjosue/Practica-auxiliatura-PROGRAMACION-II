class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def Desplazarse():
        pass
class Leon(Animal):
    def Desplazarse(self):
        print("Camina")
class Pinguino(Animal):
    def Desplazarse(self):
        print("Nada")
class Canguro(Animal):
    def Desplazarse(self):
        print("Salta")

canguro=Canguro("Eduardo",23)
canguro.Desplazarse()
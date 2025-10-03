class Mascota:
    def __init__(self,nombre,tipo,energia):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__energia = energia
    def Alimentar(self):
        if self.__energia<100:
            self.__energia+=20
        elif self.__energia>=100:
            print("Tu mascota esta llena!!!")
    def Juegar(self):
        if self.__energia<=0:
            print("Su mascota esta cansada")
        elif self.__energia>=15:
            self.__energia-=15
    def __str__(self):
        return (f"Nombre: {self.__nombre}\nTipo: {self.__tipo}\nEnergia: {self.__energia}")
mascota1=Mascota("Anthony","Gato",10)
mascota2=Mascota("Mango","Cabra",60)
mascota2.Alimentar()
mascota2.Juegar()
mascota2.Juegar()
print(mascota2)
mascota1.Alimentar()
mascota1.Alimentar()
mascota1.Alimentar()
print(mascota1)
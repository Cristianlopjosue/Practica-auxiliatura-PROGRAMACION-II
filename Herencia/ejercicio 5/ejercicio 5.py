class Vehiculo:
    def __init__(self,conductor,Placa,id):
        self._conductor = conductor
        self._Placa = Placa
        self._id=id
    def setConductor(self,otro):
        self._conductor = otro
class Bus(Vehiculo):
    def __init__(self, conductor, Placa, id,capacidad,sindicato):
        super().__init__(conductor, Placa, id)
        self.__capacidad=capacidad
        self.__sindicato=sindicato
class Auto(Vehiculo):
    def __init__(self, conductor, Placa, id,Caballosfuerza,descapotable):
        super().__init__(conductor, Placa, id)
        self.__Caballosfuerza=Caballosfuerza
        self.__descapotable=descapotable
class Moto(Vehiculo):
    def __init__(self, conductor, Placa, id,cilindrada,casco):
        super().__init__(conductor, Placa, id)
        self.__cilindrada=cilindrada
        self.__casco=casco
moto=Moto("Juan",109075,1967,0.6,True)
bus=Bus("Jose",1985,128564,24,"San Luis")
auto=Auto("Pepe",10293932,28575,99,True)
auto.setConductor("Juan")
class nadador:
    def __init__(self,estilodenatacion):
        self.estilodenatacion=estilodenatacion
    def nadar(self):
        return print(f"Nadando estilo : {self.estilodenatacion}")
class Ciclista:
    def __init__(self,tipobicicleta):
        self.tipobicicleta=tipobicicleta
    def Pedalear(self):
        return print(f"Pedaleando en la bicicleta de tipo: {self.tipobicicleta}")
class Corredor:
    def __init__(self,distanciapreferida):
        self.distanciapreferida=distanciapreferida
    def Correr(self):
        return print(f"Corriendo una distancia de {self.distanciapreferida} km")
class triatleta(nadador,Ciclista,Corredor):
    def __init__(self, estilodenatacion,tipobicicleta,distanciapreferida):
        nadador.__init__(self,estilodenatacion)
        Ciclista.__init__(self,tipobicicleta)
        Corredor.__init__(self,distanciapreferida)

triatleta1=triatleta("Mariposa","7 cambios",780)
triatleta1.Correr()
triatleta1.nadar()
triatleta1.Pedalear()
        
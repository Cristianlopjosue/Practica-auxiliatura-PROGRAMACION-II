class Videojuego:
    def __init__(self, nombre="", plataforma="", jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores
    def agregarJugadores(self, cantidad=None):
        if cantidad is None:
            self.jugadores += 1
        else:
            self.jugadores += cantidad

v1 = Videojuego("FIFA 2025", "PC", 1)
v2 = Videojuego("Zelda", "Switch") 
v3 = Videojuego("Mario") 
v1.agregarJugadores()
v2.agregarJugadores(3)
v3.agregarJugadores()

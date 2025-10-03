class Mp4:
    def __init__(self, marca, capacidadGb):
        self.marca = marca
        self.capacidadGb = capacidadGb
        self.canciones = []  
        self.videos = []     
    def borrar_cancion(self, nombre="", artista="", peso=-1):
        nuevas = []
        for c in self.canciones:
            borrar = False
            if nombre != "" :
                if c[0] == nombre:
                    borrar = True
            if artista != "" :
                if c[1] == artista:
                    borrar = True
            if peso != -1 :
                if c[2] == peso:
                    borrar = True
            if borrar == False:
                nuevas.append(c)
        self.canciones = nuevas
    def add_cancion(self, cancion):
        existe = False
        for c in self.canciones:
            if c[0] == cancion[0]:
                if c[1] == cancion[1]:
                    existe = True
        if existe == False:
            self.canciones.append(cancion)
        else:
            print("La canción ya existe")
    def add_video(self, video):
        existe = False
        for v in self.videos:
            if v[0] == video[0]:
                if v[1] == video[1]:
                    existe = True
        if existe == False:
            self.videos.append(video)
        else:
            print("El video ya existe")
    def capacidad_disponible(self):
        total = 0
        for c in self.canciones:
            total += c[2]
        for v in self.videos:
            total += v[2]
        return self.capacidadGb - total
    def mostrar_canciones(self):
        for c in self.canciones:
            print(c)
    def mostrar_videos(self):
        for v in self.videos:
            print(v)


mp4 = Mp4("Sony", 1000)

mp4.add_cancion(["Sweet child of mine","Guns and roses",100])
mp4.add_cancion(["Fruto","Milo j",150])
mp4.add_video(["Remember the time","Michael jackson",50])
mp4.add_video(["Nino","Milo j",30])
mp4.borrar_cancion(nombre="Fruto")
print("Canciones:")
mp4.mostrar_canciones()
print("Videos:")
mp4.mostrar_videos()
print("Capacidad disponible:", mp4.capacidad_disponible())

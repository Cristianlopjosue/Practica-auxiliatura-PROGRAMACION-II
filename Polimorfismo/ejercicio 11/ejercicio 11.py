class Crucero:
    def __init__(self,nombre,paisOrigen,paisDestino,nroPasajeros,pasajeros):
        self.__nombre=nombre
        self.__paisOrigen=paisOrigen
        self.__paisDestino=paisDestino
        self.__nroPasajeros=nroPasajeros
        self.__pasajeros=pasajeros
    
    def __add__(self,otro):
        a=0
        for i in range (1,len(self.__pasajeros)+1):
            a=a+self.__pasajeros[2][i]+otro.__pasajeros[2][i]
        return (f"La suma de los pasajes seria de: {a}")
    
    def __sub__(self, otro):
        hombres = 0
        mujeres = 0
        for pasajero in self.__pasajeros:
            if pasajero[1].lower() == "hombre":
                hombres += 1
        for pasajero in self.__pasajeros:
            if pasajero[1].lower() == "mujer":
                mujeres += 1
        return f"Hombres: {hombres}, Mujeres: {mujeres}"
    
    def __eq__(self,otro):
        if (len(self.__pasajeros)==len(otro.__pasajeros)):
            return True
        else:
            return False
    
    def Comparar(self,otro):
        if self.__eq__(otro):
            return "Los cruceros tienen los mismos pasajeros"
        else:
            return "Los cruceros tienen distintos pasajeros"

class Pasajeros:
    def __init__(self,nombre,edad,genero):
        self.__nombre=nombre
        self.__edad=edad
        self.__genero=genero
    def __sub__(self,otro):
        return "a"

crucero1=Crucero("TITANIC","Bolivia","Estados Unidos",40,[["Nombre: ","Juan Vargas","Martina Vasques","Wilmer Montero"],["nroHabitacion","502","603","401"],["costoPasaje",500,1000,500]])
crucero2=Crucero("BOA LAGO TITICACA","Bolivia","Peru",40,[["Nombre: ","Julian","Pedro","Diego"],["nroHabitacion","505","898","781"],["costoPasaje",534,589,556]])
pasaje1=Pasajeros("Juan",14,"Mujer")
pasaje2=Pasajeros("Pepe",28,"Hombre")
pasaje3=Pasajeros("Juan",45,"Hombre")
pasaje4=Pasajeros("Tati",20,"Mujer")
pasaje5=Pasajeros("Amy",21,"Mujer")
v1= crucero1+crucero2
print(v1)
print(crucero1.Comparar(crucero2))
print(crucero1 - crucero2)
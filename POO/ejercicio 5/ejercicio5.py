class Persona:
    def __init__(self,nombre,paterno,materno,edad,ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
    def MostrarDatos(self):
        print(f"Nombre: {self.nombre}\nPaterno: {self.paterno}\nMaterno: {self.materno}\nEdad: {self.edad}\nCi: {self.ci}")
    def Mayordeedad(self):
        if self.edad>=18:
            print(f"Es mayor de edad tiene: {self.edad} de edad")
        else:
            print("Es menor de edad")
    def Modificaredad(self,otro):
        self.edad=otro
    def MismoApellido(self,otro):
        if self.paterno==otro:
            print(f"Tienen el mismo apellido")
            
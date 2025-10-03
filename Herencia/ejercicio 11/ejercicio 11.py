class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
class Empleado:
    def __init__(self,salario,horas):
        self.salario=salario
        self.Horas=horas
class Policia:
    def __init__(self,arma,rol):
        self.arma=arma
        self.rol=rol
class JefePolicia(Persona,Empleado,Policia):
    def __init__(self, nombre, edad,salario,Horas,arma,rol):
        Persona.__init__(self,nombre, edad)
        Empleado.__init__(self,salario,Horas)
        Policia.__init__(self,arma,rol)
    def __str__(self):
        return (f"Nombre: {self.nombre}\nEdad: {self.edad}\nSalario: {self.salario}\nHoras: {self.Horas}\nArma: {self.arma}\nRol: {self.rol}")
    def Mayor(self,otro):
        if (self.salario>otro.salario):
            return (f"{self.nombre} tiene el mayor salario")
        else:
            return (f"{otro.nombre} tiene mayor salario")        
jefe1 = JefePolicia("Juan Perez", 45, 5000, 40, "Pistola", "Comandante")
jefe2 = JefePolicia("Maria Lopez", 38, 4800, 35, "Rifle", "Subcomandante")
print(jefe1)
print(jefe1.Mayor(jefe2))
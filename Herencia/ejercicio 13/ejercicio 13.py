class Empleado:
    def __init__(self,nombre,sueldomes):
        self.nombre=nombre
        self.sueldomes=sueldomes
    def SueldoTotal(self):
        return self.sueldomes

class Administrativo(Empleado):
    def __init__(self, nombre, sueldomes,cargo):
        super().__init__(nombre, sueldomes)
        self.cargo=cargo
    def SueldoTotal(self):
        return self.sueldomes
class Chef(Empleado):
    def __init__(self, nombre, sueldomes,horasExtra,tipo,sueldoHora):
        super().__init__(nombre, sueldomes)
        self.horasExtra=horasExtra
        self.tipo=tipo
        self.sueldoHora=sueldoHora
    def SueldoTotal(self):
        return self.sueldomes + (self.horasExtra * self.sueldoHora)
class Mesero(Empleado):
    def __init__(self, nombre, sueldomes,propina,horasExtra,sueldoHora):
        super().__init__(nombre, sueldomes)
        self.horasExtra=horasExtra
        self.propina=propina
        self.sueldoHora=sueldoHora
    def Igual(self,otro1,otro2,x):
        if (self.sueldomes==x):
            return (f"ese sueldo lo tiene {self.nombre}")
        elif (otro1.sueldomes==x):
            return (f"ese sueldo lo tiene {otro1.nombre}")
        elif (otro2.sueldomes==x):
            return (f"ese sueldo lo tiene {otro2.nombre}")
    def SueldoTotal(self):
        return self.sueldomes + (self.horasExtra * self.sueldoHora) + self.propina
                
chef1 = Chef("Gordon Ramsay", 3000, 10, "Italiana", 50)
mesero1 = Mesero("Juan Perez", 1200, 150, 5, 15)
mesero2 = Mesero("Maria Lopez", 1300, 200, 6, 16)
admin1 = Administrativo("Carlos Gomez", 2000, "Gerente")
admin2 = Administrativo("Lucia Fernandez", 1800, "Contadora")
print(mesero1.Igual(chef1,mesero2,3000))
print("Sueldo total Chef:", chef1.SueldoTotal())
print("Sueldo total Mesero1:", mesero1.SueldoTotal())
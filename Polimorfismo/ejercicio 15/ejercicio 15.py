class Ordenador:
    def __init__(self,codigoserial,numero,Ram,procesador,estado):
        self.codigoserial=codigoserial
        self.numero=numero
        self.Ram=Ram
        self.procesador=procesador
        self.estado=estado
class Lasin:
    def __init__(self,nombre,cantidad,capacidaddeordenador,registro):
        self.nombre=nombre
        self.cantidad=cantidad
        self.capacidaddeordenador=capacidaddeordenador
        self.registro=registro
    def informacion(self, tipo="", valor=""):
        if tipo == "estado":
            for o in self.registro:
                if o.estado == valor:
                    print(o.codigoserial, o.Ram, o.procesador, o.estado)
        elif tipo == "laboratorio":
            if  self.nombre == valor:
                for o in self.registro:
                    print(o.codigoserial, o.Ram, o.procesador, o.estado)
        elif tipo == "Ram":
            for o in self.registro:
                if o.Ram > valor:
                    print(o.codigoserial, o.Ram, o.procesador, o.estado)
        else:
            for o in self.registro:
                print(o.codigoserial, o.Ram, o.procesador, o.estado)

ordenador1 = Ordenador(198767,1,16,"Intel i-5","Activo")
ordenador2 = Ordenador(191231,2,2,"Intel i-5","Desactivo")
ordenador3 = Ordenador(2987231,3,6,"Intel i-5","Activo")
ordenador4 = Ordenador(5698375,4,16,"Intel i-5","Activo")
ordenador5 = Ordenador(459275,5,5,"Intel i-5","Desactivo")
ordenador6 = Ordenador(4954831,6,32,"Intel i-5","Desactivo")
lasin1 = Lasin("Lasin 1", 4, 2, [ordenador1, ordenador2, ordenador3, ordenador4])
lasin2 = Lasin("Lasin 2", 6, 3, [ordenador5, ordenador6])
print("Ordenadores activos en Lasin 1:")
lasin1.informacion("estado", "Activo")
print("\nOrdenadores con RAM mayor a 8 en Lasin 1:")
lasin1.informacion("Ram", 8)
print("\nTodos los ordenadores en Lasin 2:")
lasin2.informacion()

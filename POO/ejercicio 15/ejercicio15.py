class Buzon:
    def __init__(self, nro, nroC, c):
        self.nro = nro
        self.nroC = nroC
        self.c = c  

class Carta:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

buzon = Buzon(1, 2, [
    ["Codigo","Remitente","Destinatario"],
    ["C123","Pepe Mujica","Peter Chaves"],
    ["C456","Pepe Mujica","Wilmer Pérez"],
    ["C789","Paty Vasques","Pepe Mujica"]
])

buzon2 = Buzon(2, 1, [
    ["Codigo","Remitente","Destinatario"],
    ["C777","Spiderman","Duende Verde"],
    ["C999","Juancito Pinto","Juan Perez"],
    ["C677","Pepe Sallez","Julian Alvarez"]
])

buzon3 = Buzon(3, 1, [
    ["Codigo","Remitente","Destinatario"],
    ["C756","Julian","Jacinta"],
    ["C938","Paco","Paca"],
    ["C645","Ernesto","Terrazas"]
])

carta1 = Carta("C123", "Carta sobre reunión importante")
carta2 = Carta("C999", "Informe urgente")
carta3 = Carta("C645", "Carta de amor")


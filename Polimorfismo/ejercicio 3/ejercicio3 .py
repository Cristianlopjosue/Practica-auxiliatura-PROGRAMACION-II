class Matriz:
    def __init__(self):
        self.matriz = [[1.0 if i == j else 0.0 for j in range(10)] for i in range(10)]

    def sumar(self, otra):
        resultado = [[self.matriz[i][j] + otra.matriz[i][j] for j in range(10)] for i in range(10)]
        return Matriz(resultado)

    def restar(self, otra):
        resultado = [[self.matriz[i][j] - otra.matriz[i][j] for j in range(10)] for i in range(10)]
        return Matriz(resultado)

    def igual(self, otra):
        for i in range(10):
            for j in range(10):
                if self.matriz[i][j] != otra.matriz[i][j]:
                    return False
        return True

m1 = Matriz()
m2 = Matriz([[i+j for j in range(10)] for i in range(10)])
m3 = m1.sumar(m2)
m4 = m2.restar(m1)
print(m1.igual(m2))
print(m1.igual(m1))

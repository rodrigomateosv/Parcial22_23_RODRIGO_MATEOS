import copy

class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

    def submatriz(self, fila, columna):
        submatriz = copy.deepcopy(self.elementos)
        del submatriz[fila]
        for fila in submatriz:
            del fila[columna]
        return Matriz(submatriz)

    def determinante_recursivo(self):
        if len(self.elementos) == 2:
            return self.elementos[0][0] * self.elementos[1][1] - self.elementos[0][1] * self.elementos[1][0]
        else:
            det = 0
            for i in range(len(self.elementos)):
                coeficiente = self.elementos[0][i]
                if i % 2 != 0:
                    coeficiente = -coeficiente
                det += coeficiente * self.submatriz(0, i).determinante_recursivo()
            return det

matriz = Matriz([
    [2, 3, 1, 4, 5],
    [3, 1, 4, 2, 6],
    [5, 3, 2, 4, 7],
    [6, 1, 5, 2, 8],
    [7, 4, 3, 5, 9]
])

print("Determinante recursivo:", matriz.determinante_recursivo())

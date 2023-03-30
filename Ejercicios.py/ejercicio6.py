class Nodo:
    def __init__(self, matriz, signo):
        self.matriz = matriz
        self.signo = signo

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def submatriz(matriz, col):
    return [fila[:col] + fila[col+1:] for fila in matriz[1:]]

def determinante_recursivo_con_pila(matriz):
    pila = Pila()
    determinante = 0

    for i, coeficiente in enumerate(matriz[0]):
        pila.push(Nodo(submatriz(matriz, i), ((-1) ** i) * coeficiente))

    while not pila.is_empty():
        nodo = pila.pop()
        matriz_actual = nodo.matriz
        signo_actual = nodo.signo

        if len(matriz_actual) == 1:
            determinante += signo_actual * matriz_actual[0][0]
        else:
            for i, coeficiente in enumerate(matriz_actual[0]):
                pila.push(Nodo(submatriz(matriz_actual, i), signo_actual * ((-1) ** i) * coeficiente))

    return determinante

def determinante_iterativo_con_pila(matriz):
    pila = Pila()
    determinante = 0
    signo = 1

    pila.push(Nodo(matriz, 0, 0))

    while not pila.is_empty():
        nodo = pila.pop()
        matriz_actual = nodo.matriz

        if len(matriz_actual) == 2:
            determinante += nodo.signo * (matriz_actual[0][0] * matriz_actual[1][1] - matriz_actual[0][1] * matriz_actual[1][0])
        else:
            for i, coeficiente in enumerate(matriz_actual[0]):
                pila.push(Nodo(submatriz(matriz_actual, i), nodo.signo * ((-1) ** i) * coeficiente))

    return determinante

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print("Determinante (recursivo con pila y clases):", determinante_recursivo_con_pila(matriz))
print("Determinante (iterativo con pila y clases):", determinante_iterativo_con_pila(matriz))

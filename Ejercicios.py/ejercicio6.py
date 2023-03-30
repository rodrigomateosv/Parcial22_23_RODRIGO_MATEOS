import copy 

class NodoPila:
    # Clase nodo pila
    def __init__(self, valor):
        self.info = valor
        self.sig = None

class Pila:
    # Clase pila
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo = NodoPila(valor)
        nuevo.sig = self.cima
        self.cima = nuevo

    def desapilar(self):
        valor = self.cima.info
        self.cima = self.cima.sig
        return valor

    def pila_vacia(self):
        return self.cima == None

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        for i in range(self.filas):
            self.matriz.append([0] * self.columnas)

    def __str__(self):
        return str(self.matriz)

def determinante_recursivo(Matriz, total=0):
    """
    Función para el cálculo recursivo del determinante de cualquier matriz cuadrada.
    """
    tamaño = list(range(len(Matriz))) 

    if len(Matriz) == 2 and len(Matriz[0]) == 2: 
        val = Matriz[0][0] * Matriz[1][1] - Matriz[1][0] * Matriz[0][1] 
        return val 

    for fc in tamaño: 
        As = copy.deepcopy(Matriz) 
        As = As[1:] 
        height = len(As) 

        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 

        sign = (-1) ** (fc % 2)  
        sub_det = determinante_recursivo(As) 
        total += sign * Matriz[0][fc] * sub_det 

    return total 

def determinante_iterativo(Matriz1):
    aux = 0 
    for o in range(0, size): 
        temp = 1 
        k = o 
        for i in range(0, size): 
            temp *= Matriz1[i][k] 
            k += 1  
            if k == size: 
                k = 0 
        aux += temp 

    for o in range(size-1, -1, -1): 
        temp = 1 
        k = o 
        for i in range(0, size): 
            temp *= Matriz1[i][k] 
            k -= 1 
            if k == -1: 
                k = size - 1 
        aux -= temp 
    return aux 

Matriz1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] 
size = len(Matriz1) 

if __name__ == "__main__":
    # prueba de la función determinante_recursivo

    # Introductimos el tamaño de la matriz
    n = 5
    # Creamos una matriz cuadrada random de tamaño nxn
    Matriz = [0]


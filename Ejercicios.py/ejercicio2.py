def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    Izquierda = merge_sort(lst[:mid])
    derecha = merge_sort(lst[mid:])

    return merge_recursivo(Izquierda, derecha)

def merge_recursivo(Izquierda, derecha, result=None):
    if result is None:
        result = []

    if not Izquierda:
        result.extend(derecha)
        return result
    elif not derecha:
        result.extend(Izquierda)
        return result
    elif Izquierda[0] < derecha[0]:
        result.append(Izquierda[0])
        return merge_recursivo(Izquierda[1:], derecha, result)
    else:
        result.append(derecha[0])
        return merge_recursivo(Izquierda, derecha[1:], result)

numeros = [18, 50, 210, 80, 145, 333, 70, 30]

for numero in numeros:
    if numero > 300:
        print("Se encontró un número mayor a 300, terminando el programa.")
        break
    if numero % 10 == 0 and numero < 200:
        print(numero)

# Organizar la lista usando el método Merge Sort
numeros_ordenados = merge_sort(numeros)
print("Lista ordenada:", numeros_ordenados)

def buscar_valor_recursivo(lista, valor, indice):
    if not lista:
        return -1
    if lista[0] == valor:
        return indice
    else:
        return buscar_valor_recursivo(lista[1:], valor, indice + 1)

numeros = [18, 50, 210, 80, 145, 333, 70, 30]
valor_buscado = 145

indice = buscar_valor_recursivo(numeros, valor_buscado, 0)
print(f"El índice del valor {valor_buscado} en la lista es: {indice}")


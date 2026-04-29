# Lógica, pensaba usar set primero pero no se puede

entrada = [4, 2, 7, 2, 4, 9, 1]
#salida = [1, 2, 4, 7, 9]

# Código sacado de https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/
# con mergesort probablemente era mejor (en términos de complejidad)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

def ordenarLista(entrada):
    bubbleSort(entrada) #Lo ordenamos
    resultado = []
    for index in range(len(entrada)):
        if index == 0 or entrada[index] != entrada[index - 1]: 
            # añadimos la primera posición | añadimos el número si no es igual al anterior
            resultado.append(entrada[index])
    return resultado

print(ordenarLista(entrada))
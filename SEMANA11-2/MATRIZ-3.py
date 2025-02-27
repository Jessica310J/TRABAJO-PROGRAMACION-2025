def bubble_sort(fila):
    """Ordena una fila utilizando Bubble Sort."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Matriz de ejemplo
matriz = [
    [3, 2, 1],
    [4, 5, 6],
    [7, 8, 9]
]

# Fila a ordenar (en este caso, la primera fila)
fila_a_ordenar = 0

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)

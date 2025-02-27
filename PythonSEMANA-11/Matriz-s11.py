def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    Parameters:
    - matriz: Matriz bidimensional a buscar.
    - valor: Valor a buscar en la matriz.

    Returns:
    - La posición del valor si se encuentra, de lo contrario, un mensaje indicando que no se encontró.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor encontrado en la posición ({i}, {j})"
    return "Valor no encontrado en la matriz"


# Ejemplo de uso
matriz = [
    [6, 8, 7],
    [4, 5, 3],
    [9, 1, 2]
]

valor_a_buscar = 7
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)

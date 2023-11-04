
def algoritmo_burbuja_inverso(random):
    if not isinstance(random, list):
        raise ValueError("Solo se aceptan Listas")

    ordenada = random.copy()
    for i in range(len(ordenada) - 1):
        for j in range(len(ordenada) - 1 - i):
            if ordenada[j] < ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    return ordenada

def numeros_en_orden_inverso():
    numeros = list(range(1, 11))
    numeros_inverso = algoritmo_burbuja_inverso(numeros)
    return numeros_inverso

if __name__ == "__main__":
    numeros = numeros_en_orden_inverso()
    print(numeros)

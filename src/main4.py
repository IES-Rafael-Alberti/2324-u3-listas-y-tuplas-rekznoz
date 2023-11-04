
def es_numero(numero):
    if numero.isdigit():
        return True
    else:
        return False
    
def algoritmo_burbuja(random):
    if not isinstance(random, list):
        raise ValueError("Solo se aceptan Listas")

    ordenada = random.copy()
    for i in range(len(ordenada) - 1):
        for j in range(len(ordenada) - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    return ordenada

if __name__ == "__main__":
    loteria = []

    while len(loteria) < 6:
        entrada = input("Introduce un numero ")
        if es_numero(entrada):
            loteria.append(int(entrada))
        else:
            print("La entrada no es un numero")

    loteria_ordenada = algoritmo_burbuja(loteria)
    print(loteria_ordenada)
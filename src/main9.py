def contar_vocales(palabra):
    palabra = palabra.lower()
    conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1
    
    return conteo

if __name__ == "__main__":

    palabra = input("Introduce una palabra ")
    resultado = contar_vocales(palabra)

    for vocal, cantidad in resultado.items():
        print(f"{vocal}: {cantidad}")

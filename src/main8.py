def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "") 
    return palabra == palabra[::-1]

if __name__ == "__main__":
    palabra = input("Introduce una palabra ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palindromo.")
    else:
        print(f"{palabra} no es un palindromo.")

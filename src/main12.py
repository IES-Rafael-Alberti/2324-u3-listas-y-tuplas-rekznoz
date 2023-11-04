def producto_matriz(a, b):
    resultado = 0
    for i, _ in enumerate(a):
        resultado += a[i] * b[i]
    return resultado

if __name__=="__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    resultado = producto_matriz(a, b)
    print(f"Este es el producto de la matriz -> {resultado}")
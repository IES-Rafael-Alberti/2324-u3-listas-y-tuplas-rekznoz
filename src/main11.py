def producto_escalar(vector1, vector2):
    producto = 0
    for x, y in zip(vector1, vector2):
        producto += x * y
    return producto

if __name__ == "__main__":
    vector1 = [1, 2, 3]
    vector2 = [-1, 0, 2]
    resultado = producto_escalar(vector1, vector2)
    print(f"El producto escalar {vector1} y {vector2} es {resultado}")

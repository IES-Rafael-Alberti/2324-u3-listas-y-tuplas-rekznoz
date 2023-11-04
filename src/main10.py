def encontrar_menor(precios):
    if not precios:
        return 0
    menor_precio = min(precios)
    return menor_precio

def encontrar_mayor(precios):
    if not precios:
        return 0
    mayor_precio = max(precios)
    return mayor_precio

if __name__ == "__main__":
    precios = [50, 75, 46, 22, 80, 65, 8]
    menor, mayor = encontrar_menor(precios), encontrar_mayor(precios)
    
    if menor != 0 and mayor != 0:
        print(f"El precio más bajo es: {menor}")
        print(f"El precio más alto es: {mayor}")
    else:
        print("La lista de precios está vacía.")

def obtener_abecedario():
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    return abecedario

def multiplos_3(numero):
    if numero % 3 == 0:
        return True 
    else:
        return False
    
def eliminar_letras_multiplos_de_3(abecedario):
    abecedario_mod = []

    for i, letra in enumerate(abecedario, 1):
        if not multiplos_3(i):
            abecedario_mod.append(letra)

    return abecedario_mod

if __name__ == "__main__":
    abecedario = obtener_abecedario()
    abecedario_mod = eliminar_letras_multiplos_de_3(abecedario)
    print(abecedario_mod)

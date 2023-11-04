def es_numero(numero):
    if numero.isdigit():
        return True
    else:
        return False
def obtener_asignaturas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
    return asignaturas

def aprobado_suspenso(numero):
    if numero <= 4 and numero >= 0 :
        return True
    else:
        return False

if __name__=="__main__":

    notas = []
    suspensos = []
    asignaturas = obtener_asignaturas()

    for asignatura in asignaturas:
        numeroValido = True
        while numeroValido:
            nota = input("Nota de " + asignatura + " ")
            if es_numero(nota):
                numeroValido = False
                if aprobado_suspenso(int(nota)):
                    suspensos.append(asignatura)
            else:
                numeroValido = True

    print("Las asignaturas suspensas son" , str(suspensos))
    
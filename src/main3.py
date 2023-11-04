def obtener_asignaturas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
    return asignaturas

if __name__ == "__main__":
    asignaturas = obtener_asignaturas()
    notas = []

    for asignatura in asignaturas:
        nota = input(f"Introduce la nota de {asignatura}: ")
        notas.append(nota)

    for i, asignatura in enumerate(asignaturas):
        print(f"En {asignatura} has sacado {notas[i]}")
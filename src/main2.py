def obtener_asignaturas():
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
    return asignaturas

if __name__ == "__main__":
    asignaturas = obtener_asignaturas()

    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")

    
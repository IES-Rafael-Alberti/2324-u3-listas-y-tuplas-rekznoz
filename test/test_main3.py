from src.main3 import obtener_asignaturas

def test_obtener_asignaturas():
    asignaturas = obtener_asignaturas()
    assert "Matematicas" in asignaturas
    assert "Fisica" in asignaturas
    assert "Quimica" in asignaturas
    assert "Historia" in asignaturas
    assert "Lenguaje" in asignaturas
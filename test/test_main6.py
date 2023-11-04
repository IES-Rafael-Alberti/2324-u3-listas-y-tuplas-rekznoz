from src.main6 import obtener_asignaturas, es_numero, aprobado_suspenso

def test_obtener_asignaturas():
    asignaturas = obtener_asignaturas()
    assert "Matematicas" in asignaturas
    assert "Fisica" in asignaturas
    assert "Quimica" in asignaturas
    assert "Historia" in asignaturas
    assert "Lenguaje" in asignaturas

def test_es_numero():
    assert es_numero("123") == True
    assert es_numero("0") == True
    assert es_numero("999") == True

def test_aprobado_suspenso():
    assert aprobado_suspenso(4) == True
    assert aprobado_suspenso(6) == False
    assert aprobado_suspenso(9) == False
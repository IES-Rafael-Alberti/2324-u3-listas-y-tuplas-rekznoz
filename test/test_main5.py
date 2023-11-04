from src.main5 import algoritmo_burbuja_inverso, numeros_en_orden_inverso

def test_algoritmo_burbuja_inverso():
    assert algoritmo_burbuja_inverso([5, 2, 8, 1, 9, 3]) == [9, 8, 5, 3, 2, 1]

def test_numeros_en_orden_inverso():
    result = numeros_en_orden_inverso()
    assert result == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
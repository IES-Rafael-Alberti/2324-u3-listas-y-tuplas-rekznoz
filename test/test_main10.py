from src.main10 import encontrar_menor, encontrar_mayor

def test_encontrar_menor():
    precios = [5, 10, 3, 8, 2]
    assert encontrar_menor(precios) == 2

def test_encontrar_mayor():
    precios = [1, 2, 3, 4, 5]
    assert encontrar_mayor(precios) == 5
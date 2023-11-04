from src.main12 import producto_matriz

def test_producto_matriz():
    a = [1, 2, 3]
    b = [4, 5, 6]
    assert producto_matriz(a, b) == 32
from src.main11 import producto_escalar

def test_producto_escalar():
    assert producto_escalar([1, 2, 3], [-1, 0, 2]) == 5
    assert producto_escalar([1, 2, 3], [0, 0, 0]) == 0
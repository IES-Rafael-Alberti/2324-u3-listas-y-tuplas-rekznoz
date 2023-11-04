from src.main4 import es_numero, algoritmo_burbuja

def test_es_numero():
        assert es_numero("123") == True
        assert es_numero("0") == True
        assert es_numero("999") == True

def test_algoritmo_burbuja():
        assert algoritmo_burbuja([4, 2, 1, 3]) == [1, 2, 3, 4]
from src.main8 import es_palindromo

def test_es_palindromo():
    assert es_palindromo("reconocer") == True
    assert es_palindromo("oso") == True
    assert es_palindromo("casa") == False
    assert es_palindromo("Anilina") == True
    assert es_palindromo("a man a plan a canal panama") == True

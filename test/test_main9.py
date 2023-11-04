from src.main9 import contar_vocales

def test_contar_vocales():
    assert contar_vocales("murcielago") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    assert contar_vocales("AEIOU") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    assert contar_vocales("zyxwv") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
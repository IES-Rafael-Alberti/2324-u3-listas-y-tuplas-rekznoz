from src.main7 import obtener_abecedario, multiplos_3, eliminar_letras_multiplos_de_3

def test_obtener_abecedarios():
    result = obtener_abecedario()
    assert result == list("abcdefghijklmnopqrstuvwxyz")

def test_multiplos_3():
    assert multiplos_3(3) == True
    assert multiplos_3(6) == True
    assert multiplos_3(9) == True
    assert multiplos_3(12) == True

def test_eliminar_letras_multiplos_de_3():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    retorno = eliminar_letras_multiplos_de_3(abecedario)
    assert retorno == ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k']
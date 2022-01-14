import unittest
from lista1 import exercicios


class TestProrama1(unittest.TestCase):
    def test_maior_de_idade(self):
        expected = 'Apto a ser eleitor'
        result = exercicios.verifica_idade_eleitor(1994)
        self.assertEqual(expected, result)

    def test_menor_de_idade(self):
        expected = 'Inapto a ser eleitor'
        result = exercicios.verifica_idade_eleitor(2018)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

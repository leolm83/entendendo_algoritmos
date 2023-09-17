import unittest
import ex1_busca_binaria as b


class BuscaBinaria(unittest.TestCase):

    def test_espera_encontrar_o_valor_na_lista(self):
        self.assertEqual(b.busca_binaria([0,1,2,3,4,5],1), 1)
        
    def test_espera_nao_encontrar_o_valor_na_lista(self):
        self.assertEqual(b.busca_binaria([0,1,2,3,4,5],9), None)

if __name__ == '__main__' :
    unittest.main()
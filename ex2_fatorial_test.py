import unittest
import ex2_fatorial as f


class Fatorial(unittest.TestCase):

    def test_fatorial_de_5_deve_ser_120(self):
        self.assertEqual(f.fatorial(5), 120)

    def test_fatorial_de_1_deve_ser_1(self):
        self.assertEqual(f.fatorial(1), 1)

    def test_fatorial_ternario_de_5_deve_ser_120(self):
        self.assertEqual(f.fatorial_ternario(5), 120)

    def test_fatorial_ternario_de_1_deve_ser_1(self):
        self.assertEqual(f.fatorial_ternario(1), 1)


if __name__ == '__main__' :
    unittest.main()
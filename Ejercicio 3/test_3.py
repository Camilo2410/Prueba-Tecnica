import unittest
import solucion


class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(solucion.min_jumps(3), 2, "x=1 debería requerir 2 saltos")
        self.assertEqual(solucion.min_jumps(5), 4, "x=2 debería requerir 4 saltos")
        self.assertEqual(solucion.min_jumps(7), 5, "x=3 debería requerir 5 saltos")
        self.assertEqual(solucion.min_jumps(9), 5, "x=3 debería requerir 5 saltos")


if __name__ == '__main__':
    unittest.main()
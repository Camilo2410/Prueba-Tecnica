import unittest
import solucion


class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(solucion.min_jumps(1), 1, "x=1 debería requerir 1 salto")
        self.assertEqual(solucion.min_jumps(2), 3, "x=2 debería requerir 3 saltos")
        self.assertEqual(solucion.min_jumps(3), 2, "x=3 debería requerir 2 saltos")


if __name__ == '__main__':
    unittest.main()

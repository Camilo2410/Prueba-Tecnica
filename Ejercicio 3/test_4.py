import unittest
import solucion


class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(solucion.min_jumps(2), 2, "x=1 debería requerir 3 saltos")
        self.assertEqual(solucion.min_jumps(4), 3, "x=2 debería requerir 3 saltos")
        self.assertEqual(solucion.min_jumps(6), 3, "x=3 debería requerir 3 saltos")


if __name__ == '__main__':
    unittest.main()

import unittest
import solucion


class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(solucion.min_jumps(4), 3, "x=1 debería requerir 3 saltos")
        self.assertEqual(solucion.min_jumps(1000), 46, "x=2 debería requerir 46 saltos")
        self.assertEqual(solucion.min_jumps(74), 12, "x=3 debería requerir 12 saltos")
        self.assertEqual(solucion.min_jumps(5670), 107, "x=3 debería requerir 107 saltos")


if __name__ == '__main__':
    unittest.main()
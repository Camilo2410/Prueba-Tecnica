import unittest
import solucion


class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(solucion.min_jumps(1000), 46, "x=1 debería requerir 46 saltos")
        self.assertEqual(solucion.min_jumps(2000), 63, "x=2 debería requerir 63 saltos")
        self.assertEqual(solucion.min_jumps(3000), 78, "x=3 debería requerir 78 saltos")
        self.assertEqual(solucion.min_jumps(4000), 90, "x=3 debería requerir 90 saltos")


if __name__ == '__main__':
    unittest.main()

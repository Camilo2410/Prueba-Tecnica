import unittest
import solucion


class TestF1Championship(unittest.TestCase):
    def test_calculate_champions(self):
        # Simulando los inputs del ejemplo
        number_of_races = 1
        race_results = [[3, 2, 1]]
        scoring_systems = [[5, 3, 2], [5, 3, 1], [1, 1, 1]]

        champions = solucion.calculate_champions(number_of_races, race_results, scoring_systems)
        # Llamando a la función que queremos testear

        # Chequeando que la salida es la esperada
        self.assertEqual(champions, [[3], [3], [1, 2, 3]])


# Permite ejecutar los tests con el comando `python test_solution.py`
if __name__ == '__main__':
    unittest.main()
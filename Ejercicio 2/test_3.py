import unittest
import solucion


class TestF1Championship(unittest.TestCase):
    def test_different_values_3(self):
        number_of_races = 1
        race_results = [[2, 1]]
        scoring_systems = [[9, 6], [6, 4], [4, 3], [2, 1]]
        expected = [[1], [1], [1], [1]]

        champions = solucion.calculate_champions(number_of_races, race_results, scoring_systems)
        self.assertEqual(champions, expected)


if __name__ == '__main__':
    unittest.main()

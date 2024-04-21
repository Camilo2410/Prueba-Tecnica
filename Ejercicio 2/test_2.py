import unittest
import solucion


class TestF1Championship(unittest.TestCase):
    def test_different_values_2(self):
        number_of_races = 3
        race_results = [[1, 2, 3], [2, 1, 3], [2, 3, 1]]
        scoring_systems = [[10, 5, 1]]
        expected = [[2]]

        champions = solucion.calculate_champions(number_of_races, race_results, scoring_systems)
        self.assertEqual(champions, expected)


if __name__ == '__main__':
    unittest.main()

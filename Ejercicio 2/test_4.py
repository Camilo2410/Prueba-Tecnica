import unittest
import solucion


class TestF1Championship(unittest.TestCase):
    def test_different_values_4(self):
        number_of_races = 4
        race_results = [[4, 3, 2, 1], [3, 4, 1, 2], [2, 1, 4, 3], [1, 2, 3, 4]]
        scoring_systems = [[12, 9, 6, 3], [8, 6, 4, 2]]
        expected = [[1, 2, 3, 4], [1, 2, 3, 4]]

        champions = solucion.calculate_champions(number_of_races, race_results, scoring_systems)
        self.assertEqual(champions, expected)


if __name__ == '__main__':
    unittest.main()
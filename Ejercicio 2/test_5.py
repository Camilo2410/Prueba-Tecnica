import unittest
import solucion


class TestF1Championship(unittest.TestCase):
    def test_different_values_5(self):
        number_of_races = 10
        race_results = [
            [1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3],
            [1, 3, 2, 4], [2, 1, 4, 3], [3, 2, 1, 4], [4, 3, 2, 1],
            [1, 4, 3, 2], [2, 1, 3, 4]
        ]
        scoring_systems = [
            [25, 18, 15, 12],
            [10, 8, 6, 5],
            [50, 40, 30, 20],
            [100, 0, 0, 0]
        ]
        expected = [
            [2],
            [2],
            [2],
            [1, 2, 3, 4]
        ]

        champions = solucion.calculate_champions(number_of_races, race_results, scoring_systems)
        self.assertEqual(champions, expected)


if __name__ == '__main__':
    unittest.main()
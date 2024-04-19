import unittest
from solucion import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        result = is_palindrome("luz azul")
        print(f"Result: {result}")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

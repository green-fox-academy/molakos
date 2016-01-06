import unittest
from dojo_soduku import *

class TestValidateNumbers(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(validate_numbers([]), False)

    def test_lenght_nine(self):
        self.assertEqual(validate_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)
        self.assertEqual(validate_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1]), True)

    def test_is_not_number(self):
        self.assertEqual(validate_numbers(['a', 'b', 'c', 4, 5, 6, 7, 8, 9]), False)

    def test_lenght_seven(self):
        self.assertEqual(validate_numbers([1, 2, 3, 4, 5, 6, 7]), False)

unittest.main()

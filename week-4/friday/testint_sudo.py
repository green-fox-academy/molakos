import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_empty_true(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is good.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too long.")

    def test_is_complete_repetitive_numbers(self):
        test_input = [1, 2, 2, 3, 4, 5, 6, 7, 9]
        expected = False
        actual = sudoku_checker.is_the_same(test_input)
        self.assertEqual(expected, actual, "There are repetitive numbers")

    def test_is_complete_correct_numbers(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = True
        actual = sudoku_checker.is_the_same(test_input)
        self.assertEqual(expected, actual, "The row is good")

    def test_is_complete_correct_numbers_reversed(self):
        test_input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = True
        actual = sudoku_checker.is_the_same(test_input)
        self.assertEqual(expected, actual, "The row is good")
        
unittest.main()

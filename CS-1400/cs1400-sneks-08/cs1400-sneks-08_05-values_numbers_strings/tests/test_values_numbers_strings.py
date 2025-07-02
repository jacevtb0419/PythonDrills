import ast
import unittest

import asttest

class TestValuesNumbersStrings(asttest.ASTTest):

    def setUp(self):
        super().setUp("values_numbers_strings.py")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 2, "You should print exactly "
                "two lines of output.")
        number = self.printed_lines[0]
        self.assertIsInstance(number, int, "First, you must print out your "
                "birth year as a number.")
        self.assertGreater(number, 0, "I'm pretty sure that's not when you "
                "were born.")
        self.assertLess(number, 2020, "I'm pretty sure that's not when you "
                "were born.")
        string = self.printed_lines[1]
        self.assertIsInstance(string, str, "The second thing you print should "
                "be your birth year as a string.")
        self.assertEqual(str(number), string, "The output should be the same "
                "for both the string and the number.")

if __name__ == "__main__":
    unittest.main()

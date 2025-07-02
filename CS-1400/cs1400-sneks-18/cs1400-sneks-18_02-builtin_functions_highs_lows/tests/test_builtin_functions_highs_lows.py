import ast
import unittest

import asttest

class TestBuiltinFunctionsHighsLows(asttest.ASTTest):

    def setUp(self):
        super().setUp("builtin_functions_highs_lows.py")

    def test_required_syntax(self):
        strs = [s.s for s in self.find_all(ast.Str)]
        self.assertGreaterEqual(len(strs), 1, "You should not erase the "
                "original \"High, High, Low, ...\" string. Reload the starter "
                "code and try again.")

        self.assertIn("High, High, Low, Low, High, High, Low", strs, 'You '
                'should not erase the original "High, High, Low, ..." string.')
        self.assertLessEqual(len(strs), 2, "You should only have two string "
                "literals in your code.")
        self.assertEqual(len(self.find_all(ast.Num)), 0, "You should have no "
                "integer or float literals in your code!")
        attrs = [a.attr for a in self.find_all(ast.Attribute)]
        self.assertIn('count', attrs, "What method from the reference page is "
                "used to count occurrences in a string?")
        self.assertEqual(len(strs), 2, "What are you counting? Double-check "
                "the documentation for the count function.")
        self.assertNotIn("Low", strs, "You are not supposed to be counting the"
                " Lows; count the Highs!")
        self.assertNotIn("high", strs, "Remember, strings are case-sensitive "
                "so capitialization matters!")
        self.assertIn("High", strs, "What are you supposed to be counting?")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line of output.")
        self.assertEqual(self.printed_lines[0], 4, "You are printing the wrong"
                " thing!")

if __name__ == "__main__":
    unittest.main()

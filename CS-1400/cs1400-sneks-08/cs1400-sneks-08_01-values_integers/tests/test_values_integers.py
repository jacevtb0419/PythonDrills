import ast
import sys
import unittest

import asttest

class TestValuesIntegers(asttest.ASTTest):

    def setUp(self):
        super().setUp("values_integers.py")

    def test_required_syntax(self):
        funcs = self.find_all(ast.Call)
        self.assertNotEqual(len(funcs), 0, "You need to actually call the print "
                "function.")
        self.assertEqual(len(funcs), 1, "You only need a single function call "
                "to print.")
        self.assertIn(funcs[0].func.id, "print", "You will need to call the print "
                "function.")
        self.assertIsInstance(funcs[0].func, ast.Name, "Function is not of "
                "type ast.Name. Please send this error to ren.quinn@dixie.edu")
        self.assertNotEqual(len(funcs[0].args), 0, "You are not printing "
                "anything! You need to put something in between those "
                "parentheses...")
        self.assertEqual(len(funcs[0].args), 1, "You should be printing a "
                "single number.")
        names = self.find_all(ast.Name)
        self.assertEqual(len(names), 1, "There is no need to use variables, "
                "just print a single integer literal.")
        arg = funcs[0].args[0]
        number = 0
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
            self.assertIsInstance(arg, ast.Constant, "You need to be "
                    "printing a number.")
            number = arg.value
            self.assertNotIsInstance(number, str, "You need to be printing a "
                    "number. Instead, you are printing a string. Notice the "
                    "quotation marks?")
        else:
            self.assertNotIsInstance(arg, ast.Str, "You need to be printing a "
                    "number. Instead, you are printing a string. Notice the "
                    "quotation marks?")
            self.assertIsInstance(arg, ast.Num, "You need to be "
                    "printing a number.")
            number = arg.n
        self.assertNotIsInstance(number, float, "You must not use a float "
                "value as your age in years (integers only).")
        self.assertIsInstance(number, int, "You should be "
                "printing an integer literal.")
        self.assertGreater(number, 0, "Pretty sure that's not a "
                "valid age. What's your actual age in years? (Or simply a valid "
                "age if you prefer not to reveal your actual age.)")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly "
                "one thing.")

if __name__ == "__main__":
    unittest.main()

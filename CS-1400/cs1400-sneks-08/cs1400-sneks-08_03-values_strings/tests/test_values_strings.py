import ast
import sys
import unittest

import asttest

class TestValuesStrings(asttest.ASTTest):

    def setUp(self):
        super().setUp("values_strings.py")

    def test_required_syntax(self):
        funcs = self.find_all(ast.Call)
        self.assertNotEqual(len(funcs), 0, "You need to actually call the print "
                "function.")
        self.assertEqual(len(funcs), 1, "You only need a single function call.")
        self.assertIn(funcs[0].func.id, "print", "You will need to call the print "
                "function.")
        self.assertIsInstance(funcs[0].func, ast.Name, "Function is not of "
                "type ast.Name. Please send this error to ren.quinn@dixie.edu")
        self.assertNotEqual(len(funcs[0].args), 0, "You are not printing "
                "anything! You need to put something in between those "
                "parentheses...")
        names = self.find_all(ast.Name)
        self.assertEqual(len(names), 1, "There is no need to use variables, "
                "just print a single string literal.")
        arg = funcs[0].args[0]
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
            self.assertIsInstance(arg, ast.Constant, "You need to be "
                        "printing a string.")
            self.assertIsInstance(arg.value, str, "You need to be "
                    "printing a string.")
        else:
            self.assertIsInstance(arg, ast.Str, "You need to be printing a "
                    "string.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly "
                "one thing.")
        self.assertGreaterEqual(len(self.printed_lines[0]), 1, "You need to "
                "print SOMETHING. Not just a blank string!")

if __name__ == "__main__":
    unittest.main()

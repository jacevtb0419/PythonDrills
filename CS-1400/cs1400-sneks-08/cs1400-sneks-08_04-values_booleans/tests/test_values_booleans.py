import ast
import sys
import unittest

import asttest

class TestValuesBooleans(asttest.ASTTest):

    def setUp(self):
        super().setUp("values_booleans.py")

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
        arg = funcs[0].args[0]
        if isinstance(arg, ast.Name):
            if arg.id in ["true", "false"]:
                self.fail("You wrote '{}' with a lower case '{}' instead of a "
                        "capital '{}'. Remember that Python identifies "
                        "booleans by a capital 'T' or 'F'".format(arg.id,
                            arg.id[0], arg.id[0].upper()))
        names = self.find_all(ast.Name)
        self.assertEqual(len(names), 1, "There is no need to use variables, "
                "just print a single boolean literal.")
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
            self.assertIsInstance(arg, ast.Constant, "You need to print a boolean "
                    "literal.")
        else:
            self.assertIsInstance(arg, ast.NameConstant, "You need to print a "
                    "boolean literal.")
        self.assertIsInstance(arg.value, bool, "You need to print a boolean "
                "literal.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly "
                "one thing.")
        self.assertNotIn(self.printed_lines[0], ["True", "False", "true",
            "false"], "You are printing a string literal with the value {} "
            "instead of a boolean literal. They are different! Your code "
            "should not have quotation marks in "
            "it.".format(self.printed_lines[0]))

if __name__ == "__main__":
    unittest.main()

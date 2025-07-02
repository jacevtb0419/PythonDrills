import ast
import sys
import unittest

import asttest

class TestValuesFloats(asttest.ASTTest):

    def setUp(self):
        super().setUp("values_floats.py")

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
        names = self.find_all(ast.Name)
        self.assertEqual(len(names), 1, "There is no need to use variables, "
                "just print a single float literal.")
        arg = funcs[0].args[0]
        if isinstance(arg, ast.UnaryOp) and isinstance(arg.op, ast.USub):
            if is_num(arg.operand):
                # if they type a negative number
                self.fail("Pretty sure that's not a valid GPA. Surely you "
                        "can get a better GPA?")
            else:
                self.fail("You need to be printing a number.")
        else:
            self.assertTrue(is_num(arg), "You need to be printing a number.")

        number = 0
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
            self.assertIsInstance(arg, ast.Constant, "You need to be "
                    "printing a number.")
            number = arg.value
            self.assertNotIsInstance(number, str, "You need to be "
                    "printing a number. Instead, you are printing a string. Notice "
                    "the quotation marks?")
        else:
            self.assertNotIsInstance(arg, ast.Str, "You need to be printing a "
                    "number. Instead, you are printing a string. Notice the "
                    "quotation marks?")
            self.assertIsInstance(arg, ast.Num, "You need to be "
                    "printing a number.")
            number = arg.n
        self.assertNotIsInstance(number, int, "You must use a float value as "
                "your ideal GPA. What's the difference between floats and "
                "integers?")
        self.assertIsInstance(number, float, "You must use a float value as "
                "your ideal GPA.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly "
                "one thing.")
        number = self.printed_lines[0]
        self.assertGreaterEqual(number, 0.0, "Pretty sure that's not a valid "
                "GPA. Surely you can get a better GPA?")
        self.assertLessEqual(number, 4.0, "A worthwhile goal, to be sure, but "
                "GPAs are 4.00 or less at our school :)")

def is_num(value):
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        return isinstance(value, ast.Constant)
    else:
        return isinstance(value, ast.Num)

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestArithmeticFormula(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_formula.py", False)

    def test_required_syntax(self):
        if 'x' in self.file or '×' in self.file:
            self.fail("Remember that the multiplication operator in Python is "
                    "a single asterisk (*).")

        self.tree = ast.parse(self.file)

        numbers = self.find_all(ast.Num)
        seen_50 = False
        for number in numbers:
            if number.n == 10:
                self.fail("You cannot embed the answer into your code. Use the formula!")
            elif number.n == 50:
                seen_50 = True
        if not seen_50:
            self.fail("You must use the value 50 in your code.")

        if self.find_all(ast.Str):
            self.fail("You should not be using any strings.")

        if len(self.find_all(ast.BinOp)) < 2:
            self.fail("You have not written the correct formula!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertGreaterEqual(len(self.printed_lines), 1, "You must print "
                "out the correct answer.")
        self.assertLessEqual(len(self.printed_lines), 1, "You have printed "
                "out too many things.")
        self.assertNotIsInstance(self.printed_lines[0], int, "The end result "
                "should be a float, not an integer.")
        self.assertIsInstance(self.printed_lines[0], float, "The end result "
                "should be a float.")
        self.assertNotAlmostEqual(self.printed_lines[0], 32.22222222222222, 7,
                "I think you're close, but not quite there. Remember the "
                "order of operations is important for Python expressions.")
        self.assertAlmostEqual(self.printed_lines[0], 10.0, 1, "This is not "
                "the correct result.")

if __name__ == "__main__":
    unittest.main()

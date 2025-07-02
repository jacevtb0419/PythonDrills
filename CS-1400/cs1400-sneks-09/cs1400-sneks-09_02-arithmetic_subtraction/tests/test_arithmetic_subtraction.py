import ast
import unittest

import asttest

class TestArithmeticSubtraction(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_subtraction.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertEqual(numbers[0].n, 15, "When subtracting how many weeks "
                "are left in the semester, the first number in the expression "
                "should be the total number of weeks in the semester (15).")
        self.assertEqual(numbers[1].n, 2, "When subtracting how many weeks "
                "are left in the semester, the second number in the expression "
                "should be how many weeks we've completed so far (2).")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single "
                "operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Sub, "The operator in your "
                "expression should be a subtraction operator (minus sign).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertEqual(self.printed_lines[0], 13, "You have calculated the "
                "wrong value.")

if __name__ == "__main__":
    unittest.main()

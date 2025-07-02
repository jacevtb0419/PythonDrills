import ast
import unittest

import asttest

class TestArithmeticDivision(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_division.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertEqual(numbers[0].n, 10000, "When dividing the number of "
                "students by the number of faculty, the first number in the "
                "expression should be the number of students (10000).")
        self.assertEqual(numbers[1].n, 212, "When dividing the number of "
                "students by the number of faculty, the second number in the "
                "expression should be the number of faculty (212).")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single "
                "operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Div, "The operator in your "
                "expression should be a division operator (single forward "
                "slash).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertNotEqual(self.printed_lines[0], 47, "Looks like you did "
                "some rounding. I see what you're getting at, but let's stick "
                "to regular /, shall we?")
        self.assertAlmostEqual(self.printed_lines[0], 47.169, 2, "You have "
                "calculated the wrong value.")

if __name__ == "__main__":
    unittest.main()

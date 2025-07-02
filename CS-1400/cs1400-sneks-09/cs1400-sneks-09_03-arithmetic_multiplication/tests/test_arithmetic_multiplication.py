import ast
import unittest

import asttest

class TestArithmeticMultiplication(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_multiplication.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        legal = [24, 365]
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertIn(numbers[0].n, legal, "You should use the numbers 24 and "
                "365 exactly once each in your code.")
        self.assertIn(numbers[1].n, legal, "You should use the numbers 24 and "
                "365 exactly once each in your code.")
        self.assertNotEqual(numbers[0].n, numbers[1].n, "You should only use "
                "the numbers 24 and 365 once each in your code.")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single "
                "multiplication operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Mult, "The operator in "
                "your expression should be a multiplication operator "
                "(asterisk).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertEqual(self.printed_lines[0], 8760, "You have calculated the "
                "wrong value.")


if __name__ == "__main__":
    unittest.main()

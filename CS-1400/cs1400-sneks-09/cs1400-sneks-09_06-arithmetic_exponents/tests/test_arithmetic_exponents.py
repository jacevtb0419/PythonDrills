import ast
import unittest

import asttest

class TestArithmeticExponents(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_exponents.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertEqual(numbers[0].n, 2, "The first number in the expression "
                "should be 2.")
        self.assertEqual(numbers[1].n, 10, "The second number in the expression "
                "should be 10.")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single "
                "operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Pow, "The operator in your "
                "expression should be a power operator (double asterisk).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertEqual(self.printed_lines[0], 1024, "You have calculated the "
                "wrong value.")

if __name__ == "__main__":
    unittest.main()

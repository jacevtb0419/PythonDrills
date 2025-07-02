import ast
import unittest

import asttest

class TestArithmeticModulo(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_modulo.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertEqual(numbers[0].n, 23, "The first number in the expression "
                "should be the hour to convert (23).")
        self.assertEqual(numbers[1].n, 12, "The second number in the expression "
                "should be the number of hours used by a clock (12).")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single "
                "operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Mod, "The operator in your "
                "expression should be a modulo operator (percent sign).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertEqual(self.printed_lines[0], 11, "You have calculated the "
                "wrong value.")

if __name__ == "__main__":
    unittest.main()

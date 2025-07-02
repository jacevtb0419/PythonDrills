import ast
import unittest

import asttest

class TestArithmeticAddition(asttest.ASTTest):

    def setUp(self):
        super().setUp("arithmetic_addition.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        legal = [2, 5]
        self.assertEqual(len(numbers), 2, "You should use exactly two numbers "
                "in your expression.")
        self.assertIn(numbers[0].n, legal, "You should use the numbers 2 and "
                "5 exactly once each in your code.")
        self.assertIn(numbers[1].n, legal, "You should use the numbers 2 and "
                "5 exactly once each in your code.")
        self.assertNotEqual(numbers[0].n, numbers[1].n, "You should only use "
                "the numbers 2 and 5 once each in your code.")

        operators = self.find_all(ast.BinOp)
        self.assertEqual(len(operators), 1, "You should use a single addition "
                "operator in your expression.")
        self.assertIsInstance(operators[0].op, ast.Add, "The operator in your "
                "expression should be an addition operator (plus sign).")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything! Put something between those parentheses.")
        self.assertEqual(self.printed_lines[0], 7, "You have calculated the "
                "wrong value")

if __name__ == "__main__":
    unittest.main()

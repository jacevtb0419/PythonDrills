import ast
import unittest

import asttest

class TestStatementsExpressionsArranging_2(asttest.ASTTest):

    def setUp(self):
        super().setUp("statements_expressions_arranging_2.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.Assign)), 6, "Do not delete any "
                "assignment statements! Reset the program!")
        self.assertEqual(len(self.find_all(ast.Num)), 2, "Do not delete any "
                "numbers! Reset the program!")
        self.assertEqual(len(self.find_all(ast.BinOp)), 3, "Do not delete any "
                "operations! Reset the program!")
        self.assertEqual(len(self.find_all(ast.Compare)), 2, "Do not delete any "
                "operations! Reset the program!")
        self.assertEqual(len(self.find_all(ast.BoolOp)), 1, "Do not delete any "
                "operations! Reset the program!")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "Do not add or remove any function "
                "calls. The only function call should be print.")
        self.assertIsInstance(calls[0].func, ast.Name, "Do not change any "
                "function calls. The only function call should be print.")
        self.assertEqual(calls[0].func.id, "print", "Do not change the "
                "function call. The only function call should be print.")
        self.assertEqual(len(calls[0].args), 1, "Do not change the "
                "function call. You should only be printing the e variable.")
        self.assertIsInstance(calls[0].args[0], ast.Name, "Do not change the "
                "function call. You should only be printing the e variable.")
        self.assertEqual(calls[0].args[0].id, "e", "Do not change the function"
                " call. You should only be printing the e variable.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You printed the wrong "
                "answer.")
        self.assertEqual(self.printed_lines[0], False, "You printed the wrong "
                "answer.")

if __name__ == "__main__":
    unittest.main()

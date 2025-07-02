import ast
import unittest

import asttest

class TestCallingCallsAndVariables(asttest.ASTTest):

    def setUp(self):
        super().setUp("calling_calls_and_variables.py")

    def test_required_syntax(self):
        self.assertNotIn("$", self.file, "You should not use the dollar sign "
                "($) anywhere in your code!")
        self.tree = ast.parse(self.file)

        self.assertEqual(len(self.find_all(ast.Str)), 0, "You should have no "
                "string literals in your code.")
        nums = self.find_all(ast.Num)
        self.assertEqual(len(nums), 1, "You should have exactly one number "
                "literal in your code.")
        self.assertEqual(nums[0].n, 9.50, "You need to make sure you have 9.50"
                " in your code.")

        calls = self.find_all(ast.Call)
        self.assertGreaterEqual(len(calls), 1, "You need to call the round "
                "function.")
        self.assertEqual(calls[0].func.id, "round", "Make sure you are using "
                "the round function! You'll want to call it first, before "
                "assigning")
        self.assertEqual(len(calls), 2, "You should call two functions.")
        self.assertEqual(calls[1].func.id, "print", "Make sure you are using "
                "the print function! You'll want to call it last, after you've"
                " assigned the rounded float to a variable.")

        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 1, "You have not created any new"
                " variables.")
        self.assertEqual(len(assigns), 1, "You have created more than one "
                "variable.")
        self.assertNotIsInstance(assigns[0].value, ast.Num, "Your variable has"
                " the wrong value. Make sure you round the number before "
                "storing it in the variable!")
        self.assertIsInstance(assigns[0].value, ast.Call, "You should assign "
                "the result of calling the round function to the variable.")
        self.assertEqual(assigns[0].value.func.id, "round", "You should assign"
                " the result of calling the round function to the variable.")
        self.assertEqual(len(assigns[0].value.args), 1, "You should pass in a "
                "single argument to round, a float literal.")
        self.assertIsInstance(assigns[0].value.args[0], ast.Num, "You should "
                "pass in a float literal to the round function.")
        self.assertEqual(assigns[0].value.args[0].n, 9.5, "Your variable has "
                "the wrong value.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should be printing "
                "one thing.")
        self.assertEqual(self.printed_lines[0], 10, "You are printing the "
                "wrong thing.")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestCallingRoundingUp(asttest.ASTTest):

    def setUp(self):
        super().setUp("calling_rounding_up.py", False)

    def test_required_syntax(self):
        self.assertNotIn("$", self.file, "You should not use the dollar sign "
                "($) anywhere in your code! While we are writing a program "
                "that deals with a dollar amount, Python doesn't understand "
                "the idea of currency.")
        self.tree = ast.parse(self.file)

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 2, "You should call two functions.")
        self.assertEqual(calls[0].func.id, "print", "The first/outer function "
                "call should be print.")
        self.assertEqual(calls[1].func.id, "round", "Make sure you are using "
                "the round function! You should call it inside of print.")

        nums = self.find_all(ast.Num)
        self.assertLessEqual(len(nums), 1, "You should only have one number "
                "literal in your code.")
        self.assertEqual(nums[0].n, 9.50, "You need to make sure you have 9.50"
                " in your code.")
        self.assertEqual(len(self.find_all(ast.Str)), 0, "You should have no "
                "string literals in your code.")


    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "line.")
        self.assertEqual(self.printed_lines[0], 10, "Incorrect output.")

if __name__ == "__main__":
    unittest.main()

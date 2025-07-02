import ast
import unittest

import asttest

class TestCallingCallsGoneWrong(asttest.ASTTest):

    def setUp(self):
        super().setUp("calling_calls_gone_wrong.py")

    def test_required_syntax(self):
        strs = self.find_all(ast.Str)
        self.assertGreaterEqual(len(strs), 1, "You have no "
                "literal string values in your code.")
        self.assertEqual(len(strs), 1, "You should only have the one string "
                "literal.")
        self.assertEqual(strs[0].s, "Whatever could be wrong?", "Do not "
                "change the original string literal.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertGreaterEqual(len(self.printed_lines), 1, "You are not "
                "printing!")
        self.assertEqual(len(self.printed_lines), 1, "You should only be "
                "printing one thing.")

if __name__ == "__main__":
    unittest.main()

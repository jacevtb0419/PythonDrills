import ast
import unittest

import asttest

class TestBuiltinFunctionsDashingName(asttest.ASTTest):

    def setUp(self):
        super().setUp("builtin_functions_dashing_name.py")

    def test_required_syntax(self):
        strs = [s.s for s in self.find_all(ast.Str)]
        self.assertGreaterEqual(len(strs), 1, "You have deleted the filename "
                "value. Reload the starter code to get it back!")
        self.assertNotIn("01-All-The-Single-Ladies.mp3", strs, "You cannot "
                "simply type in the answer as a string literal. How much time "
                "would that take for dozens of songs? I assure you it is much "
                "quicker to write a program using the replace method instead.")
        attrs = self.find_all(ast.Attribute)
        self.assertEqual(len(attrs), 1, "You need to call the string method "
                "named replace exactly one time.")
        self.assertEqual(attrs[0].attr, "replace", "You need to call the "
                "string method named replace exactly one time.")
        self.assertGreaterEqual(len(strs), 3, "You will need to create two new"
                " extra string literals, in addition to the original one.")
        self.assertEqual(len(strs), 3, "You only need to create two new extra "
                "strings.")
        self.assertIn(" ", strs, "For the first argument to replace, consider "
                "what character you want to replace in the filename.")
        self.assertIn("-", strs, "For the second argument to replace, consider"
                " what character with which you want to replace the spaces in "
                "the filename.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "thing, the fixed filename.")
        self.assertEqual("01-All-The-Single-Ladies.mp3", self.printed_lines[0],
                "Your output is not quite right, yet!")

if __name__ == "__main__":
    unittest.main()

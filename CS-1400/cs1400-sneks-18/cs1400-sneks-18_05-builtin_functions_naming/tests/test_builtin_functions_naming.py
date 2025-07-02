import ast
import unittest

import asttest

class TestBuiltinFunctionsNaming(asttest.ASTTest):

    def setUp(self):
        super().setUp("builtin_functions_naming.py")

    def test_required_syntax(self):
        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 2, "You should call exactly two "
                "functions: print and the corrected string method.")
        for c in calls:
            if isinstance(c.func, ast.Attribute):
                self.assertEqual(c.func.attr, "upper", "You are not calling "
                        "the correct string method to change all characters in"
                        " the string to uppercase. You might want to "
                        "double-check the documentation!")
        self.assertIn("Why are you shouting?", self.file, "You should leave "
                "the original string as is.")
        strs = [s.s for s in self.find_all(ast.Str)]
        self.assertNotIn("WHY ARE YOU SHOUTING?", strs, "You can't just embed "
                "the solution in your program. Use the proper string method!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "line.")
        self.assertNotEqual(self.printed_lines[0], "Why are you shouting?",
                "You are printing the string unmodified. It needs to be all "
                "upper case.")
        self.assertEqual(self.printed_lines[0], "WHY ARE YOU SHOUTING?", "You "
                "are printing the wrong thing.")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestBuiltinFunctionsFixingTitles(asttest.ASTTest):

    def setUp(self):
        super().setUp("builtin_functions_fixing_titles.py")

    def test_required_syntax(self):
        self.assertIn( "  the-count-of-monte-cristo  ", self.file, "You should"
                " not delete the instructor provided string.")

        calls = self.find_all(ast.Call)
        called = {
                "rstrip": False,
                "lstrip": False,
                "strip": False,
                "replace": False,
                "title": False
                }
        for c in calls:
            if isinstance(c.func, ast.Attribute):
                if c.func.attr in called:
                    called[c.func.attr] = True
        self.assertFalse(called["rstrip"] or called["lstrip"], "Do not use "
                "lstrip or rstrip; just use strip!")
        self.assertTrue(called["strip"], "What method in the documentation "
                "*strips* whitespace from a string?")
        self.assertTrue(called["replace"], "What method in the documentation "
                "*replaces* characters in a string?")
        self.assertTrue(called["title"], "What method in the documentation "
                "capitalizes letters for a *title*?")

        print_args = []
        for c in calls:
            if isinstance(c.func, ast.Attribute) and c.func.attr == "replace":
                for arg in c.args:
                    if isinstance(arg, ast.Str):
                        print_args.append(arg.s)
                    else:
                        print_args.append(arg)
        self.assertIn("-", print_args, "You aren't calling the replace "
                "function with the correct arguments. What character are you "
                "replacing?")
        self.assertIn(" ", print_args, "You aren't calling the replace "
                "function with the correct arguments. What character do you "
                "need to replace with?")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "line")
        self.assertEqual(self.printed_lines[0], "The Count Of Monte Cristo",
                "You have not printed the correct result.")

if __name__ == "__main__":
    unittest.main()

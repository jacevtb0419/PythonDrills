import ast
import sys
import unittest

import asttest

class TestStringsIntsStrs(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_ints_strs.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertEqual(len(assigns), 2, "You should have exactly two "
                "assignment statements.")
        for assign in assigns:
            if sys.version_info >= (3, 8):
                self.assertIsInstance(assign.value, ast.Constant, "It looks "
                        "like you assigned an incorrect value to your variable: "
                        "{}".format(assign.targets[0].id))
                if isinstance(assign.value.value, int):
                    self.assertEqual(assign.value.value, 5, "You assigned the "
                            "wrong number.")
                elif isinstance(assign.value.value, str):
                    self.assertEqual(assign.value.value, "5", "You assigned "
                            "the wrong string.")
            else:
                self.assertIn(type(assign.value), [ast.Num, ast.Str], "It looks "
                        "like you assigned an incorrect value to your variable: "
                        "{}".format(assign.targets[0].id))
                if isinstance(assign.value, ast.Num):
                    self.assertEqual(assign.value.n, 5, "You assigned the wrong "
                            "number.")
                elif isinstance(assign.value, ast.Str):
                    self.assertEqual(assign.value.s, "5", "You assigned the wrong "
                            "string.")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 2, "You should have exactly two "
                "function calls (both to print).")
        for call in calls:
            self.assertEqual(call.func.id, "print", "The only function you should"
                    " call is print.")
            self.assertEqual(len(call.args), 1, "You should print exactly one "
                    "variable at a time.")
            self.assertIsInstance(call.args[0], ast.Name, "You should only "
                    "print the variables.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 2, "You should print each "
                "variable on its own separate line.")
        self.assertEqual([5, "5"], self.printed_lines, "You printed the wrong "
                "thing.")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestDefiningFunctionsDoNothing(asttest.ASTTest):

    def setUp(self):
        super().setUp("defining_functions_do_nothing.py")

    def test_required_syntax(self):
        # TODO: unit_test("do_nothing", (None,), (None,), (None,)):
        self.assertIsNotNone(self.match_signature("do_nothing", 0), "You did "
                "not define your function correctly.")
        calls = self.get_function_calls()
        self.assertGreaterEqual(len(calls), 1, "You should call your function "
                "at least once.")
        self.assertIn("do_nothing", calls, "You should call your function "
                "at least once.")

        calls = self.find_all(ast.Call)
        for c in calls:
            if isinstance(c.func, ast.Name) and c.func.id == "print":
                self.assertEqual(len(c.args), 1, "You should print one "
                        "thing.")
                self.assertNotIsInstance(c.args[0], ast.NameConstant, "You "
                        "should not print None directly, or any other literal "
                        "for that matter. Just call your function and print "
                        "the result.")
                self.assertIsInstance(c.args[0], (ast.Call, ast.Name), "You "
                        "should call your function and print the result, "
                        "either directly as an argument to print or using a "
                        "variable.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints()
        self.assertIsNone(self.printed_lines[0], "You are not printing the "
                "right result.")

if __name__ == "__main__":
    unittest.main()

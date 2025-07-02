import ast
import unittest

import asttest

class TestCallingComposedCalls(asttest.ASTTest):

    def setUp(self):
        super().setUp("calling_composed_calls.py")

    def test_required_syntax(self):
        self.assertNotIn("$", self.file, "You should not use the dollar sign "
                "($) anywhere in your code!")
        self.tree = ast.parse(self.file)

        self.assertEqual(len(self.find_all(ast.Num)), 0, "You should have no "
                "number literals in your code.")
        strs = self.find_all(ast.Str)
        self.assertEqual(len(strs), 1, "You should have exactly one string "
                "literal in your code.")
        self.assertEqual(strs[0].s, "9.50", "You need to make sure you have "
                "the string \"9.50\" in your code.")

        funcnames = self.get_function_calls()
        self.assertIn("float", funcnames, "Make sure you are calling the float"
                " function!")
        self.assertIn("round", funcnames, "Make sure you are calling the round"
                " function!")

        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 1, "You have not created any "
                "new variables. Assign the result of calling the float and "
                "round functions (as a single, nested expression) to a "
                "variable.")
        self.assertEqual(len(assigns), 1, "You have created more than one "
                "variable when you only need one for this drill.")

        self.assertGreaterEqual(len(self.find_function_calls("print")), 1,
                "Make sure you are calling the print function!")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 3, "You are not making the right number "
                "of function calls.")
        self.assertEqual(calls[0].func.id, "round", "You aren't calling the "
                "round function correctly. Make sure you convert the string to"
                " a float before rounding it.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "thing.")
        self.assertEqual(self.printed_lines[0], 10, "Incorrect output.")

if __name__ == "__main__":
    unittest.main()

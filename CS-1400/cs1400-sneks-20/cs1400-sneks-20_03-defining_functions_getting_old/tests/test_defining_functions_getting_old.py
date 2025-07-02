import ast
import unittest

import asttest

class TestDefiningFunctionsGettingOld(asttest.ASTTest):

    def setUp(self):
        super().setUp("defining_functions_getting_old.py")

    def test_required_syntax(self):
        self.assertNotIn("input", self.get_function_calls(), "You should not "
                "use the input function. This function should literally return"
                " YOUR age, not the user's age.")

        self.assertIsNotNone(self.match_signature("get_my_age", 0), "You have "
                "not defined the function correctly.")

        calls = self.find_all(ast.Call)
        self.assertGreater(len(calls), 0, "You should call it at least once. A"
                " common mistake is to simply use the name of the function, "
                "without calling it (using the parentheses)!")
        self.assertGreaterEqual(len(calls), 2, "Remember to call both the "
                "print function and your get_my_age function.")
        for call in calls:
            self.assertIsInstance(call.func, ast.Name, "You are not calling "
                    "the correct functions.")
            self.assertIn(call.func.id, ["print", "get_my_age"], "You are not "
                    "calling the correct functions.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints()
        age = self.printed_lines[0]
        self.assertNotIn("<function get_my_age", str(age), "You have printed "
                "the NAME of the function, instead of actually calling the "
                "function. Notice the lack of parentheses?")
        self.assertIsNotNone(age, "You are not printing the correct result. "
                "Did you remember to return your age from your function?")
        self.assertIsInstance(age, (int, float), "Your age should be an "
                "integer or a float.")
        self.assertGreater(age, 0, "I don't think that's really your age...")

if __name__ == "__main__":
    unittest.main()

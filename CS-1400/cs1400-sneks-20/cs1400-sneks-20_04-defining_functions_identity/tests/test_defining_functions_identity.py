import ast
import unittest
import unittest.mock

import asttest

class TestDefiningFunctionsIdentity(asttest.ASTTest):

    def setUp(self):
        super().setUp("defining_functions_identity.py")

    def test_required_syntax(self):
        self.assertNotIn("input", self.get_function_calls(), "You should not "
                "use the input function. This function should rely on its "
                "parameter for input data, not the user directly.")

        self.assertIsNone(self.match_signature("identity", 0), "You have "
                "not defined the function correctly. Did you remember to give"
                " the function definition a parameter?")

        self.assertIsNotNone(self.match_signature("identity", 1), "You have "
                "not defined the function correctly.")

        calls = self.find_all(ast.Call)
        self.assertGreater(len(calls), 0, "You should call it at least once. A"
                " common mistake is to simply use the name of the function, "
                "without calling it (using the parentheses)!")
        self.assertGreaterEqual(len(calls), 2, "Remember to call both the "
                "print function and your identity function.")
        for call in calls:
            self.assertIsInstance(call.func, ast.Name, "You are not calling "
                    "the correct functions.")
            self.assertIn(call.func.id, ["print", "identity"], "You are not "
                    "calling the correct functions.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints()
        num = self.printed_lines[0]
        self.assertNotIn("<function identity", str(num), "You have printed "
                "the NAME of the function, instead of actually calling the "
                "function. Notice the lack of parentheses?")
        self.assertIsNotNone(num, "You are not printing the correct result. "
                "Did you remember to return the number parameter from your "
                "function?")
        self.assertIsInstance(num, (int, float), "The number should be an "
                "integer or a float.")

    @unittest.mock.patch('sys.stdout')
    def test_identity_function(self, mock_stdout):
        from defining_functions_identity import identity
        for i in range(10):
            self.assertEqual(identity(i), i, "Your function is not returning "
                    "the correct result. Did you remember to return the "
                    "parameter?")

if __name__ == "__main__":
    unittest.main()

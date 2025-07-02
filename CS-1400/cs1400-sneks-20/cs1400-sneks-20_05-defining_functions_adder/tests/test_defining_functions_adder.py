import ast
import unittest
import unittest.mock

import asttest

class TestDefiningFunctionsAdder(asttest.ASTTest):

    def setUp(self):
        super().setUp("defining_functions_adder.py")

    def test_required_syntax(self):
        self.assertNotIn("input", self.get_function_calls(), "You should not "
                "use the input function. This function should rely on its "
                "parameter for input data, not the user directly.")

        self.assertIsNone(self.match_signature("add_together", 0), "You have "
                "not defined the function correctly. Did you remember to give"
                " the function definition its parameters?")

        self.assertIsNotNone(self.match_signature("add_together", 2), "You "
                "have not defined the function correctly.")

        calls = self.find_all(ast.Call)
        self.assertGreater(len(calls), 0, "You should call your function at "
                "least once. A common mistake is to simply use the name of the"
                " function, without calling it (using the parentheses)!")
        self.assertGreaterEqual(len(calls), 2, "Remember to call both the "
                "print function and your add_together function.")
        for call in calls:
            self.assertIsInstance(call.func, ast.Name, "You are not calling "
                    "the correct functions.")
            self.assertIn(call.func.id, ["print", "add_together"], "You are not "
                    "calling the correct functions.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints()
        num = self.printed_lines[0]
        self.assertNotIn("<function add_together", str(num), "You have printed "
                "the NAME of the function, instead of actually calling it. "
                "Notice the lack of parentheses?")
        self.assertIsNotNone(num, "You are not printing the correct result. "
                "Did you remember to return the addition result from your "
                "function?")
        self.assertIsInstance(num, (int, float), "The addition result should "
                "be an integer or a float.")

    @unittest.mock.patch('sys.stdout')
    def test_add_together_function(self, mock_stdout):
        from defining_functions_adder import add_together
        tests = [(1,1,2), (4, 3, 7), (5,5,10), (-3,-3,-6)]
        for test in tests:
            result = add_together(test[0], test[1])
            self.assertEqual(result, test[2], "Your function is not returning"
                    " the correct result. When given {} and {} it returned {} "
                    "but should have returned {}."
                    .format(test[0], test[1], result, test[2]))

if __name__ == "__main__":
    unittest.main()

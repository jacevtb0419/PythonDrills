import ast
import unittest

import asttest

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("defining_functions_call.py")

    def test_required_syntax(self):
        self.assertIsNotNone(self.match_signature("average_numbers", 2), "You "
                "should leave the original function definition in the program."
                " The problem is with the function call, not its definition.")
        calls = self.get_function_calls()
        self.assertGreaterEqual(len(calls), 1, "You should call the function "
                "at least once.")
        self.assertIn('average_numbers', calls, "You should call the "
                "average_numbers function.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints()
        self.assertEqual(self.printed_lines[0], 5.0, "You are not printing the"
                " right result.")

    """
    def test_function_output(self):
        call = self.match_signature("average_numbers", 2)
        # TODO: python not recognizing exec's side effects
        exec(astor.to_source(call))
        self.assertEqual(average_numbers(1, 3), 2., "Do not change the "
                "original function definition")
        self.assertEqual(average_numbers(4, 6), 5., "Do not change the "
                "original function definition")
        self.assertEqual(average_numbers(1, 2), 1.5, "Do not change the "
                "original function definition")
    """

if __name__ == "__main__":
    unittest.main()

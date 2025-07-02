import ast
import io
import unittest
import unittest.mock

import asttest

class TestUnitTestsGradingCurve(asttest.ASTTest):

    def setUp(self):
        super().setUp("unit_tests_grading_curve.py")

    @unittest.mock.patch('sys.stdout')
    def test_required_syntax(self, output):
        func = self.match_signature("curve_grade", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check the instructions and try again.")
        self.assertFalse(self.function_prints(func), "Your function is "
                "printing. This function is not supposed to print - you are "
                "supposed to print its result OUTSIDE of the function "
                "definition.")

        self.assertNotIn("^", self.file, "That is not quite correct. What is "
                "the symbol for the Python exponent operator?")

        funcs = self.get_function_calls()
        self.assertGreaterEqual(funcs.count("curve_grade"), 3, "You should "
                "call curve_grade three times by writing at least three unit "
                "tests.")
        self.assertGreaterEqual(funcs.count("assert_equal"), 3, "You should "
                "write at least three unit tests using the assert_equal "
                "function.")

        self.ensure_coverage(["curve_grade"], .9)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_result(self, output):
        from unit_tests_grading_curve import curve_grade
        tests = [(64, 80), (0, 0), (100, 100)]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(message=test[0]):
                    result = curve_grade(test[0])
                    printed = output.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n{}".format(printed))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

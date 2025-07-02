import ast
import io
import unittest
import unittest.mock

import asttest

class TestReturnPrintReturnGreeting(asttest.ASTTest):

    def setUp(self):
        super().setUp("return_print_return_greeting.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, stdout):
        func = self.match_signature("return_greeting", 1)
        self.assertIsNotNone(func, "You are not defining the function "
                "correctly.")
        self.assertFalse(self.function_prints(func), "Your function is "
                "printing something. This function should not print, but "
                "instead, it should return the result.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 0, "Your "
                "function is not returning anything. It should return a "
                "value!")
        self.ensure_coverage(["return_greeting"], .9)
        unittests = self.find_function_calls("assert_equal")
        self.assertGreaterEqual(len(unittests), 1, "You did not write enough "
                "unit tests.")

    def test_correct_result(self):
        tests = [("Klaus", "Hello Klaus"), ("Ada Lovelace", "Hello Ada Lovelace")]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(name=test[0]):
                    from return_print_return_greeting import return_greeting
                    result = return_greeting(test[0])
                    printed = buffer.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n\n{}".format(printed))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

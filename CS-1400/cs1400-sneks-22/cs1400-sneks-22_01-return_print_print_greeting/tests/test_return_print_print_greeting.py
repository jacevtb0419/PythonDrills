import ast
import io
import unittest
import unittest.mock

import asttest

class TestReturnPrintPrintGreeting(asttest.ASTTest):

    def setUp(self):
        super().setUp("return_print_print_greeting.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, stdout):
        func = self.match_signature("print_greeting", 1)
        self.assertIsNotNone(func, "You did not implement the function "
                "signature correctly. Double-check its name and parameters.")
        self.assertTrue(self.function_prints(func), "Your function"
                " should be printing but it is not.")
        self.assertEqual(len(self.find_all(ast.Return)), 0, "Your function is "
                "returning something. It should not explicitly return any "
                "values!")

        for a_print in self.find_function_calls('print'):
            self.assertFalse(self.is_top_level(a_print), "You should not print"
                    " outside the function. Only the function should print.")

        funcs = self.get_function_calls()
        self.assertGreaterEqual(funcs.count("print_greeting"), 1, "You should "
                "call print_greeting one time by writing at least one unit "
                "test for it.")
        self.assertGreaterEqual(funcs.count("assert_equal"), 1, "You should "
                "write at least one unit test using the assert_equal "
                "function.")
        self.ensure_coverage(["print_greeting"], .9)

    @unittest.mock.patch("sys.stdout")
    def test_correct_result(self, stdout):
        from return_print_print_greeting import print_greeting
        tests = [("Klaus", "Hello Klaus"), ("Ada Lovelace", "Hello Ada Lovelace")]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(name=test[0]):
                    result = print_greeting(test[0])
                    printed = buffer.getvalue()
                    self.assertIsNone(result, "Your function should return "
                            "None.")
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n{}".format(printed))
                    self.assertEqual(printed.rstrip(), test[1], "Your function is not "
                            "printing the correct result. When given '{}' it "
                            "printed '{}', however, it should have printed "
                            "'{}'.".format(test[0], printed, test[1]))

if __name__ == "__main__":
    unittest.main()

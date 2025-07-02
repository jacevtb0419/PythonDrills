import ast
import io
import unittest
import unittest.mock

import asttest

class TestReturnPrintMakeReceipt(asttest.ASTTest):

    def setUp(self):
        super().setUp("return_print_make_receipt.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, stdout):
        func = self.match_signature("make_receipt", 1)
        self.assertIsNotNone(func, "You are not defining the function "
                "correctly.")
        self.assertTrue(self.function_prints(func), "Your function is "
                "not printing. This function should print the receipt as it "
                "creates it.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 0, "Your "
                "function is not returning anything. It should return a "
                "value!")

        for a_print in self.find_function_calls('print'):
            self.assertFalse(self.is_top_level(a_print), "You should not print"
                    " outside the function. Only the function should print.")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_correct_output(self, stdout):
        import return_print_make_receipt
        printed = stdout.getvalue().strip().split('\n')
        self.assertIn(printed, (["20", "18.0", "18.0", "16.2"],
                ["20.0", "18.0", "18.0", "16.2"]), "Your program is not "
                "printing the correct output. Check the instructions carefully"
                " and try again (you should print exactly four things).")

    @unittest.mock.patch("sys.stdout")
    def test_correct_result(self, stdout):
        from return_print_make_receipt import make_receipt
        tests = [(10, 9.0), (0, 0.0)]
        expected_prints = ['10\n9.0\n', '0\n0.0\n']
        for i in range(len(tests)):
            test = tests[i]
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(price=test[0]):
                    result = make_receipt(test[0])
                    printed = buffer.getvalue()
                    self.assertEqual(printed, expected_prints[i], "Your "
                            "function is not printing the correct output. When"
                            " given '{}' it printed '{}', however, it should "
                            "have printed '{}'.".format(test[0], printed,
                                expected_prints[i]))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))


if __name__ == "__main__":
    unittest.main()

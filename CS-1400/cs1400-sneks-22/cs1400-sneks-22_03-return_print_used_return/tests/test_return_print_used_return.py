import ast
import io
import unittest
import unittest.mock

import asttest

class TestReturnPrintUsedReturn(asttest.ASTTest):

    def setUp(self):
        super().setUp("return_print_used_return.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, stdout):
        self.assertIn('print(noun + " can pet other " + noun)', self.file, "Do"
                " not erase or change the print function call. Reset it and "
                "try again.")
        func = self.match_signature("pluralize", 1)
        self.assertIsNotNone(func, "You are not defining the function "
                "correctly.")
        self.assertFalse(self.function_prints(func), "Your function is "
                "printing something. This function should not print, but "
                "instead, it should return the result.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 0, "Your "
                "function is not returning anything. It should return a "
                "value!")

        self.ensure_coverage(["pluralize"], .9)
        unittests = self.find_function_calls("assert_equal")
        self.assertGreaterEqual(len(unittests), 1, "You did not write enough "
                "unit tests.")

    @unittest.mock.patch("sys.stdout")
    def test_correct_output(self, stdout):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        self.assertIn("Dogs can pet other Dogs", self.printed_lines, "Your "
                "program is not printing the right thing. Remember, your "
                "function should not print, but your program should print "
                "\"Dogs can pet other Dogs\" by calling your pluralize "
                "function and the given print call.")

    def test_correct_result(self):
        tests = [("dog","dogs"), ("cat", "cats"), ("","s")]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(word=test[0]):
                    from return_print_used_return import pluralize
                    result = pluralize(test[0])
                    printed = buffer.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n\n{}".format(printed))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()
'''
'''

import ast
import io
import unittest
import unittest.mock

import asttest

class TestUnitTestsVowelFunction(asttest.ASTTest):

    def setUp(self):
        super().setUp("unit_tests_vowel_function.py")

    @unittest.mock.patch('sys.stdout')
    def test_required_syntax(self, output):
        self.assertEqual(len(self.find_all(ast.If)), 0, "You do not need an "
                "if statement to solve this problem. Remember, it is meant to"
                " return True or False, so you should be returning a boolean "
                "value. What operators can be used to write an expression that"
                " evaluates to a boolean? In other words, what operators ask "
                "questions?")

        func = self.match_signature("begins_with_vowel", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check the instructions and try again.")

        self.assertNotIn('startswith', self.get_method_calls(), "While you are"
                " on the right track, using the .startswith() method is "
                "probably not the best idea. Since a string can only start "
                "with one character at a time, you'd have to call the "
                ".startswith() method for every possible vowel that the user "
                "might use in their string. Instead, you'll want to use the in"
                " operator here.")
        compares = self.find_all(ast.Compare)
        if (not compares or
            (compares and not compares[0].ops) or
            (compares and compares[0].ops and
             (ast.In not in (type(o) for o in compares[0].ops)))):
            self.fail("You will need to use the in operator.")

        funcs = self.get_function_calls()
        self.assertGreaterEqual(funcs.count("begins_with_vowel"), 2, "You should "
                "call begins_with_vowel three times by writing at least three unit "
                "tests.")
        self.assertGreaterEqual(funcs.count("assert_equal"), 2, "You should "
                "write at least three unit tests using the assert_equal "
                "function.")

        self.ensure_coverage(["begins_with_vowel"], .9)

    def test_correct_result(self):
        tests = [("A vowel", True),
                ("a vowel", True),
                ("No vowel", False),
                ("no vowel", False),
                ("1", False)]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                from unit_tests_vowel_function import begins_with_vowel
                with self.subTest(message=test[0]):
                    result = begins_with_vowel(test[0])
                    printed = buffer.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n{}".format(printed))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

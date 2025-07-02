import ast
import io
import unittest
import unittest.mock

import asttest

class TestUnitTestsBePolite(asttest.ASTTest):

    def setUp(self):
        super().setUp("unit_tests_be_polite.py")

    @unittest.mock.patch('sys.stdout')
    def test_required_syntax(self, output):
        func = self.match_signature("make_polite", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Please check the instructions and try again.")
        self.assertFalse(self.function_prints(func), "Your function is "
                "printing. This function is not supposed to print - you are "
                "supposed to print its result OUTSIDE of the function "
                "definition.")

        funcs = self.get_function_calls()
        self.assertGreaterEqual(funcs.count("make_polite"), 2, "You should "
                "call make_polite twice, by writing at least two unit tests.")
        self.assertGreaterEqual(funcs.count("assert_equal"), 2, "You should "
                "write at least two unit tests using the assert_equal "
                "function.")

        self.assertIn("Pet the dog", self.file, "For this drill, you should "
                "test your function twice with the arguments 'Pet the dog' and"
                " 'Walk the dog'")
        self.assertIn("Walk the dog", self.file, "For this drill, you should "
                "test your function twice with the arguments 'Pet the dog' and"
                " 'Walk the dog'")

        self.ensure_coverage(["make_polite"], .9)

    @unittest.mock.patch('sys.stdout')
    def test_correct_result(self, output):
        from unit_tests_be_polite import make_polite
        tests  = [("",", please"), ("Pet the dog", "Pet the dog, please"), ("Walk the dog","Walk the dog, please")]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(message=test[0]):
                    result = make_polite(test[0])
                    printed = output.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nYour unit tests "
                            "are not all passing: \n{}".format(printed))
                    self.assertEqual(result, test[1], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

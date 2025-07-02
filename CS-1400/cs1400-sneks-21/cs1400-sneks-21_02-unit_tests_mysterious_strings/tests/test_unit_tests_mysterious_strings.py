import ast
import io
import unittest
import unittest.mock

import asttest

class TestUnitTestsMysteriousStrings(asttest.ASTTest):

    def setUp(self):
        super().setUp("unit_tests_mysterious_strings.py")

    def test_required_syntax(self):
        self.assertLessEqual(len(self.find_all(ast.Return)), 1, "Your function"
                " should not explicitly return any values.")
        funcs = self.find_all(ast.FunctionDef)
        self.assertEqual(len(funcs), 1, "You should define a single function.")
        calls = self.find_all(ast.Call, funcs[0])
        self.assertEqual(len(calls), 1, "You should call only print inside of "
                "the function definition.")
        self.assertEqual(calls[0].func.id, "print", "Your function is not "
                "printing. This function is supposed to print.")
        self.assertIsNotNone(self.match_signature("mysterious_strings", 1),
                "Do not change the given function definition.")

    @unittest.mock.patch('sys.stdout')
    def test_correct_result(self, output):
        from unit_tests_mysterious_strings import mysterious_strings
        tests = [("Hello", "Ho"), ("Well", "Wl"), ("oHIo", "oo")]

        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(a_string=test[0]):
                    result = mysterious_strings(test[0])
                    printed = buffer.getvalue().strip()
                    self.assertIsNone(result, "Your function is not returning the "
                            "correct result. What is returned from a function "
                            "that does not explicitly return?")
                    self.assertEqual(printed, test[1], "Your function is not printing the correct result. "
                            "When given '{}' it printed '{}', however, it should "
                            "have printed '{}'.".format(test[0], printed, test[1]))

if __name__ == "__main__":
    unittest.main()

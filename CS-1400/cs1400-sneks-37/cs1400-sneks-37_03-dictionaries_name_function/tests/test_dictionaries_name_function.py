import ast
import unittest
import unittest.mock

import asttest

class TestDictionariesNameFunction(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionaries_name_function.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        fors = self.find_all(ast.For)
        self.assertEqual(len(fors), 0, "You are using a for loop, but you do "
                "not need to do so! Dictionaries give you the ability to "
                "lookup a value WITHOUT using iteration. Take advantage of "
                "that!")

        func = self.match_signature('get_name', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [({"Name": "Klaus"}, "Klaus"),
                ({"Name": "Wrex"}, "Wrex"),
                ({"Name": "Pumpkin", "Age": 2}, "Pumpkin")]
        for test in tests:
            with self.subTest(dictionary=test[0]):
                from dictionaries_name_function import get_name
                result = get_name(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
                1, "You did not write enough unit tests.")
        self.ensure_coverage(['get_name'], .9)

if __name__ == "__main__":
    unittest.main()

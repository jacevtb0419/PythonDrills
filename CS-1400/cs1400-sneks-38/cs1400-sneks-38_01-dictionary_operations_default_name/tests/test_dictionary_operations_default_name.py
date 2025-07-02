import ast
import unittest
import unittest.mock

import asttest

class TestDictionaryOperationsDefaultName(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_operations_default_name.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        fors = self.find_all(ast.For)
        self.assertEqual(len(fors), 0, "You are using a for loop, but you do "
                "not need to do so! Dictionaries give you the ability to "
                "lookup a value WITHOUT using iteration. Take advantage of "
                "that!")

        func = self.match_signature('get_default_name', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [({"Dog's Name": "Klaus"}, "Klaus"),
                ({"Dog's Name": "Wrex"}, "Wrex"),
                ({"Dog's Name": "Pumpkin", "Age": 2}, "Pumpkin"),
                ({"Age": 2}, "No dog"),
                ({}, "No dog")]
        for test in tests:
            with self.subTest(dictionary=test[0]):
                from dictionary_operations_default_name import get_default_name
                result = get_default_name(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
            2, "You did not write enough unit tests.")
        self.ensure_coverage(['get_default_name'], .9)

if __name__ == "__main__":
    unittest.main()

import ast
import unittest
import unittest.mock

import asttest

class TestNestedDataSumDictionary(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_sum_dictionary.py", False)

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        program_lines = [line.strip() for line in self.file.split("\n")]
        expected_lines = """for key, values in a_dictionary.items():\nnew = {}\nfor value in values:\nnew[key] = 0\nnew[key] = new[key] + value\nreturn new""".split("\n")
        for line in expected_lines:
            if line not in program_lines:
                self.fail("Do not add, remove, or change any of the originally"
                        " given lines, except to add indentation. Reset your "
                        "program from the starter code and try again.")

        self.tree = ast.parse(self.file)

        func = self.match_signature('sum_dictionary', 1)
        self.assertIsNotNone(func, "Do not delete or change the function "
                "definition.")

        tests = [({}, {}),
            ({'M1': []}, {'M1': 0}),
            ({'M1': [1,2]}, {'M1': 3}),
            ({'M1': [1,2], 'M2': [3,4]}, {'M1': 3, 'M2': 7})]
        for test in tests:
            with self.subTest(a_dictionary=test[0]):
                from nested_data_sum_dictionary import sum_dictionary
                result = sum_dictionary(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

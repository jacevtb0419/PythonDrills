import ast
import unittest
import unittest.mock

import asttest

class TestDictionaryPatternsWordFrequency(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_patterns_word_frequency.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        for name in self.find_all(ast.Name):
            self.assertNotEqual(name.id, "Counter", "You are not allowed to "
                    "use a Counter for this problem.")

        self.assertEqual(len(self.find_method_calls("upper")), 0, "You do"
                " not need to use the upper method. Just count the words, "
                "don't change them.")

        self.assertEqual(len(self.find_method_calls("lower")), 0, "You do"
                " not need to use the lower method. Just count the words, "
                "don't change them.")

        self.assertEqual(len(self.find_all(ast.List)), 0, "You should not be "
                "creating any list literals for this question.")

        func = self.match_signature('count_words', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter.")

        tests = [("apple", {"apple": 1}),
                ("", {"": 1}),
                ("apple,apple", {"apple": 2}),
                ("apple,banana", {"apple": 1, "banana":1}),
                ("apple,banana,apple", {"apple": 2, "banana":1}),
                ("dog,dog,dog,cat,cat", {"dog": 3, "cat": 2})]
        for test in tests:
            with self.subTest(words=test[0]):
                from dictionary_patterns_word_frequency import count_words
                result = count_words(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
            2, "You did not write enough unit tests.")
        self.ensure_coverage(['count_words'], .9)

if __name__ == "__main__":
    unittest.main()

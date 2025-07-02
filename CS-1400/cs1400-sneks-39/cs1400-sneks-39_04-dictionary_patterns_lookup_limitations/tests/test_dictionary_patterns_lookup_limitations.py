import ast
import unittest
import unittest.mock

import asttest

class TestDictionaryPatternsLookupLimitations(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_patterns_lookup_limitations.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        self.assertEqual(len(self.find_all(ast.Dict)), 0, "You do not need a "
                "dictionary to solve this problem!")
        func = self.match_signature("lookup_temperature", 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [(10, "Freezing"),
                (32, "Cold"),
                (40, "Cold"),
                (50, "Warm"),
                (60, "Warm"),
                (70, "Hot"),
                (90, "Hot")]
        for test in tests:
            with self.subTest(temperature=test[0]):
                from dictionary_patterns_lookup_limitations import lookup_temperature
                result = lookup_temperature(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        names = [n.id for n in self.find_all(ast.Name)]
        self.assertFalse(any(n[0].upper() == n[0] for n in names), "It is bad "
                "practice to start variable names with a capital letter (even "
                "if someone gives you a table that suggests that's a "
                "reasonable name). This isn't a universal rule, but capital "
                "letters suggest we are working with classes (which we will "
                "learn about next semester). For this problem, I recommend "
                "changing your variable names to not use capital letters at "
                "the start.")

        self.assertGreaterEqual(len(self.find_function_calls("assert_equal")),
                4, "You did not write enough unit tests.")
        self.ensure_coverage(['lookup_temperature'], .9)

if __name__ == "__main__":
    unittest.main()

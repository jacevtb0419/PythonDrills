import ast
import unittest

import asttest

class TestStringsSingleQuotes(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_single_quotes.py", False)

    def test_required_syntax(self):
        self.assertNotIn('''"Mrs. Flaversham said, "How are you today?"''',
                self.file, "You attempted to put double quotes around a string"
                " that already had double quotes. You can't do that, but "
                "single quotes would work!")
        self.tree = ast.parse(self.file)
        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "You should call "
                "the print function once.")
        self.assertEqual(len(calls[0].args), 1, "You need to print something.")
        self.assertIsInstance(calls[0].args[0], ast.Str, "You should print a "
                "string.")
        self.assertIn("How are you today?", calls[0].args[0].s, "Make sure you"
                " print the right thing.")
        self.assertIn('"How are you today?', self.file, "Mrs. Flaversham's "
                "quote should be printed and surrounded by double quotes.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should be printing a"
                " single line.")
        self.assertNotIn("Mrs. Flaversham said, 'How are you today?'",
                self.printed_lines[0], "You should be using double, not "
                "single, quotes!")
        self.assertNotIn("'", self.printed_lines[0], "You should not be "
                "printing any single quotes.")
        self.assertEqual(self.printed_lines[0],
                'Mrs. Flaversham said, "How are you today?"',
                "You printed the wrong string.")

if __name__ == "__main__":
    unittest.main()

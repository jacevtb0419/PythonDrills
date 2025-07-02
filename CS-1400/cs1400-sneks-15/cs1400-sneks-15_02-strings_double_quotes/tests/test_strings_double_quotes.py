import ast
import unittest

import asttest

class TestStringsDoubleQuotes(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_double_quotes.py", False)

    def test_required_syntax(self):
        self.assertNotIn(''''The dog's house is big and red.''', self.file,
                "You attempted to put single quotes around a string that "
                "already had single quotes. You should use double quotes on "
                "the outside!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should be printing a"
                " single line.")
        self.assertNotIn('"', self.printed_lines[0], "You should not be "
                "printing any double quotes.")
        self.assertEqual("The dog's house is big and red.",
                self.printed_lines[0],
                "You are printing the wrong string.")

if __name__ == "__main__":
    unittest.main()

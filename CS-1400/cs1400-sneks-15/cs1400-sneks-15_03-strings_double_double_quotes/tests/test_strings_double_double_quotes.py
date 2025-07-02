import ast
import unittest

import asttest

class TestStringsDoubleDoubleQuotes(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_double_double_quotes.py", False)

    def test_required_syntax(self):
        self.assertNotIn("'", self.file, "You may not use single quotes to "
                "solve this problem.")
        self.assertNotIn(
                '''"Then the student asked, "But how do I escape a string?"''',
                self.file, "You attempted to put double quotes around a string"
                " that already had double quotes. For this problem, you must "
                "escape the inner double quotes.")
        self.assertIn('\\"', self.file, "You must escape the double quotes to "
                "complete this drill.")
        self.assertNotIn('''"Then the student asked, \\"But how do I escape '''
                '''a string?"")''', self.file, "Remember to escape BOTH inner "
                "double quotes!")
        self.assertNotIn('''"Then the student asked, "But how do I escape a '''
                '''string?\\"")''', self.file, "Remember to escape BOTH inner "
                "double quotes!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertNotIn("'", self.printed_lines[0], "You should not be "
                "printing any single quotes.")
        self.assertEqual(self.printed_lines[0],
                'Then the student asked, "But how do I escape a string?"',
                "You are printing the wrong string.")

if __name__ == "__main__":
    unittest.main()

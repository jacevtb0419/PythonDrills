import ast
import unittest

import asttest

class TestErrorsSyntax(asttest.ASTTest):

    def setUp(self):
        super().setUp("errors_syntax.py")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print "
                '"Hello World".')
        self.assertEqual(self.printed_lines[0], "Hello World", "You printed "
                "the wrong thing.")

if __name__ == "__main__":
    unittest.main()

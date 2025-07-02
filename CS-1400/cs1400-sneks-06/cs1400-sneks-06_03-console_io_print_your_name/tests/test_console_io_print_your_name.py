import ast
import unittest

import asttest

class TestConsoleIoPrintYourName(asttest.ASTTest):

    def setUp(self):
        super().setUp("console_io_print_your_name.py")

    def test_required_syntax(self):
        pass

    def test_correct_result(self):
        self.exec_solution()
        printed = len(self.printed_lines)
        self.assertLess(printed, 2,
                'You should only print one thing. You are currently printing '
                'more than one thing.')
        self.assertEqual(printed, 1,
                "You are not printing anything. Make sure you use the print "
                "function.")
        self.assertNotIn("Hello World", self.printed_lines,
                "Okay, but don't print Hello World. Print something more "
                "interesting!")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestConsoleIoNowYouPrint(asttest.ASTTest):

    def setUp(self):
        super().setUp("console_io_now_you_print.py")

    def test_correct_result(self):
        self.exec_solution()
        printed = len(self.printed_lines)
        self.assertLess(printed, 2,
                'You should only print "Hello World". You are '
                        'currently printing more than one thing.')
        self.assertEqual(printed, 1, "You are not printing anything. Make "
                "sure you use the print function.")
        self.assertNotIn('"Hello World"', self.printed_lines,
                "Do not put the quotation marks in the string. Notice how "
                        "there are already quotation marks on the block? "
                        "Adding quotation marks inside is redundant!")
        self.assertEqual("Hello World", self.printed_lines[0],
                "You are not printing the right message.")

if __name__ == "__main__":
    unittest.main()

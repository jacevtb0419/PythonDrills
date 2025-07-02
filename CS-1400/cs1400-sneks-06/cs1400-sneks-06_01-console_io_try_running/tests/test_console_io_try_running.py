import ast
import unittest

import asttest

class TestConsoleIoTryRunning(asttest.ASTTest):

    def setUp(self):
        super().setUp("console_io_try_running.py")

    def test_required_syntax(self):
        pass

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(1, len(self.printed_lines), "You should only be printing once.")
        self.assertEqual("This is the output", self.printed_lines[0], 'You should not change the string for this problem. Leave it as "This is the output"')

if __name__ == "__main__":
    unittest.main()

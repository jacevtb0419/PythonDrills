import ast
import unittest

import asttest

class TestTryCodegrinderProblem(asttest.ASTTest):

    def setUp(self):
        super().setUp("try_codegrinder_problem.py")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(1, len(self.printed_lines), "You should only be printing once.")
        self.assertEqual("Welcome to CodeGrinder!", self.printed_lines[0], 'You should not change the string for this problem. Leave it as "Welcome to CodeGrinder!"')

if __name__ == "__main__":
    unittest.main()

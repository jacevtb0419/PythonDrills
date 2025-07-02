import ast
import unittest

import asttest

class TestWhileLoopsNoWhileLoops(asttest.ASTTest):

    def setUp(self):
        super().setUp("while_loops_no_while_loops.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.While)), 0, "You need to remove"
                " the WHILE statement.")
        self.assertNotEqual(len(self.find_all(ast.For)), 0, "You will need a "
                "FOR statement.")
        self.assertNotEqual(len(self.find_function_calls("range")), 0, "You "
                "will need to use the built-in range function.")
        self.assertNotIn("4950", self.file, "Do not embed the answer directly "
                "into your program. You should calculate it with a for loop.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing.")
        self.assertEqual(len(self.printed_lines), 1, "You should only be "
                "printing once.")
        self.assertEqual(self.printed_lines[0], 4950, "You are not printing "
                "the correct result.")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestErrorsType(asttest.ASTTest):

    def setUp(self):
        super().setUp("errors_type.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.BinOp)), 1, "Not a bad thought,"
                " but you aren't allowed to simply delete the addition here. "
                "If it helps, remember that although you can't add numbers to "
                "strings, you CAN add strings to strings. And anything can be "
                "a string!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print "
                '"Hello World".')
        self.assertEqual(self.printed_lines[0], "The Number 5", "You printed "
                "the wrong thing.")

if __name__ == "__main__":
    unittest.main()

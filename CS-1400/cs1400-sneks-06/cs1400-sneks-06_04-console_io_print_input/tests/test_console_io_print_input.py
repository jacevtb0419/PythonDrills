import ast
import unittest
from unittest.mock import patch

import asttest

class TestConsoleIoPrintInput(asttest.ASTTest):

    def setUp(self):
        super().setUp("console_io_print_input.py")

    def test_required_syntax(self):
        funcs = self.find_all(ast.Call)
        names = self.get_function_calls()
        self.assertEqual(len(funcs), 2, "You must have two function calls.")
        self.assertIn("input", names, "You must use the input function! Reset "
                "your program to get it back.")
        self.assertIn("print", names, "You will need to call the print "
                "function.")
        self.assertEqual(type(funcs[0].func), ast.Name, "Function is not of "
                "type ast.Name. Please send this error to ren.quinn@dixie.edu")
        self.assertEqual(funcs[0].func.id, "print", "You are not calling the "
                "print function correctly!")
        self.assertNotEqual(len(funcs[0].args), 0, "You must print something.")
        self.assertEqual(type(funcs[0].args[0].func), ast.Name, "Function is "
                "not of type ast.Name. Please send this error to "
                "ren.quinn@dixie.edu")
        self.assertEqual(funcs[0].args[0].func.id, "input", "You must call "
                "the input function inside your print.")
        self.assertEqual(len(funcs[0].args[0].args), 1, "You must not "
                "change the input function call. Replace your Python file with"
                "the one with the same name in the starter folder to reset "
                "your code and try again.")
        self.assertEqual(type(funcs[0].args[0].args[0].s), str, "You must "
                "not change the input function call.")
        self.assertEqual(funcs[0].args[0].args[0].s,
                "Type something, please: ",
                "You must not change the input function call.")

    @patch('builtins.input', side_effect=["words that I type"])
    def test_correct_result(self, mock_inputs):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should only print "
                "once.")
        self.assertEqual(self.printed_lines[0], "words that I type", "You "
                "must print your input!")

if __name__ == "__main__":
    unittest.main()

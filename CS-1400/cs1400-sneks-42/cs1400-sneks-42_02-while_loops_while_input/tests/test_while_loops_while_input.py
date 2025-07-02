import ast
import unittest
import unittest.mock

import asttest

class TestWhileLoopsWhileInput(asttest.ASTTest):

    def setUp(self):
        super().setUp("while_loops_while_input.py")

    def test_required_syntax(self):
        for func in ['sum', 'map', 'filter', 'reduce', 'max', 'min', 'max',
                'sorted', 'all', 'any', 'getattr', 'setattr', 'eval', 'exec',
                'iter']:
            self.assertEqual(len(self.find_function_calls(func)), 0, "You "
                    "cannot use the {} function for this problem.".format(func))

        self.assertNotEqual(len(self.find_all(ast.While)), 0, "You should be "
                "using a while loop.")
        self.assertEqual(len(self.find_all(ast.For)), 0, "You cannot use a for"
                " loop for this problem.")
        self.assertNotEqual(len(self.find_function_calls("input")), 0, "You "
                "will need to use the input function.")
        self.assertNotEqual(len(self.find_function_calls("print")), 0, "You "
                "will need to use the print function.")
        #elif prevent_operation("==") or prevent_operation("!="):
            #explain("You will not need to use the comparison operator. Take advantage of the truthiness of the user input variable. When is a string True?")

        tests = [["Apple", "Orange", ""],
                      ["Banana", "Pineapple", ""]]
        for test in tests:
            with unittest.mock.patch('builtins.input', side_effect=test):
                self.exec_solution()
                self.assertIn(self.printed_lines, (test, test[:-1]), "You are "
                        "not printing exactly the strings that the user "
                        "entered when they type\n{}."
                        .format('\n'.join(test)))
                self.printed_lines = []

if __name__ == "__main__":
    unittest.main()

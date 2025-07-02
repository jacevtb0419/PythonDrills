import ast
import io
import string
import re
import unittest
import unittest.mock

import asttest

class TestWhileLoopsChoose(asttest.ASTTest):

    def setUp(self):
        super().setUp("while_loops_choose.py")

    def test_choose(self):
        for func in ['sum', 'map', 'filter', 'reduce', 'len', 'max', 'min',
                'max', 'sorted', 'all', 'any', 'getattr', 'setattr', 'eval',
                'exec', 'iter']:
            self.assertEqual(len(self.find_function_calls(func)), 0, "You "
                    "cannot use the {} function for this problem.".format(func))

        self.assertNotEqual(len(self.find_all(ast.While)), 0, "You should be "
                "using a while loop.")
        self.assertNotEqual(len(self.find_all(ast.For)), 0, "You should be "
                "using a for loop.")
        self.assertNotEqual(len(self.find_function_calls("input")), 0, "You "
                "will need to use the input function.")
        self.assertNotEqual(len(self.find_function_calls("print")), 0, "You "
                "will need to use the print function.")

        func = self.match_signature('choose', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        # import function without triggering its execution
        lines = self.file.split('\n')
        #func_lines = lines[func.lineno-1:func.end_lineno] # only works in Python 3.8+
        linenos = self.get_function_linenos() # python 3.7
        func_lines = lines[linenos["choose"]["start"]-1:linenos["choose"]["end"]]

        func_text = '\n'.join(func_lines)
        exec(func_text, globals())


        tests = [ (["quit", "nap", "fight"], ["escape", "sleep", "fight"], "fight", "You can:\n- quit\n- nap\n- fight\nWhat will you do?"),
            (["walk" , "run", "jump"], ["fight", "nap", "quit", "run"], "run", "You can:\n- walk\n- run\n- jump\nWhat will you do?")]

        for options, inputs, expected, out in tests:
            context = ("when I call choose({}) and the user enters the "
                    "following inputs: {}\n"
                    .format(repr(options),'\n'.join(inputs)))

            with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                with unittest.mock.patch("builtins.input", side_effect=inputs+inputs):
                    try:
                        result = choose(options)
                    except StopIteration:
                        self.fail("Your function did not return when the user "
                                "typed a valid option.")
                    self.assertEqual(result, expected, "Your function returns {} "
                            "instead of {} ".format(result, expected)+context)

                    printed = mock_stdout.getvalue()
                    self.assertIn("You can:", printed, "You did not print out "
                            "the menu correctly.")
                    for option in options:
                        self.assertIn(option, printed, "You did not print out "
                                "each option.")

if __name__ == "__main__":
    unittest.main()

import ast
import string
import unittest

import asttest

class TestStringsStringOfStuff(asttest.ASTTest):

    def setUp(self):
        super().setUp("strings_string_of_stuff.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertEqual(len(assigns), 1, "You should have exactly one "
                "assignment statement.")
        self.assertIsInstance(assigns[0].value, ast.Str, "You should assign a "
                "string value to the variable.")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "You should call the print function "
                "exactly one time.")
        self.assertEqual(calls[0].func.id, "print", "The only function you "
                "should call is print.")
        self.assertEqual(len(calls[0].args), 1, "You should just print the one "
                "variable.")
        self.assertIsInstance(calls[0].args[0], ast.Name, "You should only "
                "print your variable, not the string literal directly or "
                "anything else.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print exactly"
                " one line.")
        self.assertIsInstance(self.printed_lines[0], str, "You must print out "
                "a string.")
        if not any(char in self.printed_lines[0] for char in string.ascii_letters):
            self.fail("You must have a letter in your string.")
        if not any(char in self.printed_lines[0] for char in string.digits):
            self.fail("You must have a number in your string.")
        if not any(char in self.printed_lines[0] for char in string.punctuation):
            self.fail("You must have a symbol in your string.")

if __name__ == "__main__":
    unittest.main()

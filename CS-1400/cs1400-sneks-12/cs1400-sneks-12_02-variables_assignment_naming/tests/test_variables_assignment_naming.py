import ast
import unittest

import asttest

class TestVariablesAssignmentNaming(asttest.ASTTest):

    def setUp(self):
        super().setUp("variables_assignment_naming.py")

    def test_required_syntax(self):
        compares = self.find_all(ast.Compare)
        for comp in compares:
            for op in comp.ops:
                if isinstance(op, ast.Eq):
                    self.fail("It looks like you are using the == operator. "
                            "The double-equals operator is for comparing two "
                            "values to see if they are equal. To assign a "
                            "value to a variable, you need a single-equals "
                            "(=) operator.")
        self.assertEqual(len(compares), 0, "You shouldn't be using any "
                "conditional logic for you solution.")

        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "You should use an assignment "
                "statement (with the = operator) to assign your name to a "
                "variable.")
        self.assertEqual(len(assigns), 1, "You should only use one assignment "
                "statement in your solution.")
        self.assertIsInstance(assigns[0].value, ast.Str, "It looks like "
                "you created a variable, but it does not have the right type. "
                "Make sure that you give your variable a string value, and "
                "not something else.")

        prints = False
        names = self.find_all(ast.Name)
        variable = None
        for name in names:
            if isinstance(name.ctx, ast.Store):
                variable = name.id
            elif name.id == 'print':
                prints = True

        calls = self.find_all(ast.Call)
        if prints:
            self.assertNotEqual(len(calls), 0, "I see that you tried to "
                    "print, but you didn't actually call the print function. "
                    "What syntax is always required to call a function?")
        else:
            self.assertNotEqual(len(calls), 0, "Don't forget to print your "
                    "name variable!")
        self.assertEqual(len(calls), 1, "You should only be calling a single "
                "function (print).")
        self.assertEqual(calls[0].func.id, "print", "You are calling a function "
                "but it's not print! You should only be calling the print "
                "function.")
        self.assertEqual(len(calls[0].args), 1, "You should only be printing "
                "one thing!")
        self.assertNotIsInstance(calls[0].args[0], ast.Num, "You should print "
                "your name variable, not your name directly as a string.")
        self.assertIsInstance(calls[0].args[0], ast.Name, "You should print "
                "your name variable.")
        self.assertEqual(calls[0].args[0].id, variable, "You should print your "
                "{} variable.".format(variable))

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        name = self.printed_lines[0]
        self.assertIsInstance(name, str, "You must use a string to represent "
                "your name.")
        self.assertLess(len(name), 200, "I don't think that {} is a valid "
                "name.".format(name))
        self.assertGreater(len(name), 0, "I don't think that {} is a valid "
                "name.".format(name))

if __name__ == "__main__":
    unittest.main()

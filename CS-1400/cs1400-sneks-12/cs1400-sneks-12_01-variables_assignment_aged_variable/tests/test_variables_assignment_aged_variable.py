import ast
import unittest

import asttest

class TestVariablesAssignmentAgedVariable(asttest.ASTTest):

    def setUp(self):
        super().setUp("variables_assignment_aged_variable.py")

    def test_required_syntax(self):
        compares = self.find_all(ast.Compare)
        for comp in compares:
            for op in comp.ops:
                if isinstance(op, ast.Eq):
                    self.fail("It looks like you are using the == operator. "
                            "The double-equals operator is for comparing two "
                            "numbers to see if they are equal. To assign a "
                            "value to a variable, you need a single-equals "
                            "(=) operator.")
        self.assertEqual(len(compares), 0, "You shouldn't be using any "
                "conditional logic for you solution.")

        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "You should use an assignment "
                "statement (with the = operator) to assign your age to a "
                "variable.")
        self.assertEqual(len(assigns), 1, "You should only use one assignment "
                "statement in your solution.")
        self.assertNotIsInstance(assigns[0].value, ast.Str, "It looks like "
                "you have created a variable, but it does not have the right "
                "type. Make sure that you give your variable an integer "
                "value, and not something else. For instance, did you use a "
                "string value instead of a number?")
        self.assertIsInstance(assigns[0].value, ast.Num, "It looks like "
                "you created a variable, but it does not have the right type. "
                "Make sure that you give your variable an integer value, and "
                "not something else.")

        prints = False
        names = self.find_all(ast.Name)
        for name in names:
            if isinstance(name.ctx, ast.Store):
                self.assertEqual(name.id, "age", 'You should name your new '
                        'variable "age" (without quotes).')
            elif name.id == 'print':
                prints = True

        calls = self.find_all(ast.Call)
        if prints:
            self.assertNotEqual(len(calls), 0, "I see that you tried to "
                    "print, but you didn't actually call the print function. "
                    "What syntax is always required to call a function?")
        else:
            self.assertNotEqual(len(calls), 0, "Don't forget to print your "
                    "age variable!")
        self.assertEqual(len(calls), 1, "You should only be calling a single "
                "function (print).")
        self.assertEqual(calls[0].func.id, "print", "You are calling a function "
                "but it's not print! You should only be calling the print "
                "function.")
        self.assertEqual(len(calls[0].args), 1, "You should only be printing "
                "one thing!")
        self.assertNotIsInstance(calls[0].args[0], ast.Num, "You should print "
                "your age variable, not your age directly as an integer.")
        self.assertIsInstance(calls[0].args[0], ast.Name, "You should print "
                "your age variable.")
        self.assertEqual(calls[0].args[0].id, "age", "You should print your "
                "age variable.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        age = self.printed_lines[0]
        self.assertNotIsInstance(age, float, "While ages can be represented "
                "as floats, the problem asks for your age in years as an "
                "integer.")
        self.assertIsInstance(age, int, "You must use an integer to represent "
                "your age in years.")
        self.assertLess(age, 200, "I don't think that {} is a valid age. But "
                "you look great for your age!".format(age))
        self.assertGreater(age, 0, "I don't think that {} is a valid "
                "age.".format(age))

if __name__ == "__main__":
    unittest.main()

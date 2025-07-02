import ast
import unittest

import asttest

class TestVariablesAssignmentExtract(asttest.ASTTest):

    def setUp(self):
        super().setUp("variables_assignment_extract.py")

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
                "statement (with the = operator).")
        self.assertEqual(len(assigns), 1, "You should only use one assignment "
                "statement in your solution.")
        self.assertIsInstance(assigns[0].value, ast.Num, "It looks like you "
                "created a variable, but it does not have the right type. "
                "Make sure that your variable is assigned the integer value "
                "in the starter code, and not something else.")

        prints = False
        names = self.find_all(ast.Name)
        for name in names:
            if isinstance(name.ctx, ast.Store):
                self.assertEqual(name.id, "score", 'You should name your '
                        'variable "score" (without quotes).')
            elif name.id == 'print':
                prints = True

        calls = self.find_all(ast.Call)
        if prints:
            self.assertNotEqual(len(calls), 0, "I see that you tried to "
                    "print, but you didn't actually call the print function. "
                    "What syntax is always required to call a function?")
        else:
            self.assertNotEqual(len(calls), 0, "Don't forget to print the "
                    "score variable!")
        self.assertEqual(len(calls), 1, "You should only be calling a single "
                "function (print).")
        self.assertEqual(calls[0].func.id, "print", "You are calling a function "
                "but it's not print! You should only be calling the print "
                "function.")
        self.assertEqual(len(calls[0].args), 1, "You should only be printing "
                "one thing!")
        self.assertNotIsInstance(calls[0].args[0], ast.Num, "You should print "
                "the score variable, not 103 directly.")
        self.assertIsInstance(calls[0].args[0], ast.Name, "You should print "
                "the score variable.")
        self.assertEqual(calls[0].args[0].id, "score", "You should print the "
                "score variable.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You should be "
                "printing something!")
        score = self.printed_lines[0]
        self.assertEqual(score, 103, "Keep the score the same (103).")

if __name__ == "__main__":
    unittest.main()

'''
integer_variables = student.get_names_by_type(int)
if len(integer_variables) == 0:
    if len(student.data) > 4:
        if ast.find_all("Str"):
            gently("It looks like you may have created a variable, but it does not have the right type. Make sure that you give your variable an integer value, and not something else. For instance, did you use a string value instead of a number?")
        else:
            gently("It looks like you may have created a variable, but it does not have the right type. Make sure that you give your variable an integer value, and not something else.")
    else:
        gently("You need to create and initialize a new *integer* variable. You can do that using an assignment statement (the single <code>=</code> symbol).")

compares = ast.find_all('Compare')
if compares:
    if "Eq" in [o.ast_name for o in compares[0].ops]:
        explain("It looks like you are using the <code>==</code> operator. The double-equals operator is for comparing two numbers to see if they are equal. To assign a value to a variable, you need a single-equals (<code>=</code>) operator.", 'analyzer')

ensure_prints(1)
if not only_printing_variables():
    gently("You should only be printing variables, not values!")
if integer_variables:
    value = student.data[integer_variables[0]]
    if str(value) in get_output():
        if value == 103:
            set_success()
        else:
            gently("Keep the score the same (103).")
    else:
        gently("Remember to print your variable!")
'''

import ast
import unittest

import asttest

class TestVariablesAssignmentCombining(asttest.ASTTest):

    def setUp(self):
        super().setUp("variables_assignment_combining.py")

    def test_required_syntax(self):
        numbers = self.find_all(ast.Num)
        self.assertGreaterEqual(len(numbers), 2, "You should use both the "
                "numbers 432 and 6 in your program.")
        self.assertIn(numbers[0].n, [432, 6], "You should only use the numbers"
                " 432 and 6 in your program.")
        self.assertIn(numbers[1].n, [432, 6], "You should only use the numbers"
                " 432 and 6 in your program.")
        self.assertNotEqual(numbers[0].n, numbers[1].n, "You should only use "
                "the numbers 432 and 6 in your program.")
        self.assertEqual(len(numbers), 2, "You used more numbers than you "
                "needed. You should only use the numbers 432 and 6 in your "
                "program.")

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
                "conditional logic for your solution.")

        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 2, "You should write two "
                "assignment statements (with the = operator).")
        self.assertEqual(len(assigns), 2, "You only need two assignment "
                "statements in your solution.")
        for assign in assigns:
            self.assertIsInstance(assign.value, ast.Num, "It looks like you "
                    "created a variable, but it does not have the right type. "
                    "Make sure that your variable is assigned one of the integer "
                    "value in the starter code, and not something else.")

        names = self.find_all(ast.Name)
        self.assertEqual(len(names), 5, "You need two variables and ")

        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "You should only be calling a single "
                "function (print).")
        self.assertEqual(calls[0].func.id, "print", "You are calling a function "
                "but it's not print! You should only be calling the print "
                "function.")
        self.assertEqual(len(calls[0].args), 1, "You should only be printing "
                "one thing!")

        self.assertIsInstance(calls[0].args[0], ast.BinOp, "The expression to "
                "calculate the average miles per hour should be used as the "
                "only argument to print.")
        self.assertIsInstance(calls[0].args[0].op, ast.Div, "You should be "
                "dividing, not some other operation.")
        self.assertIsInstance(calls[0].args[0].left, ast.Name, "Use the "
                "variables to calculate the speed, not the literal values!")
        self.assertIsInstance(calls[0].args[0].right, ast.Name, "Use the "
                "variables to calculate the speed, not the literal values!")

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "Remember to print the"
                " result!")
        result = self.printed_lines[0]
        self.assertEqual(result, 432/6, "The result should be "
                "{}.".format(432/6))

if __name__ == "__main__":
    unittest.main()

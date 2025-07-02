import ast
import unittest

import asttest

class TestStatementsExpressionsArranging(asttest.ASTTest):

    def setUp(self):
        super().setUp("statements_expressions_arranging.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.Assign)), 6, "Do not delete or "
                "add any assignment statements! Simply fill in the blanks with"
                " the proper expressions.")
        self.assertEqual(len(self.find_all(ast.Num)), 4, "You have the wrong "
                "number of integer literals. Reread the instructions and try "
                "again.")
        calls = self.find_all(ast.Call)
        self.assertEqual(len(calls), 1, "You should only be calling a single "
                "function (print).")
        self.assertEqual(calls[0].func.id, "print", "You are calling a function "
                "but it's not print! You should only be calling the print "
                "function.")
        self.assertEqual(len(calls[0].args), 1, "You should only be printing "
                "one thing!")
        self.assertIsInstance(calls[0].args[0], ast.BinOp, "The expression to "
                "calculate the cost per square foot should be the only "
                "argument to print.")

        values = {'left_width':5,'right_width':5,'height':10,'total_cost':100}
        formulas = {'width':'adding the widths of the two bedrooms/boxes',
                'area':'multiplying the height by the width'}
        assigns = self.find_all(ast.Assign)
        for assign in assigns:
            self.assertEqual(len(assign.targets), 1, "Your assignment "
                    "statement is incorrect for {}."
                    .format([t.id for t in assign.targets]))
            self.assertIsInstance(assign.targets[0], ast.Name, "Your "
                    "assignment statement is incorrect for {}."
                    .format([t.id for t in assign.targets]))
            if (assign.targets[0].id in values
                    and isinstance(assign.value, ast.Num)):
                self.assertEqual(assign.value.n,
                        values[assign.targets[0].id], "You are assigning "
                            "an incorrect value to the {} variable. "
                            "Double-check the instructions to obtain the "
                            "correct values for each variable."
                            .format(assign.targets[0].id))
            elif assign.targets[0].id in formulas:
                var = assign.targets[0].id
                self.assertIsInstance(assign.value, ast.BinOp, "The variable "
                        "{} should be assigned the result of {}. Please review"
                        " the formulas in the instructions."
                        .format(var, formulas[var]))
                if var == "width":
                    self.assertIsInstance(assign.value.op, ast.Add, "The "
                    "formula for the width requires adding the two smaller "
                    "widths. Please review the formulas in the instructions.")
                elif var == "area":
                    self.assertIsInstance(assign.value.op, ast.Mult, "The "
                    "formula for the area requires multiplying the heigth and "
                    "width. Please review the formulas in the instructions.")
            else:
                self.fail("You are assigning to the wrong variable: {}."
                        .format(assign.targets[0].id))

    def test_correct_result(self):
        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "Remember to print the"
                " result! Make sure you type the right formula in the "
                "parenthesis as an argument to print.")
        self.assertEqual(self.printed_lines[0], 1.0, "You are not printing the"
                " right thing (double-check your math to match the given "
                "formulas).")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestNestedDataSummingLodod(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_summing_lodod.py")

    def test_required_syntax(self):
        self.assertIn("forecast", [assign.targets[0].id for assign in
            self.find_all(ast.Assign) if isinstance(assign.targets[0], ast.Name)],
            "Do not remove the forecast variable.")

        nums = [n.n for n in self.find_all(ast.Num)]
        self.assertNotIn(7, nums, "Do not embed the solution in your "
                "program. You should calculate it using a for loop instead.")

        self.assertEqual(len(self.find_function_calls("sum")), 0, "You are not"
                " allowed to use the sum() function for this assignment. ")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You will need a for loop.")
        self.assertNotEqual(len(fors), 0, "You will need a for loop.")
        self.assertEqual(len(fors), 1, "You should only use a single for loop."
                " Remember, you do not need to iterate through the keys of the"
                " dictionary! Instead, how should you access a (single) "
                "specific value, even if it is nested in multiple "
                "dictionaries? (Think expressions!)")

        loop = fors[0]
        if isinstance(loop.target, ast.Name) and loop.target.id in ("Weather",
                "Rainfall", "rainfall"):
            self.fail("{} is not a good variable name for the iteration "
                    "variable. Choose a more descriptive name for a singular "
                    "item in a list of games.".format(loop.target.id))

        subscripts = self.find_all(ast.Subscript, loop)
        self.assertGreater(len(subscripts), 1, "You will need to use at least"
                " one dictionary lookup.")
        self.assertEqual(len(subscripts), 2, "You only need to use two "
                "dictionary lookups.")

        str_values = [s.s for s in self.find_all(ast.Str, loop)]
        if "weather" in str_values or "rainfall" in str_values:
            self.fail("Remember, capitalization matters when it comes to "
                    "keys!")

        names = [n.id for n in self.find_all(ast.Name, loop)]
        if "Weather" in names or "Rainfall" in names:
            self.fail("You should use a string literal value to look up the "
                    "name, not a variable.")
        if "Weather" not in str_values or "Rainfall" not in str_values:
            self.fail("You are not using the right keys.")

        adds = self.find_all(ast.Add)
        self.assertNotEqual(len(adds), 0, "You should use an add operation in "
                "your program.")
        self.assertEqual(len(adds), 1, "You should only use one add operation "
                "in your program.")

        prints = self.find_function_calls('print')
        self.assertNotEqual(len(prints), 0, "You are not using the print "
                "function!")
        self.assertEqual(len(prints), 1, "You should only need to call the "
                "print function once.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything")
        self.assertEqual(len(self.printed_lines), 1, "You have printed out too"
                " many things. Are you printing inside of the for loop when "
                "you should be printing after it?")
        self.assertEqual(self.printed_lines[0], 7, "You are not printing out "
                "the right value.")

if __name__ == "__main__":
    unittest.main()

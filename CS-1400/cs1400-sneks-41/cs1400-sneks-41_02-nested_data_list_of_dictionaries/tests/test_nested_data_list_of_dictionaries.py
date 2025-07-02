import ast
import unittest

import asttest

class TestNestedDataListOfDictionaries(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_list_of_dictionaries.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 1, "Do not remove the course "
                "dictionary variable.")

        str_values = [s.s for s in self.find_all(ast.Str)]
        for literal in ["Beauty and the Beast", "Hercules", "Up"]:
            self.assertNotEqual(str_values.count(literal), 0, "Do not modify "
                    "or delete the movies dictionary.")
            self.assertEqual(str_values.count(literal), 1, "The string {} "
                    "should only appear in your program once, when the "
                    "original variable course is defined. Think about how to "
                    "access a dictionary value using a look up."
                    .format(repr(literal)))

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You will need a FOR loop.")
        self.assertEqual(len(fors), 1, "You should only use a single for "
                "loop. Remember, you do not need to iterate through the keys "
                "of the dictionary! Instead, how should you access a (single)"
                " specific value?")

        loop = fors[0]
        str_values = [s.s for s in self.find_all(ast.Str, loop)]
        self.assertNotIn("name", str_values, "Remember, capitalization matters"
                " when it comes to keys!")

        names = [n.id for n in self.find_all(ast.Name, loop)]
        if isinstance(loop.target, ast.Name) and loop.target.id.lower() == "name":
            self.fail("{} is not a good variable name for the iteration "
                    "variable. Choose a more descriptive name for a singular "
                    "item in a list of movies.".format(loop.target.id))
        if "name" in names or "Name" in names:
            self.fail("You should use a string literal value to look up the "
                    "name, not a variable.")
        self.assertIn("Name", str_values, "You are not using the right key.")

        prints = self.find_function_calls('print')
        self.assertNotEqual(len(prints), 0, "You are not using the print "
                "function!")
        self.assertEqual(len(prints), 1, "You should only need to write the "
                "print function once. That's the benefit of using a loop in "
                "this case, right?")
        self.assertNotEqual(len(self.find_all(ast.Call, loop)), 0, "The print "
                "function is meant to be used inside of the for loop.")


        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything")
        self.assertGreaterEqual(len(self.printed_lines), 3, "You printed "
                "out too few things.")
        self.assertEqual(len(self.printed_lines), 3, "You have printed out too"
                " many things.")
        self.assertEqual(sorted(self.printed_lines),
                sorted(["Beauty and the Beast", "Hercules", "Up"]),
                "You are not printing out the right values.")

if __name__ == "__main__":
    unittest.main()

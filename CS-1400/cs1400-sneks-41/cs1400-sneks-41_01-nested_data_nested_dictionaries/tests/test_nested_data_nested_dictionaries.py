import ast
import unittest

import asttest

class TestNestedDataNestedDictionaries(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_nested_dictionaries.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 1, "Do not remove the course "
                "dictionary variable.")

        self.assertGreaterEqual(len(self.find_all(ast.Subscript)), 5, "You "
                "will need to do more dictionary lookups and list indexing.")

        str_values = [s.s for s in self.find_all(ast.Str)]
        for literal in ["Steve Jobs", "Bill Gates", "Fundamentals of Computer Programming", "Introduction", "Installing Python"]:
            if str_values.count(literal) > 1:
                self.fail("The string {} should only appear in your program "
                        "once, when the original variable course is defined. "
                        "Think about how to access a dictionary value using a "
                        "look up.".format(repr(literal)))
        self.assertGreaterEqual(str_values.count("Instructors"), 2, "The key "
                "{} should be used.".format(repr('Instructors')))

        num_values = [n.n for n in self.find_all(ast.Num)]
        self.assertIn(0, num_values, "You will need to index the first "
                "element of a list.")
        for literal in ["Assignments", "Day 2", "Title"]:
            self.assertGreaterEqual(str_values.count(literal), 2, "The key {} "
                "should be used.".format(repr(literal)))

        self.exec_solution()
        self.assertGreaterEqual(len(self.printed_lines), 2, "You are not "
                "printing two answers.")
        self.assertEqual(len(self.printed_lines), 2, "You are printing too "
                "many things.")
        self.assertEqual("Steve Jobs", self.printed_lines[0], "You did not "
                "print out the first instructor.")
        self.assertEqual("Installing Python", self.printed_lines[1], "You did "
                "not print out the title of the Assignment on Day 2.")

if __name__ == "__main__":
    unittest.main()

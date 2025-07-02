import ast
import unittest

import asttest

class TestBuiltinFunctionsParametersArguments(asttest.ASTTest):

    def setUp(self):
        super().setUp("builtin_functions_parameters_arguments.py")

    def test_required_syntax(self):
        starter = "Every new beginning comes from some other beginning's end."
        strs = [s.s for s in self.find_all(ast.Str)]
        self.assertGreaterEqual(len(strs), 1, "Do not delete the given string."
                " Reload the starter code and try again.")
        self.assertIn(starter, strs, "Do not delete the instructor provided "
                "string. Reset your program.")
        self.assertGreaterEqual(len(strs), 2, "You will need to choose a "
                "suffix to test for.")
        self.assertEqual(len(strs), 2, "You have created too many strings")
        #self.assertTrue(strs[0].endswith(strs[1]), "Remember, create a string "
                #"that will cause the expression to evaluate to True.")
        #self.assertFalse(strs[1].endswith(strs[0]), "Remember, create a string"
                #" that will cause the expression to evaluate to True.")
        self.assertNotIn("True", strs, "Do not use 'True' or 'False' as "
                "strings in this program.")
        self.assertNotIn("False", strs, "Do not use 'True' or 'False' as "
                "strings in this program.")
        self.assertEqual(len(self.find_all(ast.NameConstant)), 0, "Do not use "
                "any boolean literals or None values in this program.")
        attrs = self.find_all(ast.Attribute)
        self.assertEqual(len(attrs), 1, "Make sure you use the endswith "
                "method and no other function except print.")
        self.assertEqual(attrs[0].attr, "endswith", "Make sure you use the "
                "endswith function.")

    def test_correct_result(self):
        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "You should print one "
                "line.")
        self.assertNotEqual(self.printed_lines[0], False, "Remember, choose a "
                "string that will cause the expression to evaluate to True.")
        self.assertEqual(self.printed_lines[0], True, "You should be printing "
                "the result of the conditional expression (i.e. a boolean "
                "value).")

if __name__ == "__main__":
    unittest.main()

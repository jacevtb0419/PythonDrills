import ast
import importlib
import unittest
import unittest.mock

import asttest

class TestDefiningFunctionsCall(asttest.ASTTest):

    def setUp(self):
        super().setUp("ada_stats.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        assigns = self.find_all(ast.Assign)
        found_q = False
        found_a = False
        for assign in assigns:
            if assign.targets[0].id == "QUESTION":
                found_q = True
                self.assertIsInstance(assign.value, ast.Str, "Your survey "
                        "question should be a string.")
                self.assertNotEqual(assign.value.s, "", "You did not "
                        "enter your survey question correctly.")
            elif assign.targets[0].id == "ANSWERS":
                found_a = True
                question = "You did not enter your survey question correctly."
                self.assertIsInstance(assign.value, ast.List, "Your survey "
                        "answers should be represented as a list of numbers.")
                self.assertGreaterEqual(len(assign.value.elts), 16, "You did "
                        "not record enough survey responses.")
        self.assertTrue(found_q, "Could not find the variable QUESTION. Make "
                "sure you assign your survey question as a string to a "
                "variable called QUESTION.")
        self.assertTrue(found_a, "Could not find the variable ANSWERS. Make "
                "sure you assign your survey responses as a list to a "
                "variable called ANSWERS.")

        goal = "The goal is to learn to implement it on your own!"
        imports = [name.name for i in self.find_all(ast.Import) for name in i.names]
        for import_ in imports:
            self.assertNotIn(import_, ['pandas', 'numpy', 'statistics'], "You "
                    "are not allowed to the {} module for this assignment. "
                    .format(import_) + goal)
        self.assertEqual(len(self.find_function_calls("sum")), 0, "You are not"
                " allowed to use the sum() function for this assignment. " +
                goal)
        self.assertEqual(len(self.find_function_calls("len")), 0, "You are not"
                " allowed to use the len() function for this assignment. " +
                goal)
        self.assertEqual(len(self.find_all(ast.ListComp)), 0, "You are not "
                "allowed to use list comprehensions for this assignment. First"
                " show us that you understand how to use a basic for loop.")

        # ensure no nested function definitions
        for func_def in self.find_all(ast.FunctionDef):
            self.assertEqual(len(self.find_all(ast.FunctionDef, func_def)), 1,
                    "It looks like you've defined a function *inside* of the "
                    "{}() function. The DEF keyword of each function should be"
                    " completely unindented.".format(func_def.name))

        self.assertEqual(len(self.find_all(ast.Global)), 0, "You should not be"
                " using the global keyword.")
        self.assertEqual(len(self.find_all(ast.Nonlocal)), 0, "You should not be"
                " using the nonlocal keyword.")

        func = self.assert_function("count", 1)
        self.assertNotEqual(len(self.find_all(ast.For, func)), 0, "You'll want"
                " to use a for loop to count the numbers in the list.")
        self.unittest_function("count", [
            ([], 0),
            ([1], 1),
            ([1,2], 2),
            ([100, 100, 100], 3),
            ([5, 3, 6, 3, 5, 3, 2, 8], 8)])

        self.assert_function('summate', 1)
        self.unittest_function('summate', [
            ([], 0),
            ([1], 1),
            ([1,2], 3),
            ([100, 100, 100], 300),
            ([8, 2, 6, 4, 5, 3, 2], 30)])

        func = self.assert_function('mean', 1)
        self.assertEqual(len(self.find_all(ast.For, func)), 0, "Sure, it works"
                " to use a for loop to count and add up the numbers in the "
                "list, but you already implemented functions to do that. Why "
                "not use them?")
        self.assertNotEqual(len(self.find_all(ast.If, func)), 0, "Don't forget"
                " to check if the numbers list is empty in your mean function.")
        calls = [c.func.id for c in self.find_all(ast.Call, func) if isinstance(c.func, ast.Name)]
        self.assertIn("round", calls, "Don't forget to round the average to "
                "two decimal places.")
        self.unittest_function('mean', [
            ([1], 1.0),
            ([1,2], 1.5),
            ([100, 200, 300], 200.0),
            ([5, 10, 9], 8.0),
            ([], None),
            ([1, 5, 6.4], 4.13)])

        self.assert_function('square', 1)
        self.unittest_function('square', [
            ([1], [1]),
            ([1,2], [1,4]),
            ([10, 15, 20], [100, 225, 400]),
            ([5, 10, 9, -5], [25, 100, 81, 25]),
            ([], [])])

        self.assert_function('standard_deviation', 1)
        self.unittest_function('standard_deviation', [
            ([], None),
            ([1], None),
            ([0, 10], 7.0710678118654755),
            ([5, 5, 5, 5, 5], 0.0),
            ([10, 15, 20], 5.0),
            ([5, 8, 3, 4, 6, 3, 2, 6], 1.9955307206712847)])

    def assert_function(self, name, num_params):
        func = self.match_signature(name, num_params)
        self.assertIsNotNone(func, "Cannot find function {} with the correct "
                "number of parameters ({}).".format(name, num_params))
        self.assertEqual(len(self.find_all(ast.Pass, func)), 0, "Function {} "
                "not yet implemented.".format(name))
        #assertHasFunction(student, 'count', args=['list[int]'], returns='int', score=.5)
        return func

    def unittest_function(self, name, tests):
        for test in tests:
            #with self.subTest(numbers=test[0]):
            ada_stats = importlib.import_module("ada_stats")
            func = getattr(ada_stats, name)
            result = func(test[0])
            if isinstance(test[1], list):
                self.assertEqual(result, test[1], "Function {}() is "
                        "not returning the correct result. When given {} it "
                        "returned {}, however, it should have returned {}."
                        .format(name, test[0], result, test[1]))
            else:
                self.assertAlmostEqual(result, test[1], 4, "Function {}() is "
                        "not returning the correct result. When given {} it "
                        "returned {}, however, it should have returned {}."
                        .format(name, test[0], result, test[1]))

if __name__ == "__main__":
    unittest.main()

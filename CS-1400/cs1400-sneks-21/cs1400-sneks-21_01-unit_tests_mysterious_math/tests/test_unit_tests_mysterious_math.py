import ast
import unittest
import unittest.mock

import asttest

class TestUnitTestsMysteriousMath(asttest.ASTTest):

    def setUp(self):
        super().setUp("unit_tests_mysterious_math.py")

    def test_required_syntax(self):
        func_defs = self.find_all(ast.FunctionDef)
        self.assertEqual(len(func_defs), 1, "You should define exactly one "
                "function.")
        calls_in_func = self.find_all(ast.Call, func_defs[0])
        for c in calls_in_func:
            if isinstance(c.func, ast.Name) and c.func.id == "print":
                self.fail("Your function is printing. This function is not "
                        "supposed to print - you are only supposed to print "
                        "its result OUTSIDE of the function definition.")
        self.assertEqual(len(calls_in_func), 0, "You do not need to call any "
                "function inside of your function to get it to work.")
        self.assertGreaterEqual(len(self.find_all(ast.Return)), 1, "Your "
                "function is not returning. It needs to return something!")
        self.assertIsNotNone(self.match_signature("mysterious_math", 2), "Do "
                "not change the name of the function or its parameters, simply"
                " change what the function does with the parameters within its"
                " body.")

    def test_correct_result(self):
        self.exec_solution()
        self.assert_prints(msg="You should call the function at least once.")

    @unittest.mock.patch('sys.stdout')
    def test_mysterious_math(self, mock):
        from unit_tests_mysterious_math import mysterious_math
        tests = [(2, 3, 6), (3, 1, 3), (2, 0, 0), (0, 4, 0)]
        for test in tests:
            result = mysterious_math(test[0], test[1])
            self.assertEqual(result, test[2], "Your function is not returning"
                    " the correct result. When given {} and {} it returned {} "
                    "but should have returned {}."
                    .format(test[0], test[1], result, test[2]))

if __name__ == "__main__":
    unittest.main()

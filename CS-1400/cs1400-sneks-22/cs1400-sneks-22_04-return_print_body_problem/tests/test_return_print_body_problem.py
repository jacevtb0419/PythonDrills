import ast
import io
import unittest
import unittest.mock

import asttest

class TestReturnPrintBodyProblem(asttest.ASTTest):

    def setUp(self):
        super().setUp("return_print_body_problem.py")

    def test_required_syntax(self):
        func = self.match_signature("calculate_area", 2)
        self.assertIsNotNone(func, "You have deleted or renamed the "
                "calculate_area function. Reset your program!")

    def test_correct_result(self):
        tests = [(10, 10, 100), (2, 2, 4)]
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buffer:
                with self.subTest(height=test[0], width=test[1]):
                    from return_print_body_problem import calculate_area
                    result = calculate_area(test[0], test[1])
                    printed = buffer.getvalue()
                    self.assertNotIn("FAILURE", printed, "\n\nThe unit tests "
                            "are not all passing: \n\n{}".format(printed))
                    self.assertEqual(result, test[2], "Your function is not "
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format((test[0], test[1]), result, test[2]))

if __name__ == "__main__":
    unittest.main()

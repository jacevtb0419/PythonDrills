import ast
import unittest

import asttest

class TestDictionaryOperationsDictionaryIteration(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_operations_dictionary_iteration.py")

    def test_required_syntax(self):
        self.assertEqual(len(self.find_all(ast.List)), 0, "You should not use "
                "a list for this problem.")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You need to use a for loop.")
        self.assertEqual(len(self.find_all(ast.FunctionDef)), 0, "Nothing in "
                "the problem description said to define a function. So why are"
                " you defining a function?")
        self.assertEqual(len(self.find_function_calls("zip")), 0, "You do not "
                "need the zip function.")
        self.assertEqual(len(fors), 1, "You should only use one for loop.")

        delete = "Do not remove or change the book_prices variable."
        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, delete)
        self.assertEqual(len(assigns), 1, "Do not add any new assignment "
                "statements. Simply loop over the dictionary and print out "
                "each title with it price.")
        self.assertEqual(len(assigns[0].targets), 1, delete)
        self.assertIsInstance(assigns[0].targets[0], ast.Name, delete)
        self.assertEqual(assigns[0].targets[0].id, "book_prices", delete)
        self.assertIsInstance(assigns[0].value, ast.Dict, delete)
        self.assertNotEqual(len(self.find_function_calls("print")), 0, "You "
                "are not printing.")
        self.assertEqual(len(self.find_function_calls("print")), 1, "You "
                "should not print more than once.")

        inside = "You must print inside the loop."
        calls = self.find_all(ast.Call, fors[0])
        self.assertNotEqual(len(calls), 0, inside)
        if (len(calls) == 2 and
                isinstance(calls[1].func, ast.Name) and
                calls[1].func.id == "str"):
            pass
        else:
            self.assertEqual(len(calls), 1, "You should only call the print "
                    "function and do so once.")
        self.assertIsInstance(calls[0].func, ast.Name, inside)
        self.assertEqual(calls[0].func.id, "print", inside)

        output = [['Alice in Wonderland 6.99', 'Chronicles of Narnia 12.59',
            'A Tale of Two Cities 5.7', 'Count of Monte Cristo 10.72'],
            [('Alice in Wonderland', 6.99), ('Chronicles of Narnia', 12.59),
                ('A Tale of Two Cities', 5.7), ('Count of Monte Cristo', 10.72)]]
        correct = "You are not printing the correct result."
        self.exec_solution()
        if len(self.printed_lines) == 4:
            for i in range(len(self.printed_lines)):
                line = self.printed_lines[i]
                self.assertIn(line, (output[0][i], output[1][i]), correct)
        else:
            self.assertEqual(self.printed_lines, ['Alice in Wonderland', 6.99,
                'Chronicles of Narnia', 12.59, 'A Tale of Two Cities', 5.7,
                'Count of Monte Cristo', 10.72], correct)


if __name__ == "__main__":
    unittest.main()

import ast
import unittest

import asttest

class TestNestedDataNestedLists(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_nested_lists.py")

    def test_required_syntax(self):
        remove = "Do not remove or change the hourly donations list variable."
        assigns = self.find_all(ast.Assign)
        self.assertGreaterEqual(len(assigns), 1, remove)
        self.assertEqual("hourly_donations_per_day", assigns[0].targets[0].id,
                remove)
        self.assertIsInstance(assigns[0].value, ast.List, remove)
        lst = to_list(assigns[0].value)
        original = [
            [44, 33, 56, 27, 33, 25],
            [12, 15, 22, 19, 21],
            [36, 34, 32, 37, 28, 11, 35],
            [20, 19, 29],
            [22, 27, 21, 15, 26, 15]
            ]
        self.assertEqual(lst, original, remove)

        self.assertEqual(len(self.find_function_calls("sum")), 0, "You are not"
                " allowed to use the sum() function for this assignment. ")

        nums = [n.n for n in self.find_all(ast.Num)]
        self.assertNotIn(714, nums, "Do not embed the solution in your "
                "program. You should calculate it using a for loop instead.")

        fors = self.find_all(ast.For)
        self.assertNotEqual(len(fors), 0, "You need a for loop.")

        outer_loop = fors[0]
        self.assertNotEqual(len(self.find_all(ast.For, outer_loop)), 0, "You "
                "need a nested for loop too.")
        self.assertEqual(len(self.find_all(ast.Subscript)), 0, "You should not"
                " be using list indexing or dictionary lookups.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything")
        self.assertEqual(len(self.printed_lines), 1, "You have printed out too"
                " many things. Are you printing inside of the for loop when "
                "you should be printing after it?")
        self.assertEqual(self.printed_lines[0], 714, "You are not printing out"
                " the right value.")

if __name__ == "__main__":
    unittest.main()

def to_list(lst):
    l = []
    for elt in lst.elts:
        l.append(get_value(elt))
    return l

def get_value(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.NameConstant):
        return node.value
    elif isinstance(node, ast.List):
        return to_list(node)
    return None

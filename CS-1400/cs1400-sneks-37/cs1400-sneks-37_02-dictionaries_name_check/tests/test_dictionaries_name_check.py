import ast
import sys
import unittest

import asttest

class TestDictionariesNameCheck(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionaries_name_check.py")

    def test_required_syntax(self):
        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "Do not remove the person "
                "variable.")
        self.assertEqual(len(assigns), 1, "Do not assign to any other "
                "variables.")
        self.assertIsInstance(assigns[0].value, ast.Dict, "Do not change the "
            "person dictionary.")
        person = {5: "Apple", "Name": 5, "Apple": "Name"}
        self.assertEqual(to_dict(assigns[0].value), person, "Do not change the"
                " person dictionary.")

        print_call = self.find_function_calls('print')
        self.assertNotEqual(len(print_call), 0, "You are not printing.")
        self.assertNotEqual(len(print_call[0].args), 0, "You are not printing "
                "the result.")

        subscripts = self.find_all(ast.Subscript)
        self.assertNotEqual(len(subscripts), 0, "You will need to use a "
                "dictionary lookup.")
        self.assertEqual(len(subscripts), 1, "You should not use more than one"
                " dictionary lookup.")

        lookup = subscripts[0]
        self.assertEqual(print_call[0].args[0], lookup, "You should be "
                "printing the result of the lookup directly.")
        self.assertIsInstance(lookup.ctx, ast.Load, "You need to be using a "
                "dictionary lookup, not writing to a dictionary key.")
        self.assertIsInstance(lookup.value, ast.Name, "You need to look up the"
                " person variable.")
        self.assertEqual(lookup.value.id, "person", "You need to look up the"
                " person variable.")

        if sys.version_info >= (3, 9):
            self.assertIsInstance(lookup.slice, ast.Constant, "You need to look up a "
                    "single key, not a range. That doesn't make sense for "
                    "dictionaries.")
            self.assertNotIsInstance(lookup.slice.value, ast.Num, "You are "
                    "attempting to use a numeric value to look up the value, "
                    "instead of the key 'Name'.")
            if isinstance(lookup.slice.value, ast.Name) and lookup.slice.value.id.lower() == "name":
                self.fail("It looks like you are trying to use a variable named "
                        "{}, instead of the actual string literal."
                        .format(lookup.slice.value.id))
            self.assertIsInstance(lookup.slice.value, str, "You should use a "
                    "string literal to look up the value.")
            self.assertEqual(lookup.slice.value, "Name", "You are not using the "
                    "right string literal.")
        else:
            self.assertIsInstance(lookup.slice, ast.Index, "You need to look up a "
                    "single key, not a range. That doesn't make sense for "
                    "dictionaries.")
            self.assertNotIsInstance(lookup.slice.value, ast.Num, "You are "
                    "attempting to use a numeric value to look up the value, "
                    "instead of the key 'Name'.")
            if isinstance(lookup.slice.value, ast.Name) and lookup.slice.value.id.lower() == "name":
                self.fail("It looks like you are trying to use a variable named "
                        "{}, instead of the actual string literal."
                        .format(lookup.slice.value.id))
            self.assertIsInstance(lookup.slice.value, ast.Str, "You should use a "
                    "string literal to look up the value.")
            self.assertEqual(lookup.slice.value.s, "Name", "You are not using the "
                    "right string literal.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not "
                "printing.")
        self.assertEqual(self.printed_lines[0], 5, "You are not printing the "
                "right result")

def to_dict(dict_node):
    d = {}
    keys = dict_node.keys
    vals = dict_node.values
    for i in range(len(keys)):
        key = get_value(keys[i])
        val = get_value(vals[i])
        d[key] = val
    return d

def get_value(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.NameConstant):
        return node.value
    return None

if __name__ == "__main__":
    unittest.main()

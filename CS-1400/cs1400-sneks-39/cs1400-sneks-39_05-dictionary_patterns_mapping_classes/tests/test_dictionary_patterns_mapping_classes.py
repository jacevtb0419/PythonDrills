import ast
import sys
import unittest

import asttest

class TestDictionaryPatternsMappingClasses(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_patterns_mapping_classes.py")

    def test_required_syntax(self):
        dicts = self.find_all(ast.Dict)
        self.assertNotEqual(len(dicts), 0, "You have not created any "
                "dictionaries.")
        self.assertEqual(len(dicts), 1, "You only need one dictionary.")

        assigns = self.find_all(ast.Assign)
        self.assertNotEqual(len(assigns), 0, "You did not assign your "
                "dictionary to a variable.")
        self.assertEqual(len(assigns), 1, "You only need one assignment "
                "statement.")
        self.assertEqual(assigns[0].value, dicts[0], "You did not assign your "
                "dictionary to the variable.")

        submission = to_dict(dicts[0])
        self.assertIn('CS1400', submission, "You have not created a key to "
                "represent this course!")
        self.assertTrue(all(isinstance(v,  float) for v in submission.values()),
            "Some of your values are not floats.")
        self.assertLess(sum(submission.values()), 1.01, "Your values add up to"
                " more than 1.")
        self.assertGreater(sum(submission.values()), .99, "Your values add up "
                "to less than 1.")

        lookup = "You need to demonstrate how to use a key on your dictionary variable!"
        lookups = self.find_all(ast.Subscript)
        self.assertNotEqual(len(lookups), 0, lookup)
        if sys.version_info >= (3, 9):
            self.assertTrue(any(l.slice.value == "CS1400"
                for l in lookups if isinstance(l.slice, ast.Constant) and
                isinstance(l.slice.value, str)), lookup)
        else:
            self.assertTrue(any(l.slice.value.s == "CS1400"
                for l in lookups if isinstance(l.slice, ast.Index) and isinstance(l.slice.value, ast.Str)), lookup)


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

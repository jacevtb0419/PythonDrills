import ast
import unittest

import asttest

class TestDictionaryPatternsDefinitions(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_patterns_definitions.py")

    def test_required_syntax(self):
        goal = {
            "Doe": "A female deer.",
            "Ray": "A drop of golden sun.",
            "Me": "A name I call myself.",
            "Far": "A long way to run.",
            "Sew": "A needle pulling thread.",
            }

        dicts = self.find_all(ast.Dict)
        self.assertNotEqual(len(dicts), 0, "You have not created any "
                "dictionaries.")
        self.assertEqual(len(dicts), 1, "You only need one dictionary ")

        submission = to_dict(dicts[0])
        if tuple(sorted(submission.keys())) != tuple(sorted(goal.keys())):
            self.fail("Your dictionary's keys does not match the table's keys "
                    "exactly.")
        elif tuple(sorted(submission.keys())) != tuple(sorted(goal.keys())):
            self.fail("Your dictionary's values does not match the table's "
                    "values exactly.")
        self.assertEqual(submission, goal, "Your dictionary does not match the"
                " table exactly.")
        self.assertNotEqual(len(self.find_all(ast.Subscript)), 0, "You need to"
                " demonstrate how to lookup a value by key in your dictionary!")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You are not printing "
                "anything.")
        self.assertIn(self.printed_lines[0], goal.values(), "You are not "
                "printing one of the designated values.")

def get_value(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Str):
        return node.s
    elif isinstance(node, ast.NameConstant):
        return node.value
    return None

def to_dict(dict_node):
    d = {}
    keys = dict_node.keys
    vals = dict_node.values
    for i in range(len(keys)):
        key = get_value(keys[i])
        val = get_value(vals[i])
        d[key] = val
    return d

if __name__ == "__main__":
    unittest.main()

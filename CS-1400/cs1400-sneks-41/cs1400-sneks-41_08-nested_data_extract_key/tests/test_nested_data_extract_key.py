import ast
import unittest
import unittest.mock

import asttest

class TestNestedDataExtractKey(asttest.ASTTest):

    def setUp(self):
        super().setUp("nested_data_extract_key.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        animals = [
            {"Name": "Klaus", "Weight": 27, "Height": 18},
            {"Name": "Pumpkin", "Weight": 20, "Height": 16},
            {"Name": "Wrex", "Weight": 3, "Height": 2},
        ]
        found = False
        assigns = self.find_all(ast.Assign)
        for assign in assigns:
            if (isinstance(assign.targets[0], ast.Name) and
                    assign.targets[0].id == "animals"):
                found = True
                self.assertEqual(to_list(assign.value), animals, "Do not "
                        "change the animals variable.")
        self.assertTrue(found, "Do not remove the animals variable.")

        func = self.match_signature('extract_key', 2)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameters and try again.")

        # TODO: should only find the function calls that are inside of the func
        lists = self.find_all(ast.List, func) + self.find_function_calls("list")
        self.assertNotEqual(len(lists), 0, "What should the type of the value "
                "be that is returned by this function? You will need a literal"
                " value of this type to initialize the accumulated values.")

        fors = self.find_all(ast.For, func)
        self.assertNotEqual(len(self.find_method_calls("append")), 0, "How "
                "do you add more elements to a list?")

        self.assertNotEqual(len(self.find_all(ast.Subscript, func)), 0, "You "
                "will need to do a dictionary look up.")

        names = [n.id for n in self.find_all(ast.Name, func)]
        self.assertNotIn("animals", names, "Do not use the animals variable in"
                " your function. It is not a good name for the parameter since"
                " we want to generalize our functions to work on more data "
                "than just animals.")

        tests = [(([], 'Name'), []),
                (([{'Name': "Klaus"}, {'Name': "Wrex"}], 'Name'), ["Klaus", "Wrex"]),
                (([{'Age': 1}, {'Age': 2}], 'Age'), [1,2]),
                (([{'Age': 1, "HP": 50}, {'Age': 2, "HP": 60}], 'Age'), [1,2])]
        for test in tests:
            with self.subTest(dictionaries=test[0][0], key=test[0][1]):
                from nested_data_extract_key import extract_key
                result = extract_key(test[0][0], test[0][1])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        self.assertGreaterEqual(len(self.find_function_calls('assert_equal')),
                2, "You should unit test your function at least twice.")
        self.ensure_coverage(['extract_key'], .9)

if __name__ == "__main__":
    unittest.main()

def to_dict(dict_node):
    d = {}
    keys = dict_node.keys
    vals = dict_node.values
    for i in range(len(keys)):
        key = get_value(keys[i])
        val = get_value(vals[i])
        d[key] = val
    return d

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
    elif isinstance(node, ast.Dict):
        return to_dict(node)
    return None

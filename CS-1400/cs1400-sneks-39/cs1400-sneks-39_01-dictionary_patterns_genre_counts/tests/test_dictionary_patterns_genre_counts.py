import ast
import unittest

import asttest

class TestDictionaryPatternsGenreCounts(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_patterns_genre_counts.py")

    def test_required_syntax(self):
        for name in self.find_all(ast.Name):
            self.assertNotEqual(name.id, "Counter", "You are not allowed to "
                    "use a Counter for this problem.")

        goal = {'Horror': 4, 'Sci-Fi': 1, 'Comedy': 3}
        loops = self.find_all(ast.For)
        self.assertNotEqual(len(loops), 0, "You need a for loop!")
        self.assertEqual(len(loops), 1, "You only need one for loop!")
        self.assertNotEqual(len(self.find_all(ast.Subscript, loops[0])), "Make"
                " sure you are subscripting within the loop!")
        for s in self.find_all(ast.Str):
            self.assertNotEqual(s.s, "genre", "Hmm check the key you are using"
                    " to track the count of each genre. What should the keys "
                    "be used for?")

        dicts = self.find_all(ast.Dict)
        self.assertNotEqual(len(dicts), 0, "Do not delete the dictionary.")
        self.assertEqual(len(dicts), 1, "Do not create any extra dictionaries.")

        all_strs = [s for s in self.find_all(ast.Str)]
        lists = [d for d in self.find_all(ast.List)]
        self.assertNotEqual(len(lists), 0, "Do not delete the list literal.")
        self.assertEqual(len(lists), 1, "Do not add any extra list literals.")
        self.assertEqual(len(self.find_all(ast.Str, lists[0])), len(all_strs),
                "You should not have any string literals outside of the list "
                "literal.")

        self.exec_solution()
        self.assertEqual(len(self.printed_lines), 1, "Make sure you are "
                "printing!")
        self.assertNotIn("genre", self.printed_lines[0], "You have created a "
                "dictionary to count elements, but it is not counting genres. "
                "Instead, it only has one key for the literal value 'genre', "
                "as opposed to keys for values like 'Horror' or 'Comedy'.")
        self.assertGreaterEqual(len(self.printed_lines[0]), 3, "You have not "
                "counted all of the genres properly.")
        self.assertEqual(tuple(sorted(self.printed_lines[0].keys())),
                ("Comedy", "Horror", "Sci-Fi"), "You have the wrong keys in "
                "your dictionary.")
        self.assertEqual(self.printed_lines[0], goal, "You have calculated the"
                " counts incorrectly.")

if __name__ == "__main__":
    unittest.main()

import ast
import unittest
import unittest.mock

import asttest

class TestDictionaryOperationsDictionaryMutation(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionary_operations_dictionary_mutation.py")

    @unittest.mock.patch("sys.stdout")
    def test_required_syntax(self, mock_stdout):
        self.assertEqual(len(self.find_all(ast.Pass)), 0, "You should delete "
                "the pass statement when you implement the function.")
        self.assertEqual(len(self.find_all(ast.For)), 0, "You are using a for "
                "loop, but you do not need to do so!")

        func = self.match_signature('make_older', 1)
        self.assertIsNotNone(func, "You did not define the function correctly."
                " Check its name and parameter and try again.")

        tests = [({"Age": 10}, 11),
                ({"Age": 0}, 1),
                ({"Age": 20}, 21)]
        for test in tests:
            with self.subTest(person=test[0]):
                from dictionary_operations_dictionary_mutation import make_older
                result = make_older(test[0])
                self.assertEqual(result, test[1], "Your function is "
                        "not returning the correct result. When given '{}' it "
                        "returned '{}', however, it should have returned '{}'."
                        .format(test[0], result, test[1]))

        from dictionary_operations_dictionary_mutation import make_older
        side_effect = {"Age": 20}
        result = make_older(side_effect)
        self.assertEqual(side_effect.get("Age"), result, "Your make_older "
                "function is supposed to change the value associated with the "
                "consumed dictionaries key. This means your function needs to "
                "mutate the dictionary. It is not enough to calculate the new "
                "value, you need to assign it to the dictionary's \"Age\" "
                "key's value!")

        """
        # TODO
        person1 = {"Name": "Charles Babbage", "Age": 17}
        person2 = {"Name": "Ada Lovelace", "Age": 32}
        if "person1" not in student.data or "person1" not in student.data:
            gently("Please ensure that both variables (<code>person1</code> and
                    <code>person2</code>) are still around!")
        elif isinstance(student.data["person1"], int):
            gently("Did you assign the result of calling
                    <code>make_older</code> to <code>person1</code>? You should
                    not do that - the function modifies the dictionaries value
                    and returns the integer (not the dictionary), so you should
                    not assign it back.")
        elif isinstance(student.data["person2"], int):
            gently("Did you assign the result of calling
                    <code>make_older</code> to <code>person2</code>? You should
                    not do that - the function modifies the dictionaries value
                    and returns the integer (not the dictionary), so you should
                    not assign it back.")
        elif student.data["person1"] == person1:
            gently("It looks like you did not change the value of the
                    <code>person1</code> dictionary.")
        elif student.data["person2"] == person2:
            gently("It looks like you did not change the value of the
                    <code>person2</code> dictionary.")
        else:
            person1["Age"] += 1
            person2["Age"] += 1
            if student.data["person1"] == person1 and student.data["person2"] == person2:
            else:
                gently("You have not changed the value of <code>person1</code> or <code>person2</code> correctly.")
        """

        tests = len(self.find_function_calls("assert_equal"))
        self.assertNotEqual(tests, 2, "You were given two unit tests for the "
                "person1 dictionary, you should write two more for person2 in "
                "the same way.")
        self.assertGreaterEqual(tests, 4, "You did not write enough unit tests.")
        self.ensure_coverage(['make_older'], .9)

if __name__ == "__main__":
    unittest.main()

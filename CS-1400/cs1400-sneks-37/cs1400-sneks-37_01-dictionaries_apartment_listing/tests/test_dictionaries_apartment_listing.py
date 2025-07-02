import ast
import unittest

import asttest

class TestDictionariesApartmentListing(asttest.ASTTest):

    def setUp(self):
        super().setUp("dictionaries_apartment_listing.py")

    def test_required_syntax(self):
        dictionaries = self.find_all(ast.Dict)
        self.assertNotEqual(len(dictionaries), 0, "You have not created any "
                "dictionaries.")
        self.assertEqual(len(dictionaries), 1, "You have created multiple "
                "dictionaries, but you should only create one.")

        self.exec_solution()
        self.assertNotEqual(len(self.printed_lines), 0, "You did not print "
                "anything.")
        self.assertEqual(len(self.printed_lines), 1, "You should only print "
                "one thing.")
        apartment = self.printed_lines[0]
        apartment = {k.lower(): v for k,v in apartment.items()}
        if len(apartment) < 4:
            self.fail("Your dictionary has less than 4 keys.")
        all_good = True
        for good_key, value in [
                ("Number of Bedrooms", 3),
                ("Has Backyard?", True),
                ("Rent per Month", 1247.55),
                ("Address", "1 Address")]:
            if good_key.lower() not in apartment:
                self.fail("One of your keys is not what was expected; I "
                        "recommend using the specific key name {} (same "
                        "spelling and punctuation).".format(repr(good_key)))
                all_good = False
            elif apartment[good_key.lower()] != value:
                self.fail("The value associated with the {} key is "
                        "incorrect.".format(repr(good_key)))
                all_good = False
        self.assertTrue(all_good, "Make sure you are printing!")

if __name__ == "__main__":
    unittest.main()

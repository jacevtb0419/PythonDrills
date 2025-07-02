import ast
import io
import unittest
import unittest.mock

import asttest

# The required outputs for each function. input() prompts are commented out
# because when input() is mocked, the prompt doesn't come through the mocked
# stdout.
OUTPUTS = {
    'print_introduction': "* 1) Introduction ********************************\n"
                           "Welcome to the Goblins Magical Loan System!\n"
                           "Please answer the following questions truthfully,\n"
                           "and we will process your loan request.\n"
                           "Imposters will be fed to the dragons.\n",
    'input_name':         "* 2) Name ****************************************\n"
                           "Please enter your full, legal name.\n"
                           "Magical verification will verify your identity.\n"
                           #"Write your name and press enter: \n"
                           "Welcome, {name}!\n",
    'print_rating':       "* 3) Rating **************************************\n"
                           "Your user rating has been calculated.\n"
                           "Your rating is: {rating}/10 points.\n",
    'input_loan_amount':  "* 4) Loan ****************************************\n"
                           "Loans are made based on your customer rating.\n"
                           "However, you can request a loan of any size.\n"
                           "How many galleons do you want?\n",
                           #"Write your loan amount: ",
    'print_loan_availability':
                          "* 5) Available? **********************************\n"
                           "Your loan request has been evaluated.\n"
                           "Loan available: {available}\n",
    'print_conclusion':   "* 6) Conclusion **********************************\n"
                           "Thanks for using Goblins Magical Loan System!\n"
                           "Best of luck with your new small business.\n"
                           "We hope you'll use Goblins for all your future\n"
                           "banking needs. Remember: Fortius Quo Fidelius!\n"
                           "**************************************************\n"
}

FLATTENED_OUTPUT = (OUTPUTS['print_introduction'] +
                    OUTPUTS['input_name'] +
                    OUTPUTS['print_rating'] +
                    OUTPUTS['input_loan_amount'] +
                    OUTPUTS['print_loan_availability'] +
                    OUTPUTS['print_conclusion'])


class TestFunctionalMagic(asttest.ASTTest):

    def setUp(self):
        super().setUp("functional_magic.py")

    def test_required_syntax(self):
        # assert no nested function defs
        func_defs = self.find_all(ast.FunctionDef)
        for func_def in func_defs:
            nested_func_defs = self.find_all(ast.FunctionDef, func_def)
            nested_names = []
            for nested_func_def in nested_func_defs:
                if nested_func_def.name == func_def.name:
                    continue
                nested_names.append(nested_func_def.name)
                self.assertEqual(len(nested_func_defs), 0, "You have nested at"
                        " least one function definition ({}) within another "
                        "function ({}). All functions should be defined at the"
                        " top level of the program."
                        .format(nested_func_def.name, func_def.name))

        # assert no global keyword
        if self.file.count("global") > 1:
            self.fail("You should not use any global variables for this "
                    "project.")

        # assert no nonlocal keyword
        if "nonlocal" in self.file:
            self.fail("You should not use any nonlocal variables for this "
                    "project.")

        # assert calling calculate_rating once
        count = 0
        calls = self.find_all(ast.Call)
        for call in calls:
            if isinstance(call.func, ast.Attribute) and call.func.attr == "calculate_rating":
                count += 1
        self.assertGreaterEqual(count, 1, "You need to call calculate_rating "
                "one time in the main function in order to properly approve a "
                "loan for your customers.")
        self.assertEqual(count, 1, "You should only call calculate_rating one "
                "time in the main function.")

        # assert calculate_rating not modifed
        with open("operations.py") as f:
            self.assertIn("""def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is delicate, and will break after being called once.

    Notes:
        (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.

    Args:
        name (str): A string representing the user's full name.
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC""", f.read(),
            "You should not change the calculate_rating function! You will "
            "need to reset your progress in codegrinder. Ask your instructor "
            "for help if you get lost.")

        # Assert main is called correctly
        if (("""if __name__ == '__main__':
    main()""" not in self.file)
        and ("""if __name__ == '__main__': main()""" not in self.file)):
            self.fail("You are not calling the main function correctly. "
                    "Copy the cody snippet in the \"Testing Your Program\""
                    "section of the instructions into your program and try again.")


    def test_functions(self):
        # def test_print_introduction(self, buf):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf:
            func = self.match_signature('print_introduction', 0)
            self.assertIsNotNone(func, "Function print_introduction missing.")
            self.assertTrue(self.function_prints(func), "The print_introduction "
                    "function should *print* the introduction.")
            from functional_magic import print_introduction
            result = print_introduction()
            self.assertIsNone(result, "The print_introduction function should not "
                    "return anything.")
            marker = "="*60 + "\n"
            printed = buf.getvalue()
            expected = OUTPUTS["print_introduction"]
            self.assertEqual(printed, expected,
                    "\n\nYour function is not printing the correct "
                    "message. It printed: \n{}{}{}"
                    "It should have printed: \n{}{}{}"
                    .format(marker, printed, marker, marker, expected, marker))

        # def test_input_name(self):
        func = self.match_signature('input_name', 0)
        self.assertIsNotNone(func, "Function input_name missing.")
        self.assertTrue(self.function_prints(func), "The input_name function "
                "should print something. Check the assignment description and "
                "update your function.")

        tests = ["Ada Bart", "Ellie Bart"]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf, \
                    unittest.mock.patch('builtins.input', side_effect=[test]):
                with self.subTest(name=test):
                    from functional_magic import input_name
                    result = input_name()
                    printed = buf.getvalue()
                    expected = OUTPUTS['input_name'].format(name=test)
                    self.assertEqual(printed, expected,
                            "\n\nYour function is not printing the correct "
                            "message. When given '{}' it printed: \n{}{}{}"
                            "It should have printed: \n{}{}{}"
                            .format(test, marker, printed, marker, marker,
                                expected, marker))
                    self.assertEqual(result, test, "\n\nYour function is not"
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test, result, test))

        # def test_print_rating(self):
        func = self.match_signature('print_rating', 1)
        self.assertIsNotNone(func, "Function print_rating missing.")
        self.assertTrue(self.function_prints(func), "The print_rating "
                "function should print something. Check the assignment "
                "description and update your function.")

        tests = [5, 8, 3, 7]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf:
                with self.subTest(rating=test):
                    from functional_magic import print_rating
                    result = print_rating(test)
                    printed = buf.getvalue()
                    expected = OUTPUTS['print_rating'].format(rating=test)
                    self.assertEqual(printed, expected,
                            "\n\nYour function is not printing the correct "
                            "message. When given '{}' it printed: \n{}{}{}"
                            "It should have printed: \n{}{}{}"
                            .format(test, marker, printed, marker, marker,
                                expected, marker))
                    self.assertIsNone(result, "\n\nYour function is not"
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(None, result, None))

        # def test_input_loan_amount(self):
        func = self.match_signature('input_loan_amount', 0)
        self.assertIsNotNone(func, "Function input_loan_amount missing.")
        self.assertTrue(self.function_prints(func), "The input_loan_amount "
                "function should print something. Check the assignment "
                "description and update your function.")

        tests = [1000, 100, 10]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf, \
                    unittest.mock.patch('builtins.input', side_effect=[test]):
                with self.subTest(name=test):
                    from functional_magic import input_loan_amount
                    result = input_loan_amount()
                    printed = buf.getvalue()
                    expected = OUTPUTS['input_loan_amount']
                    self.assertEqual(printed, expected,
                            "\n\nYour function is not printing the correct "
                            "message. It printed: \n{}{}{}"
                            "It should have printed: \n{}{}{}"
                            .format(marker, printed, marker, marker,
                                expected, marker))
                    self.assertIsInstance(result, int, "Your function is not "
                            "returning an integer. Make sure you convert the "
                            "user's desired loan amount to an int.")
                    self.assertEqual(result, test, "\n\nYour function is not"
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(test, result, test))

        # def test_test_loan(self):
        func = self.match_signature('test_loan', 2)
        self.assertIsNotNone(func, "Function test_loan missing.")
        self.assertFalse(self.function_prints(func), "The test_loan "
                "function should not print anything. Check the assignment "
                "description and update your function.")

        tests = [((5, 1000), True), ((5, 3000), False), ((2, 100), True),
                ((5, 200), True), ((2, 1000), False)]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf:
                with self.subTest(rating=test[0][0], loan_amount=test[0][1]):
                    from functional_magic import test_loan
                    result = test_loan(*test[0])
                    printed = buf.getvalue()
                    self.assertEqual(result, test[1], "\n\nYour function is "
                    "not returning the correct result. When given '{}' it "
                    "returned '{}', however, it should have returned "
                    "'{}'.".format(test[0], result, test[1]))

        # def test_print_loan_availability(self):
        """
        for rating, amount, available in test_cases:
            result = student.call('print_loan_availability', rating, amount)
            assertIsNone(result, None)
            assertPrints(result,
                         format_all(OUTPUTS['print_loan_availability'],
                                    rating=rating, amount=amount,
                                    available=available), score=.4)
        """
        func = self.match_signature('print_loan_availability', 2)
        self.assertIsNotNone(func, "Function print_loan_availability missing.")
        self.assertTrue(self.function_prints(func), "The "
                "print_loan_availability function should print something. "
                "Check the assignment description and update your function.")

        tests = [((5, 1000), True), ((5, 3000), False), ((2, 100), True),
                ((5, 200), True), ((2, 1000), False)]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf:
                with self.subTest(rating=test[0][0], loan_amount=test[0][1]):
                    from functional_magic import print_loan_availability
                    result = print_loan_availability(test[0][0], test[0][1])
                    printed = buf.getvalue()
                    expected = OUTPUTS['print_loan_availability'].format(available=test[1])
                    self.assertEqual(printed, expected,
                            "\n\nYour function is not printing the correct "
                            "message. When given '{}' it printed: \n{}{}{}"
                            "It should have printed: \n{}{}{}"
                            .format(test[0], marker, printed, marker, marker,
                                expected, marker))
                    self.assertIsNone(result, "\n\nYour function is not"
                            "returning the correct result. When given '{}' it "
                            "returned '{}', however, it should have returned "
                            "'{}'.".format(None, result, None))

        # def test_print_conclusion(self, buf):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf:
            func = self.match_signature('print_conclusion', 0)
            self.assertIsNotNone(func, "Function print_conclusion missing.")
            self.assertTrue(self.function_prints(func), "The print_conclusion "
                    "function should *print* the introduction.")
            from functional_magic import print_conclusion
            result = print_conclusion()
            self.assertIsNone(result, "The print_conclusion function should not "
                    "return anything.")
            marker = "="*60 + "\n"
            printed = buf.getvalue()
            expected = OUTPUTS["print_conclusion"]
            self.assertEqual(printed, expected,
                    "\n\nYour function is not printing the correct "
                    "message. It printed: \n{}{}{}"
                    "It should have printed: \n{}{}{}"
                    .format(marker, printed, marker, marker, expected, marker))

        # def test_main(self):
        """
        for name, rating, amount, available in test_cases:
            student.data['calculate_rating'].o=True
        """

        tests = [
            (("Ada Bart", 1000), (2, False))]
            # TODO: getting weird error 'cannot call this twice' for the rest
            # of the tests. Except it isn't an error but assigned to the value
            # of the rating variable in the print_loan_availability function.
            #(("Ada Bart", 100), (2, True))],
            #(("Harry Potter", 1000), (6, True)),
            #(("Harry Potter", 5000), (6, False)),
        #]
        marker = "="*60 + "\n"
        for test in tests:
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as buf, \
                    unittest.mock.patch('builtins.input', side_effect=test[0]):
                with self.subTest(name=test[0][0], loan_amount=test[0][1]):
                    from functional_magic import main
                    result = main()
                    printed = buf.getvalue()
                    expected = FLATTENED_OUTPUT.format(
                            name=test[0][0],
                            amount=test[0][1],
                            rating=test[1][0],
                            available=test[1][1])
                    self.assertEqual(printed, expected,
                            "\n\nYour program is not printing the correct "
                            "messages. It printed: \n{}{}{}"
                            "It should have printed: \n{}{}{}"
                            .format(marker, printed, marker, marker, expected, marker))
                    self.assertIsNone(result, "\n\nYour main function is not "
                            "returning the correct result. It returned '{}', "
                            "however, it should have returned '{}'."
                            .format(result, None))

if __name__ == "__main__":
    unittest.main()

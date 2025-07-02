import operations

def print_introduction():
    print("""* 1) Introduction ********************************
Welcome to the Goblins Magical Loan System!
Please answer the following questions truthfully,
and we will process your loan request.
Imposters will be fed to the dragons.""")

def input_name():
    print("""* 2) Name ****************************************
Please enter your full, legal name.
Magical verification will verify your identity.""")
    name = input("Write your name and press enter: ")
    print("Welcome, " + name + "!")
    return name

def print_rating(rating):
    string_rating = str(rating)
    print("""* 3) Rating **************************************
Your user rating has been calculated.
Your rating is: """ + string_rating + "/10 points.")


def input_loan_amount():
    print("""* 4) Loan ****************************************
Loans are made based on your customer rating.
However, you can request a loan of any size.
How many galleons do you want?""")
    loan_amount = int(input("Write your loan amount: "))
    return loan_amount

def test_loan(rating, loan_amount):
    return (rating ** 2) * 100 >= loan_amount

def print_loan_availability(rating, loan_amount):
    available = test_loan(rating, loan_amount)
    print("""* 5) Available? **********************************
Your loan request has been evaluated.
Loan available: """ + str(available))

def print_conclusion():
    print("""* 6) Conclusion **********************************
Thanks for using Goblins Magical Loan System!
Best of luck with your new small business.
We hope you'll use Goblins for all your future
banking needs. Remember: Fortius Quo Fidelius!
**************************************************""")
    
def main():
   print_introduction()
   name = input_name()
   rating = operations.calculate_rating(name)
   print_rating(rating)

   loan_amount = input_loan_amount()

   print_loan_availability(rating, loan_amount)

   test_loan(rating, loan_amount)
   
   print_conclusion()

if __name__ == '__main__':
    main()
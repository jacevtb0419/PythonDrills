## Character Input
def basic_input():
    name = input("Enter your name: ") 
    age = input("Enter your age: ")
    print("You are ", name, "and you are ", age, "years old.")

## Odd Or Even
def odd_or_even():
    number = int(input("Please enter a number: "))
    mod = number % 2
    if mod > 0:
        print("This number is odd!")
    elif mod == 0:
        print("0 is neither odd or even")
    else:
        print("This number is even")

## List Values Less/More than X
def list_less_than_ten():
    ## done in one line
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [ x for x in a if x < 22]
    print(b)

    ## drawn out way 
    c = [1, 1, 2, 3, 5, 8 , 13, 21, 34, 55, 89]
    d = []
    for x in c:
        if x > 5:
            d.append(x)
    print(d)

## Divisors of a number
def divisors():
    num = int(input("Please choose a number: "))
    divisor_list = []
    list_range = list(range(1, num+1))
    for x in list_range:
        if num % x == 0:
            divisor_list.append(x)
    print(divisor_list)

## List Overlap
def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for x in a:
        if x in b:
            c.append(x)
    print(c)

def string_lists():
    user_word = input("Type a word: ")
    reverse_word = user_word[::-1]
    print(reverse_word)
    if user_word == reverse_word:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome.")

def list_comprehensions():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [x for x in a if x % 2 == 0]
    print(b)

def main():
    list_comprehensions()
    
main()

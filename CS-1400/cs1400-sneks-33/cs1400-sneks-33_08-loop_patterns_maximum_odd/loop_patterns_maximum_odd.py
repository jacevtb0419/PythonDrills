from cisc108 import assert_equal

def is_odd(a_number):
    '''
    Consumes a number and determines if it is odd.

    Args:
        a_number (int or float): Any valid number
    Returns:
        bool: Whether or not the number was odd
    '''
    return a_number % 2 == 1
def maximum_odd(numbers):
    maximum = numbers[0]
    for val in numbers:
        if is_odd(val) == True and val > maximum:
            maximum = val
    return maximum

assert_equal(is_odd(1), True)
assert_equal(is_odd(2), False)
assert_equal(maximum_odd([1,7,8]), 7)
assert_equal(maximum_odd([2, 8, 10]), None)   

        


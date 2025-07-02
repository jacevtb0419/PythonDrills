from cisc108 import assert_equal
def average(numbers):
    sum = 0 
    count = 0
    for number in numbers:
        sum = sum + number
        count = count + 1
    average = sum / count
    return average

assert_equal(average([12, 24, 36]), 24.0)
assert_equal(average([6, 9, 112]), 42.333333333333336)
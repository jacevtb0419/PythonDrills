from cisc108 import assert_equal
def minimum(numbers):
    minimum = numbers[0]
    for val in numbers:
        if val < minimum:
            minimum = val
    return minimum
assert_equal(minimum([20, 13, 42, 7]), 7)
assert_equal(minimum([1, 2, 3]), 1)

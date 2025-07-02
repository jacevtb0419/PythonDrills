from cisc108 import assert_equal
def cube_elements(numbers):
    new_list = []
    for number in numbers:
        new_list.append(number ** 3)
    return new_list
assert_equal(cube_elements([2, 3, 9]), [8, 27, 729]) 
assert_equal(cube_elements([1, 2]), [1, 8])
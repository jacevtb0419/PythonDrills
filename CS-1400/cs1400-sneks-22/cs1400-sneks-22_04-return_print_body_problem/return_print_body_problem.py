from cisc108 import assert_equal

def calculate_area(height, width):
    return height*width

assert_equal(calculate_area(10, 20), 200)
assert_equal(calculate_area(20, 30), 600)
assert_equal(calculate_area(15, 20), 300)

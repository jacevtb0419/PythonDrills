from cisc108 import assert_equal
def filter_high(vals):
    new_list = []
    for numbers in vals:
        if numbers <= 50:
            new_list.append(numbers)
    return new_list

assert_equal(filter_high([12, 60, 72]), [12])
assert_equal(filter_high([22, 33, 44]), [22, 33, 44])
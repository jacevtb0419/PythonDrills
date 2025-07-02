from cisc108 import assert_equal
def sum_high(vals):
    sum = 0 
    for value in vals:
        if value > 50:
            sum = sum + value
    return sum 


assert_equal(sum_high([5, 50, 51, 62]), 113)
assert_equal(sum_high([0, 1, 2]), 0)
     
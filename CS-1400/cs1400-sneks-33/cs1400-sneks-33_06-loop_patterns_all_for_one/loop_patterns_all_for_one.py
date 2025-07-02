from cisc108 import assert_equal
def all_true(vals):
    truthiness = True
    for values in vals:
        truthiness = truthiness and values
    return truthiness

assert_equal(all_true([True, True, True]), True)
assert_equal(all_true([False, True]), False)
    

from cisc108 import assert_equal

def add_positives(a, b):
    if a > 0 and b > 0: 
        return a + b
    else:
        return 0
    


    
assert_equal(add_positives(1, 2), 3)
assert_equal(add_positives(-1, 2), 0)
assert_equal(add_positives(2, 0), 2)
assert_equal(add_positives(-2, -1), 0)
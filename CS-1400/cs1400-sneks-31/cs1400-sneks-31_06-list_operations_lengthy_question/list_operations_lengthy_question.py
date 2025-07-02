from cisc108 import assert_equal
def check_length(list1):
    if len(list1) >= 3 and len(list1) <= 5:
        return True
    else:
        return False 

assert_equal(check_length([1, 2 ,3]), True)
assert_equal(check_length([1, 2]), False)
assert_equal(check_length([1, 2, 3, 4, 5]), False)
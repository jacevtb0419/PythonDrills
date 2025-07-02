from cisc108 import assert_equal
def is_weekend(list):
    if "Saturday" in list or "Sunday" in list: 
        return True
    else: 
        return False
    
assert_equal(is_weekend(["Monday", "Tuesday"]), False)
assert_equal(is_weekend(["Saturday", "Friday", "Thursday"]), True)

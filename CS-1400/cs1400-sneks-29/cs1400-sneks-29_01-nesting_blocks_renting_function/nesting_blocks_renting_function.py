from cisc108 import assert_equal
def can_rent(age, has_license):
    if age >= 21: 
        if age < 1000:
            if has_license:
                return "Can rent a car"
            else:
                return "Doesn't have a license"
        else:
            return "Too old"
    else:
        return "Too young" 
    

assert_equal(can_rent(22, True), "Can rent a car")
assert_equal(can_rent(16, False), "Too young")
assert_equal(can_rent(1001, True), "Too old") 
assert_equal(can_rent(23, False), "Doesn't have a license" )
from cisc108 import assert_equal
def am_i_on_fire(temperature):
    return temperature >= 109

assert_equal(am_i_on_fire(100), False)
assert_equal(am_i_on_fire(110), True)

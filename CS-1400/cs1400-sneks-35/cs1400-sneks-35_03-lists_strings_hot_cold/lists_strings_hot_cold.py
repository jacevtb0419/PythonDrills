from cisc108 import assert_equal
def add_hot_cold(temps):
    count = 0
    for val in temps:
        if "C" in val:
            count = count - 1
        elif "H" in val:
            count = count + 1
    return count

assert_equal(add_hot_cold("HHHCC"), 1)
assert_equal(add_hot_cold("HHHH"), 4)

from cisc108 import assert_equal
def make_list(item1, item2, item3):
    return [item1, item2, item3]

assert_equal(make_list(1, 2, 3), [1, 2, 3])
assert_equal(make_list("frogs", "toads", "butterflies"), ["frogs", "toads", "butterflies"])
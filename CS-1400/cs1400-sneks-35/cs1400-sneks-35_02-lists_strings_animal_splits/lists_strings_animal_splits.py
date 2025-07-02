from cisc108 import assert_equal
def all_cats(animals):
    if animals == "":
        return False
    
    for animal in animals.split(","):
        if "cat" not in animal:
            return False
    return True

assert_equal(all_cats("cat,dog,whale"), False)
assert_equal(all_cats(""), False)
assert_equal(all_cats("cat, cat"), True)
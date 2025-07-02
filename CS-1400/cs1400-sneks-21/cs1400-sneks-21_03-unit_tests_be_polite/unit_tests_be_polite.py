from cisc108 import assert_equal
def make_polite(message):
    return message + ", please" 

assert_equal(make_polite("Pet the dog"), "Pet the dog, please")
assert_equal(make_polite("Walk the dog"), "Walk the dog, please")
from cisc108 import assert_equal
from string import ascii_letters
def starts_with_letter(word):
    return word[0] in ascii_letters

assert_equal(starts_with_letter("ABC123"), True)
assert_equal(starts_with_letter("!sw"), False)

        
    
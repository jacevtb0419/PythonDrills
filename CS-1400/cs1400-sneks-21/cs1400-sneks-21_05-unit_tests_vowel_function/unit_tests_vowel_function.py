from cisc108 import assert_equal
def begins_with_vowel(string):
    return string[0] in "AEIOUaeiou"

assert_equal(begins_with_vowel("Elephant"), True)
assert_equal(begins_with_vowel("Knight"), False)
assert_equal(begins_with_vowel("a vowel"), True)
assert_equal(begins_with_vowel(" "), False)


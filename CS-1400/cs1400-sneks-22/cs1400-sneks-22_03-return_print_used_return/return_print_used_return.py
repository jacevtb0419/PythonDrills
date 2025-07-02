from cisc108 import assert_equal

# define your function here
def pluralize(string):
    return string +"s"

assert_equal(pluralize("cat"), "cats")

noun = pluralize("Dog") 

print(noun + " can pet other " + noun)

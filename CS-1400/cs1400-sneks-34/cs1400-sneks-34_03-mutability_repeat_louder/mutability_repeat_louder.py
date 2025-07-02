from cisc108 import assert_equal


def make_exclamations(messages):
    exclamations = []
    for message in messages:
        exclamations.append(message + "!")
    return exclamations

assert_equal(make_exclamations(["Hi", "I'm Ada"]), ["Hi!", "I'm Ada!"])
assert_equal(make_exclamations(["Woah", "Count these"]), ["Woah!", "Count these!"])

print(make_exclamations(["Christer"]))

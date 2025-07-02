from cisc108 import assert_equal

person1 = {"Name": "Charles Babbage", "Age": 17}
person2 = {"Name": "Ada Lovelace", "Age": 32}

def make_older(person):
    if "Age" not in person:
        person["Age"] = 0
    person["Age"] = 1 + person["Age"] 
    return person["Age"]

assert_equal(make_older(person1), 18)
assert_equal(make_older({"Name": "Charles Babbage", "Age": 18}), 19)
assert_equal(make_older(person2), 33)
assert_equal(make_older({"Name": "Ada Lovelace", "Age": 32}), 33)
assert_equal(make_older({}), 0)
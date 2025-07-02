from cisc108 import assert_equal
def extract_key(categories, key):
    new_list = []
    for category in categories: 
        new_list.append(category[key]) 
    return new_list

animals = [
    {"Name": "Klaus", "Weight": 27, "Height": 18},
    {"Name": "Pumpkin", "Weight": 20, "Height": 16},
    {"Name": "Wrex", "Weight": 3, "Height": 2},
]

assert_equal(extract_key(animals, "Height"), [18, 16, 2]) 
assert_equal(extract_key(animals, "Name"), ["Klaus", "Pumpkin", "Wrex"])

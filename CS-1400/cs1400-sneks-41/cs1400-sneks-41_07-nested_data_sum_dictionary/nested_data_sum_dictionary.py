from cisc108 import assert_equal






def sum_dictionary(a_dictionary):
    new = {}
    for key, values in a_dictionary.items():
        new[key] = 0
        for value in values:
            new[key] = new[key] + value
    return new

assert_equal(sum_dictionary({
    "Module 1": [10, 5, 3, 5],
    "Module 2": [7, 3, 4, 5, 3],
    "Module 3": [10, 12, 4, 3, 2]
}), {"Module 1": 23, "Module 2": 22, "Module 3": 31})

from cisc108 import assert_equal
def get_name(dictionary):
    return dictionary["Name"]

assert_equal(get_name({"Name": "Chris", "Pay": 1000}), "Chris")
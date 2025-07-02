from cisc108 import assert_equal
def get_default_name(dictionary):
    if "Dog's Name" not in dictionary:
        return "No dog"
    return dictionary["Dog's Name"]

assert_equal(get_default_name({"Dog's Name": "Barker", "Sex": "Male"}), "Barker")
assert_equal(get_default_name({}), "No dog")
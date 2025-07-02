from cisc108 import assert_equal
def convert_operator(string):
    for character in string:
        if character == "+":
            return 1
        elif character == "-":
            return -1
        else:
            return 0
assert_equal(convert_operator("1+2"), 1)
assert_equal(convert_operator("-"), -1)
assert_equal(convert_operator(" "), 0)
        
file_path = "plus_and_minus.txt"
file = open(file_path)
file = file.read()
total = 0

for char in file:
    total = total + convert_operator(char)
print(total)
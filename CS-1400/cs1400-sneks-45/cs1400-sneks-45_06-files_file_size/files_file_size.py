from cisc108 import assert_equal
def calculate_file_size(file_name):
    file = open(file_name)
    count = 0 
    for line in file:
        for char in line:
            count = count + 1
    file.close()
    return count
     
assert_equal(calculate_file_size("rainfall.txt"), 28830)
assert_equal(calculate_file_size("names.txt"), 119)
assert_equal(calculate_file_size("empty.txt"), 0)
from cisc108 import assert_equal
def bookend_list(list): 
    
    if list:
        new_list = [list[0], list[-1]]
        return new_list
    else:
        return []
    
assert_equal(bookend_list(["Fire", "Water", "Earth"]), ["Fire", "Earth"])
assert_equal(bookend_list([]), [])
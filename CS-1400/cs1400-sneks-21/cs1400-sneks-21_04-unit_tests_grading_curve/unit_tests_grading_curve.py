from cisc108 import assert_equal
def curve_grade(grade):
    return grade ** .5 * 10

assert_equal(curve_grade(90), 94.86832980505139)
assert_equal(curve_grade(100), 100.0)
assert_equal(curve_grade(50), 70.7106781187)
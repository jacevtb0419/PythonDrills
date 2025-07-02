from cisc108 import assert_equal
def calculate_income(salary):
    tax = .1
    if salary > 5000:
        return salary - (salary * tax)
    else:
        return salary
assert_equal(calculate_income(1000), 1000)
assert_equal(calculate_income(10000), 9000.0)

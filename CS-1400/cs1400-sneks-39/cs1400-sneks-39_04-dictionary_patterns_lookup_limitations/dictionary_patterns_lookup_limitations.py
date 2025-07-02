from cisc108 import assert_equal
def lookup_temperature(temperature):
    if temperature < 32:
        return "Freezing"
    elif temperature >= 32 and temperature < 50: 
        return "Cold"
    elif temperature >= 50 and temperature < 70:
        return "Warm"
    elif temperature >= 50:
        return "Hot" 


print(lookup_temperature(25))

assert_equal(lookup_temperature(-2), "Freezing")
assert_equal(lookup_temperature(41), "Cold")
assert_equal(lookup_temperature(69), "Warm")
assert_equal(lookup_temperature(100), "Hot")
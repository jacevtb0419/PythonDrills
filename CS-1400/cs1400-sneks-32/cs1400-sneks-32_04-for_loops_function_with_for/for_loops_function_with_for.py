# write your function here
def print_fahrenheit(temperatures):
    for Celsius in temperatures:
        Fahrenheit = Celsius * 9 / 5 + 32
        print(Fahrenheit)


# this is an example of how to call your function
print_fahrenheit([20, 30, 40])

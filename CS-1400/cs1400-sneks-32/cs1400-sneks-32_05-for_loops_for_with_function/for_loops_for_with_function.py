def convert_fahrenheit(Celsius):
    Fahrenheit = Celsius * 9 / 5 + 32
    return Fahrenheit

temperatures = [10, 20, 30]
for temperature in temperatures:
    print(convert_fahrenheit(temperature))
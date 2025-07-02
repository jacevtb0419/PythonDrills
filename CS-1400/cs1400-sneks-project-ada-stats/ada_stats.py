"""
Ada's Stats Module

A collection of functions for doing some basic statistics on your data.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canvas for more information.
"""

# 0) Question and Results
QUESTION = "How many video games do you own on your favorite gaming platform"
ANSWERS = [0, 0, 0, 0, 0, 0, 0, 1, 4, 6, 3, 40, 4, 300, 36, 12]

# 1) count
def count(numbers):
    vals = 0
    for val in numbers:
        vals = vals + 1
    return vals
 

# 2) summate
def summate(numbers):
    sum = 0
    for val in numbers:
        sum = sum + val
    return sum


# 3) mean
def mean(numbers):
    if numbers == []:
        return None
    average = summate(numbers) / count(numbers)
    return round(average, 2)

# 4) square
def square(numbers):
    new_list = []
    for val in numbers: 
        new_list.append(val ** 2)
    return new_list

# 5) standard_deviation
def standard_deviation(numbers):
    length = count(numbers)
    if length < 2:
        return None
    total = summate(numbers)
    total_squared = total ** 2
    divided_by_count = total_squared / length
    squared = square(numbers)
    sum_squared = summate(squared)
    diff = sum_squared - divided_by_count
    result = diff / (length- 1)
    stdev = result ** .5
    return stdev 
# 6) main function
# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
def main(question, results):
    print("We asked", count(results), "people the following question.")
    print(' "'+question+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(results))
    print("\tMean:", mean(results))
    print("\tStandard Deviation:", standard_deviation(results))


if __name__ == "__main__":
    main(QUESTION, ANSWERS)

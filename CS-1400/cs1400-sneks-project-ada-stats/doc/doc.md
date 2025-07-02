# Project 4) Ada Stats

Last week, you collected some data out in the field. This week, you'll analyze
that data by calling some basic statistical functions. Normally, this would be
trivial, since Python has several built-in functions to do Summations, Averages,
and Standard Deviations. However, for this assignment CodeGrinder has been
configured to disable these built-in statistic functions. That means you will
have to create your own.

Your learning goals are as follows:

- Write functions that consume and/or produce lists
- Write functions that incorporate if statements to guard against bad arguments
- Practice responding to unit tests
- Translate mathematical formula into code

### Program Structure

Some code is already given to you. You will benefit from reading through the
entire file before writing any code.

For this project, you will need to implement a total of five functions and
define three variables. **When defining these functions, you cannot use any
built-in list handling functions (e.g., len, sum) or external modules (e.g.,
statistics, numpy).**

Here is an explanation of each function:

1. `count()`: Consumes a list of numbers and returns an integer representing the
   length of that list.
2. `summate()`: Consumes a list of numbers and returns an integer representing
   the total sum of all the numbers in the list (i.e., adds up all of the
   numbers in the list).
3. `mean()`: Consumes a list of numbers and returns a float value representing
   the mean of the list. The formula for the mean of a list is
   <br>`mean = sum / count`<br>
   **Think strategically about how you can use functions you have already
   written to simplify this function's definition.** If the list is empty, then
   return the special value `None` (but do this before attempting to calculate
   the mean). You should use the `round()` function to round the result to two
   decimal places.
4. `square()`: Consumes a list of numbers and returns a new list of numbers
   where each element from the original list has been squared.
5. `standard_deviation()`: Consumes a list of numbers and returns a float
   representing their standard deviation. If the list has fewer than 2 elements,
   you should return the special value `None`. The standard deviation formula
   you should use is described [here](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Na%C3%AFve_algorithm").
   However, you may simply implement it according to the following steps:
    1. Count how many numbers there are and save the result to a variable (e.g., `length`)
    2. If the length is less than 2, return `None`
    3. Sum all of the numbers and save the result to a variable (e.g., `total`)
    4. Square the total of all of the numbers and save the result to a variable (e.g., `total_squared`)
    5. Divide the square of the total by the count of numbers and save the result to a variable (e.g., `divided_by_count`)
    6. Square each number and save the result to a variable (e.g., `squared`)
    7. Sum all of the squared numbers and save the result to a variable (e.g., `sum_squared`)
    8. Subtract divided_by_count from the sum of the squared numbers and save the result to a variable (e.g., `diff`)
    9. Divide the diff by the (count - 1) and save the result to a variable (e.g., `result`)
    10. Return the square root of this result (hint: what exponent represents the square root?) Take advantage of the functions you have already written to simplify this function's definition. For reference, here is the entire formula described in the steps above but in one line (although I recommend not implementing it this way):<br>```stdev = (((sum of the values squared) - ((sum of the values) * (sum of the values))/(count of the values))/(count of the values - 1)) ** .5```
6. `main()`: This function is given to you. For it to work properly, copy over
   your `QUESTION` and `ANSWER` variables from last week's Field Work assignment
   into the proper assignment statements toward the top of the file. These
   variables are used to call the `main()` function at the bottom of the file.

### Evaluating Your Solution

You are graded based on passing the unit tests in CodeGrinder. Only the unit
tests can determine if you earn points. You should evaluate your code early and
often as you develop. The inability to follow instructions and use CodeGrinder
is not an excuse. **You must match the expected results exactly.**

There are no limits to how many times you can submit your code. However, we
keep the grade of the most recent submission.

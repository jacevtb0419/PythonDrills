# 22.3) Used Return

Write a function named `pluralize` that consumes a string and returns that
string with an `"s"` at the end (so `"dog"` would become `"dogs"`).

Now, let's call that function and use its result for something useful.
Remember that calling a function evaluates/executes that function as an
expression. Also, remember that the result of calling a function is defined by
its return value.

Call your `pluralize` function and pass in the string `"Dog"` as the argument.
Assign the result of calling the function to a variable called `noun` (notice
the use of the `noun` variable in the `print` function call).

At this point, if you run your program it should print `"Dogs can pet other Dogs"`.

Finally, write a unit test at the bottom of your program to make sure your
function works on strings other than `"Dog"`.

Notice that because this function _returned_ a value, that value could be reused
multiple times.

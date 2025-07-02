# 42.3) Choose


Define a function named `choose` that consumes a non-empty list of strings
representing options of a menu. First, print the string `"You can:"`. Then,
print out each option on a separate line. Finally, use a `while` loop to
repeatedly take in user input until the user types one of the commands, and then
return that chosen command. Use the string `"What will you do?"` as the input's
prompt.

You do not need to unit test this function.

If `choose(['quit', 'nap', 'fight'])` is executed, and the user types in
`sleep`, `escape`, and then `fight`, then the string value `'fight'` will be
returned and the following will have been printed:


    You can:

    - quit
    - nap
    - fight

    What will you do?

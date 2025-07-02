# 39.4) Lookup Limitations

Convert the table below into a function named `lookup_temperature` that converts
temperatures to strings. Do not use the Lookup Pattern - in fact, do not use a
dictionary at all. This problem is meant to illustrate the limitations of the
Lookup Pattern. Make sure to call this function to test it out.

Condition               |   Status
----------------------------------------
Temperature < 32        |   Freezing
32 <= Temperature < 50  |   Cold
50 <= Temperature < 70  |   Warm
70 <= Temperature       |   Hot

"""
Topic: While Loops
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Print numbers 1-10 using a while loop, then modify it to skip
even numbers.

"""

# -----------------------------------
# My Solution
# -----------------------------------

i = 1

while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

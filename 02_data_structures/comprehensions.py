"""
Topic: List Comprehensions
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Practice: Turn a normal for-loop that
squares numbers 1-10 into a one-line list comprehension.

"""

# -----------------------------------
# My Solution
# -----------------------------------

a = [1,2,3,4,5,6,7,8,9,10]

squared = [x**2 for x in a]
print(squared)

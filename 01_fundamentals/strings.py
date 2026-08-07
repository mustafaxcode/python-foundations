"""
Topic: Strings
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Take a sentence, use slicing to grab the first word, convert it to
uppercase, and count how many times a specific letter appears.

"""

# -----------------------------------
# My Solution
# -----------------------------------

x = "Hello I am Mustafa"
first = x[0:5]
print(first)

upper_case = first.upper()
print(upper_case)

print(upper_case.count('L'))

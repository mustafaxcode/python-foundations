"""
Topic: If...Else / Conditionals
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Write a simple grade calculator (A/B/C/F based on score).

"""

# -----------------------------------
# My Solution
# -----------------------------------

number = int(input("Enter your number:"))

if number>=85 and number<=100:
    print("A")
elif number>70 and number<=80:
    print("B")
elif number>=50 and number<=70:
    print("C")
else:
    print("F")

"""
Topic: For Loops
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Loop through a dictionary and print each key-
value pair cleanly.

"""

# -----------------------------------
# My Solution
# -----------------------------------

student = {
    "name" : "Muhammad Mustafa",
    "grades" : ["A","A-","A-","A"],
    "address" : {
        "city" : "Lahore",
        "block" :  "A",
    }
}

for x,y in student.items():
    if x == "address":
        for a,b in y.items():
            print(a,":", b)
    else:
        print(x,":", y)

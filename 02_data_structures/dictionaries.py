"""
Topic: Dictionaries 
"""

# -----------------------------------
# Exercise
# -----------------------------------

"""
Build a nested dictionary representing a "student" (name,
grades as a list, address as another dictionary). Access a value 3 layers
deep.

"""

# -----------------------------------
# My Solution
# -----------------------------------

student = {
    "name" : "Muhammad Mustafa",
    "grades" : ["A","A-","A-","A"],
    "address" : {
        "city" : "Lahore",
        "block" :  "C",
    }
}

print(student["address"]["city"])


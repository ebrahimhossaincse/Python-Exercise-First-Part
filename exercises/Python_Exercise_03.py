'''
Exercise 03: Write a function that takes 2 numbers as arguments (age of two brothers)
and find who is elder
Hints: Use condition inside the function
'''

def find_older_brother(age1, age2):
    if age1 > age2:
        return "The first brother is older."
    elif age2 > age1:
        return "The second brother is older."
    else:
        return "Both brothers are the same age."

# Example Case 01
age1 = 25
age2 = 20
print(find_older_brother(age1, age2))

# Example Case 02
age1 = 25
age2 = 30
print(find_older_brother(age1, age2))

# Example Case 03
age1 = 25
age2 = 25
print(find_older_brother(age1, age2))
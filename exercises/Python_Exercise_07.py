'''
Write a function that takes 1 number as argument.
The function should return "Fizz" if the number is divisible by 3,
"Buzz" if the number is divisible by 5,
"FizzBuzz" if the number is divisible by both 5 and 3,
otherwise return "Not a Fizz-buzz number".
'''

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

# Example 01
number = 15
print(fizz_buzz(number))

# Example 02
number = 9
print(fizz_buzz(number))

# Example 03
number = 25
print(fizz_buzz(number))

# Example 04
number = 13
print(fizz_buzz(number))
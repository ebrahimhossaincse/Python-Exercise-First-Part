'''
Write a function that takes a number 1 to 9 from the user input (use input function inside a function).
Store a number in a variable (let’s assume 6).
If the input value is less than the variable, print "Your guess is almost there".
If the input value is greater than the variable, print "Your guess is higher".
If the input value and variable are equal, print "Your Guess Is Correct!".
'''

def guessing_game():
    stored_number = 5
    guess = int(input("Guess a number between 1 and 9: "))

    if(guess>=1 and guess<=9):
        if guess < stored_number:
            print("Your guess is almost there")
        elif guess > stored_number:
            print("Your guess is higher")
        else:
            print("Your Guess Is Correct!")
    else:
        print("please enter number bwtween 1 to 9")

# Example usage
guessing_game()
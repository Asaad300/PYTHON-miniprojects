import random

top_of_range = input("Enter the top of the range: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a valid number.")
    quit()

random_number = random.randint( 0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess= input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number.")
        continue
    if user_guess < 0:
        print("Please enter a number greater than or equal to 0.")
        continue
    if user_guess == random_number:
        print("You got it!")
        print("Attempt number",guesses)
        break
    elif user_guess < random_number:
        print("You were below the number.")
    else:
        print("You were above the number.")
    continue
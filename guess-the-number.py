import random

number = random.randint(0, 100)
print("Im thinking of a number between 0 to 100.")

guess = 10
if input("Easy or Hard? ") == 'hard':
    guess = 5
print(f"You have {guess} attempts remaining to guess the number.")
should_continue = True
while should_continue:
    user = int(input("Guess the number: "))
    if user > number:
        print("Too high")
    elif user < number:
        print("Too low")
    elif user == number:
        print(f"You got it! the answer was {number}")
        should_continue = False
    if should_continue:
        guess -= 1
        if guess == 0:
            print("You are out of guesses. You lose.")
            should_continue = False

        print(f"You have {guess} attempts remaining.")
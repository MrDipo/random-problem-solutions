import random

def getNum():
    return random.randint(1, 9)

no_of_guesses = 0 # extra
test_num = getNum()
print(test_num) # printing random value for easy debugging

while True:
    print("I picked a random number between 1 and 9, guess what it is:\n(Enter 'exit' to end game)")
    try:
        user_guess = input()
        if user_guess.lower() == 'exit': # extra
            break
        elif int(user_guess) not in range(1,10):
            print("Your guess is not between 1 and 9! Try again...")
        elif int(user_guess) == test_num:
            no_of_guesses += 1
            print(f"You guessed correctly in {no_of_guesses} tries, cool.")
            break
        elif int(user_guess) > test_num:
            no_of_guesses += 1
            print("You guessed too high, try again...")
        elif int(user_guess) < test_num:
            no_of_guesses += 1
            print("You guessed too low, try again...")
    except ValueError:
        print("Oops, that is not a valid number. Try again...")
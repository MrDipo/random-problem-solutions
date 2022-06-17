import random

def getNum():
    return random.randint(1, 9)


test_num = getNum()
user_guess = -1
print(test_num)
print("I picked a random number between 1 and 9, guess what it is:")

while user_guess != test_num:
    while True:
        try:
            user_guess = int(input())
            break
        except ValueError:
            print("Oops, that is not a valid number. Try again...")
    
    if user_guess not in range(1,10):
        print("Your guess is not between 1 and 9! Try again...")
    elif user_guess == test_num:
        print("You guessed correctly, cool.")
    elif user_guess > test_num:
        print("You guessed too high, try again...")
    elif user_guess < test_num:
        print("You guessed too low, try again...")
import random

def getNum():
    return random.randint(1, 9)

test_num = getNum()
print(test_num)
user_guess = int(input("I picked a random number between 1 and 9, guess what it is:\n"))

if user_guess == test_num:
    print("You guessed correctly, cool.")
elif user_guess > test_num:
    print("You guessed too high")
elif user_guess < test_num:
    print("You guessed too low")
import random

def getNum():
    return random.randint(1, 9)

play = 1
test_num = getNum()
print(test_num) # printing random value for easy debugging
print("I picked a random number between 1 and 9, guess what it is:")

while play:
    while True: # this while block executes until the guess is correct, and validates input
        try:
            user_guess = int(input())
            if user_guess not in range(1,10):
                print("Your guess is not between 1 and 9! Try again...")
            elif user_guess == test_num:
                print("You guessed correctly, cool.")
                break
            elif user_guess > test_num:
                print("You guessed too high, try again...")
            elif user_guess < test_num:
                print("You guessed too low, try again...")
        except ValueError:
            print("Oops, that is not a valid number. Try again...")

    play = int(input("Enter \'0\' to quit OR enter \'1\' to play again:\n"))
    test_num = getNum()
    print(test_num)
    print("I picked a new number, guess again:")
    
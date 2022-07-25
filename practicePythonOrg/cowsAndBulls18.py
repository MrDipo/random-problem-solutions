import random

# generate random 4 digit number
def fourNumGen():
    return tuple(str(random.randint(1000, 9999))) # this method excludes numbers starting with a 0. I can live with that


def compare(guess, answer):
    while True:
        i = 0
        cows = 0 # reset cow and bull count for each guess
        bulls = 0
        while i < 4:
            if guess[i] == answer[i]: # check if i-th digits of both numbers are the same 
                cows += 1
            elif guess[i] in answer: # if not, check if i-th digit is in the answer
                bulls += 1
            i += 1
        print(f"{cows} cows, {bulls} bulls")
        if cows == 4: return f"Congratulations, {''.join(answer)} is correct!"
        guess = tuple(input())


# set up variables
real_num = fourNumGen()
print("Welcome to the Cows & Bulls game!\nEnter a number:")
user_guess = tuple(input())

# start comparison
print(compare(user_guess, real_num))

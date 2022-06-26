from typing import List


def fib(x:int) -> List:
    if x == 1: return [1]
    if x == 2: return [1,1]

    seed_list = [1,1]
    for i in range(x): # could have used a while loop here, didn't. Oh well
        seed_list.append(seed_list[i] + seed_list[i+1])
        if len(seed_list) == x: break
    return seed_list


noOfFibs = int(input("How many numbers do you want in the sequence?:\n"))
print(fib(noOfFibs))
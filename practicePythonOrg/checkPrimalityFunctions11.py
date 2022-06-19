import math

def is_prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True # we have effectively filtered all non primes less than 9 at this point
    if n%3 == 0: return False # all factors of 3 are also not prime

    stop = int(math.sqrt(n)) # every pair of divisors lies either side of the sqrt, no need to check other divisor in pair

    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime (check if the next odd number is a factor)
    # then loop by 6.
    # checking odds only since every even number is automatically not prime
    f = 5
    while f <= stop:
        print("\t", f) # list every f until sqrt
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6 # check with every 6n ± 1 number
    return True

num = int(input("Enter a number to see if it is prime or not:\n"))
print(is_prime(num))
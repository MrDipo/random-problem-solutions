y = int(input("Supply me a number and I'll give you a list of divisors\n:"))

print([num for num in range(2, y) if y % num == 0])
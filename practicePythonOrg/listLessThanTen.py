a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num<5:
        print(num)

# Extras
# 2. Write this in one line of Python.
print([num for num in a if num<5])
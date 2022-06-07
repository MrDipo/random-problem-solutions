# Ask user for name & age
user_name = input("What is your name?\n:")
user_age = int(input("How old are you?\n:"))

#find a way to make this generic (not explicit)
print(f"Hi {user_name}, you will turn 100 years old by {2122 - user_age}")
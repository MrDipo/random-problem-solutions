import random
import secrets
import string

def strong_passkey(length:int):
    key = random.choice(string.ascii_letters+string.digits+string.punctuation, length)
    return key


print(strong_passkey(8))
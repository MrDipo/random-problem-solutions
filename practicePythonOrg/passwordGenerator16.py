import secrets
import string

def strong_passkey(length:int):
    # Using choice method from secrets to cryptographically generate a secure password
    key = ''.join(secrets.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(length))
    return key


def main():
    size = int(input("Please enter desired password length: "))
    print(f"Your secure password is:{strong_passkey(size)}")


if __name__ == "__main__":
    main()
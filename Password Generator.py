import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")
    length = int(input("Enter the desired length of the password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

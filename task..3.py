import random
import string

def get_user_input():
    print("Welcome to the Custom Password Generator!")
    length = int(input("Please enter the password length (8 or more characters): "))
    while length < 8:
        print("Password length must be at least 8 characters.")
        length = int(input("Please enter a valid length: "))
    include_numbers = input("Do you want to include numbers? (yes/no): ").lower() == 'yes'
    include_special = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
    return length, include_numbers, include_special

def generate_custom_password(length, include_numbers, include_special):
    char_pool = string.ascii_letters 
    if include_numbers:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def save_password_to_file(password):
    with open("generated_password.txt", "w") as file:
        file.write(f"Generated Password: {password}\n")
        print("Password saved to 'generated_password.txt'")

def main():
    length, include_numbers, include_special = get_user_input()
    password = generate_custom_password(length, include_numbers, include_special)
    print(f"your generated password is: {password}")
    save_password_to_file(password)

if __name__ == "__main__":
    main()
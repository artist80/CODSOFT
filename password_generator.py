#!/usr/bin/env python3

import random
import string

def generate_password(length=8, uppercase=True, lowercase=True, numbers=True, symbols=True):
	characters = ""
	if uppercase:
		characters += string.ascii_uppercase
	if lowercase:
		characters += string.ascii_lowercase
	if numbers:
		characters += string.digits
	if symbols:
		characters += string.punctuation

	if not characters:
		return "Error: No character set selected."

	password = ''.join(random.choice(characters) for _ in range(length))
	return password

def get_user_input():
	try:
		length = int(input("Enter the password length: "))
		uppercase = input("Should we add uppercase letters? (y/n): ").lower() == 'y'
		lowercase = input("Should we add lowercase letters? (y/n): ").lower() == 'y'
		numbers = input("Your password should contain numbers? (y/n): ").lower() == 'y'
		symbols = input("Your password should contain symbols? (y/n): ").lower() == 'y'

		return length, uppercase, lowercase, numbers, symbols
	except ValueError:
		print("Error! Please enter a valid integer for the password length.")
		return get_user_input()


if __name__ == "__main__":
	print("Welcome to the Strong Password Generator!")

	length, uppercase, lowercase, numbers, symbols = get_user_input()

	password = generate_password(length, uppercase, lowercase, numbers, symbols)

	print(f"Generated Password: {password}")
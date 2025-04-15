import random
import string

print("🔐 Random Password Generator")

length = int(input("Enter password length: "))

# Define characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print("Your secure password is: ", password)

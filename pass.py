print("PASSWORD GENERATOR")
import random
import string
x=int(input("Enter the lentgh:"))

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
password = generate_password(x)
print("Generated Password:", password)
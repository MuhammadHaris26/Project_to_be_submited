import random
import string

print("Welcome to Password Generator:")
def password_generator():
  length = int(input("Enter the Password Length"))
  if length < 6:
    return "Password Shoud be at least 6 characters"

  letters = string.ascii_letters
  digits  = string.digits
  symbols = string.punctuation

  characters = letters + digits + symbols

  password = " "

  for c in range(length):
    password += random.choice(characters)

  print("Your Password is ", password)
password_generator()

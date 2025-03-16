import random

def guess_the_number(x):
    print("Welcome to the Guess the Number Game!")
    low = 1
    high = 'x'
    feedback = ''
    while feedback != 'c' and low != high:
      guess = random.randint(1, x)
      feedback = input(f"Is {guess} too high (H), too low (L) or correct(C)")
      if feedback == "h":
        high = guess - 1
      elif feedback == "l":
        low = guess + 1
      else:
        print(f"Aww! The computer guessed your number, {guess} , correctly")
guess_the_number(20)
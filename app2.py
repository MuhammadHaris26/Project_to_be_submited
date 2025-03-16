import random
def guess(x):
 random_number = random.randint(1,x)
 guess = 0
 while guess != random_number:
  guess = int(input("Guess a number between 1 and {x}"))
  if guess < random_number:
    print("Sorry, too low")
  elif guess > random_number:
    print("Sorry, too high")
  else:
    print("Congratulations! You guessed the number")

guess(10)
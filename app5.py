import random

word_list = ["python" , " programming" , "agentic" , "university" , "class"]

word = random.choice(word_list)
word_letters = list(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts >0:
  display_word =[letter if letter in guessed_letters else "_" for letter in word]
  print("word:", " ".join(display_word))

  if "_" not in display_word:
    print("Congratulations! You guessed the word:", word)
    break
  guess = input("Guess a letter:").lower()
  if guess in guessed_letters:
    print("You already guessed that letter.")
    continue

  guessed_letters.append(guess)
  if guess in word_letters:
    print("Good guess!")

  else:
    attempts -= 1
    print("Wrong guess.Attempts left:", attempts)
if attempts == 0:
  print("You lost! The word was:", word)
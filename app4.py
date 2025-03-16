import random
def play():
  user_input = input("What's your choice? 'r' for rock , 'p' for paper , 's' for scissors")
  computer = random.choice(['r' , 'p' , 's'])
  if user_input == computer:
    return 'tie'
  if is_win(user_input, computer):
    return "You won!"
  else:
    return "You lost!"


def is_win(player,opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
  or (player == 'p' and opponent == 'r'):
   return True
print(play())
import random

options = ("rock", "paper", "sissors")
running = True

print("welcome to paper rock sissors game")

palyer = input("enter a username ")
while palyer == "" or palyer == " ":
  print("the username cannot be an empty space")
  palyer = input("enter a username ")
  print(f"your name is {palyer}")

while running:
  
  choices = None
  computer = random.choice(options)

  while choices not in options:
    choices = input("choose rock or paper or sissors ")
    if choices not in options:
      print(f"{choices} is not in the game")
    else:
     print(f"you choose {choices}")
  
  print(f"the computer choose {computer}")

  if choices == computer:
    print("draw")
  elif choices == "paper" and computer == "rock":
    print(f"{palyer} won")
  elif choices == "rock" and computer == "sissors":
    print(f"{palyer} won")
  elif choices == "sissors" and computer == "paper":
    print(f"{palyer} won")
  else:
    print("you lose to the computer")

  pl = input("play again n/y ")
  if pl.lower() =="y":
    running == True
  elif pl.lower() == "n":
    print("you quit")
    running == False
    break
  else:
    print("enter y/n")

print("thanks for playing")
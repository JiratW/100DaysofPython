rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)
if player >= 3 or player < 0:
  print("You type invalid choice, you lose!!!")
else:
  print(choice[player])
  print(f"\nComputer choose:\n{choice[computer]}\n")

  if player == 0 and computer == 0:
    print("You draw")
  elif player == 0 and computer == 1:
    print("You lose")
  elif player == 0 and computer == 2:
    print("You win")
  elif player == 1 and computer == 0:
    print("You win")
  elif player == 1 and computer == 1:
    print("You draw")
  elif player == 1 and computer == 2:
    print("You lose")
  elif player == 2 and computer == 0:
    print("You lose")
  elif player == 2 and computer == 1:
    print("You win")
  # elif player == 2 and computer == 2:
  else:
    print("You draw")
  print("\n---\n")

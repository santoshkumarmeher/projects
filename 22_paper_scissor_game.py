import random
paper=('''
     _______  PAPER
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
scissor=('''
    _______   SCISSOR
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

rock=('''
    _______   ROCK
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

game_image = [paper,scissor,rock]
user_choice = int(input("Enter 0 for Paper,1 for Scissor,2 for Rock \n "))
if user_choice >= 3 or user_choice<0:
    print("You type an invalid number")
else:
    print(game_image[user_choice])
computer_choice = random.randint(0,2)
print(f" computer choice is:")
print(game_image[computer_choice])

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice>computer_choice:
    print("you win")
else:
    print("You lose")
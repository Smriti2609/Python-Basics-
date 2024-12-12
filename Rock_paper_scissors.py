# Rock Paper Scissors ASCII Art 
print("Welcome to the rock paper scissors Game!")
import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors] 

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#0,1,2
if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(game_images[user_choice])

computer_choice = random.randint(0, 2) 
print("Computer chose:")   
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice: #0 = rock ,1 = paper, 2 = scissors
    print("You lose!")
elif user_choice > computer_choice :
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")




#or we can also generate the computer choice by following the command:
#rock_paper_scissors = [rock, paper, scissors]
#random_choice_of_computer = random.choice(rock_paper_scissors)
#print(f"Computer chose: {random_choice_of_computer}")
#When we don't want to use integer 0,1,2 then ,we can use the above code.
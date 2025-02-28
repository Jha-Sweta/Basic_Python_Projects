"""
Project: Rock Paper Scissors
Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a 
corresponding variable: rock, paper, and scissors. 
This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
"""
import random
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

choices = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock Paper Scissors!")

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
if user_choice in ['0', '1', '2']:
    player_choice = int(user_choice)
else:
    print("Invalid input. Please enter 0, 1, or 2.")

computer_choice = random.randint(0, 2)

print("\nYou chose:")
print(choices[player_choice])
print(names[player_choice])

print("\nComputer chose:")
print(choices[computer_choice])
print(names[computer_choice])

if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")


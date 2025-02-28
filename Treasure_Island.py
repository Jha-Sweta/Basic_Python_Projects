"""
Project: Treasure Island
Instructions
Make your own "Choose Your Own Adventure" game. 
Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

Text Snippets from my example
'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."

"""
print("Welcome To The Treasure Island.\nYour Mission Is To Find The Treasure. ")
print("")
print('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
choice1=input()
if choice1=="left" or choice1=="Left" or choice1=="LEFT":
    print('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
else:
    print("Fall into the hole.\nOpps...! Game Over")

choice2=input()
if choice2=="Wait" or choice2=="wait" or choice2=="WAIT":
    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
    choice3=input()
    if choice3=="red" or choice3=="Red" or choice3=="RED":
        print("Burned By Fire. Game Over..")
    elif choice3=="yellow" or choice3=="Yellow" or choice3=="YELLOW":
        print("You Win!")
    elif choice3=="blue" or choice3=="Blue" or choice3=="BLUE":
        print("Eaten By Beasts. Game Over.")
    else:
        print("Game Over..")
else:
    print("You get attacked by an angry trout. Game Over.")
"""
Instructions
This is a difficult challenge. 💪
You are going to write a program that will mark a spot on a map with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
[['⬜', '⬜', '⬜'],['⬜', '⬜', '⬜'],['⬜', '⬜', '⬜']]
This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
First, your program must take the user input and convert it to a usable format.
Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:
[['⬜', '⬜', '⬜'],['⬜', '⬜', '⬜'],['⬜', '⬜', '⬜']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜', '⬜', '⬜']
['⬜', '⬜', '⬜']
️️', 'X',️️']
"""

line1 = ["⬜","⬜","⬜"]
line2 = ["⬜","⬜","⬜"]
line3 = ['⬜','⬜','⬜']
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") # Where do you want to put the treasure?
#  Do🚨n't change the code above 
# 👆Write your code below this row 
letter= position[0]
abc=["A","B","C"]
alpha_index=abc.index(letter)
number=position[1]
number_index=int(number) -1
map[number_index][alpha_index]="X"
#👇 Write your code above this row 
# 👆 Do🚨n't change the code below 
print(f"{line1}\n{line2}\n{line3}")
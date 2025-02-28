"""
Instructions
💪 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:
Take both peoples names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is *z*."

e.g.
name1 = "Virat Kohli"
name2 = "Anushka Sharma"
T occurs 1 times
R occurs 2 time
U occurs 1 times
E occurs 0 times
TRUE Total = 4

L occurs 1 time
O occurs 1 times
V occurs 1 times
E occurs 0 times
LOVE Total = 3

Love Score = 43

Print: "Your score is 43, you are alright together."

These functions will help you:
lower() count()

Example Input 1
Virat Kohli
Anushka Sharma
Example Output 2
The Love Calculator is calculating your score...
Your score is 43, you are alright together.

Example Input 2
Deepika Padukone
Ranveer Singh
Example Output 1
The Love Calculator is calculating your score...
Your score is 87.

Hint
You can check your values against mine using this table:

Name 1	        Name 2	              Score
Kiara Advani    Sidharth Malhotra	    53
Aishwarya Rai	Abhishek Bachchan	    31
Alia Bhatt	    Ranbir Kapoor	        53
Mira Kapoor	    Shahid Kapoor	        34
Katrina Kaif	Vicky Kaushal	        32
Genelia Dsouza	Riteish Deshmukh	    86

"""

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is their name?\n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true_c=0
love_c=0
names=name1+name2
true_c+= names.count("t") or names.count("T")
true_c+= names.count("r") or names.count("R")
true_c+= names.count("u") or names.count("U")
true_c+= names.count("e") or names.count("E")

love_c+= names.count("l") or names.count("L")
love_c+= names.count("o") or names.count("O")
love_c+= names.count("v") or names.count("V")
love_c+= names.count("e") or names.count("E")

score=int(str(true_c)+str(love_c))

print("The Love Calculator is calculating your score...")

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<=score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")





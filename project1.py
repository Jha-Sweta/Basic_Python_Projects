"""
Sample Output:
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
Mumbai
What's your pet's name?
Daizy
Your band name could be Mumbai Daizy
"""


#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

#2. Ask the user for the city that they grew up in.
_city_name=input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
_pet_name=input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
_band_name=_city_name +" "+_pet_name

#5. Make sure the input cursor shows on a new line:
print("Your band name could be",_band_name)
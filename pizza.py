"""
Project: Pizza Order
Instructions
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): ₹120
Medium pizza (M): ₹190
Large pizza (L): ₹250
Add pepperoni for small pizza (Y or N): +₹15
Add pepperoni for medium or large pizza (Y or N): +₹20
Add extra cheese for any size pizza (Y or N): +₹10
Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: ₹270.
"""
print("Thank you for choosing Python Pizza Deliveries!")
total_bill=0
size = input("What size pizza do you want? S, M, or L\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("# Do you want pepperoni? Y or N\n") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N\n") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size=="s" or size=="S" :
    total_bill=120
    if add_pepperoni=="y" or add_pepperoni=="Y":
        total_bill+=15
elif size=="m" or size=="M":
    total_bill=190
    if add_pepperoni=="y" or add_pepperoni=="Y":
        total_bill+=20
elif size=="l" or size=="L":
    total_bill=250
    if add_pepperoni=="y" or add_pepperoni=="Y":
        total_bill+=20

if extra_cheese=="y" or extra_cheese=="Y":
    total_bill+=10

print(f"your bill is {total_bill}Rs")
    
    
    
    
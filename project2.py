'''Instructions
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


Example Input
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10%, 12%, or 15%? 12
How many people to split the bill? 7
Example Output
Each person should pay: $19.93'''

print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? "))
tip_in_per=int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
num_of_persons=int(input("How many people to split the bill? "))
tip=tip_in_per/100
bill_div=total_bill/num_of_persons
final_tip=(total_bill/num_of_persons)*tip
final_amount=round(bill_div+final_tip,2)
print(f"Each person should pay: {final_amount}")

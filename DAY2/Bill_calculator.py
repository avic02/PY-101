# PROJECT END DAY 2 : making a Bill Calculator

print("welcome to this bill calculator")

bill = float(input("please enter the total bill amt below $:\n"))

people_counter = int(input("How many people are contributing in total =\n"))

tip_choice = int(
    input("how much tip would you be providing : 10 , 12 or 15 \n"))

message = f"your bill total is {bill} which is being split btw {people_counter} with a tip inclusive of {tip_choice}%\n"

print(message)

tip_incl_bill = tip_choice / 100 * bill + bill

print(f"total bill for whole group comes out to be =  {tip_incl_bill} $ \n")

per_person = tip_incl_bill / people_counter

final_amt = round(per_person, 2)

print(f"Each one owes = {final_amt} $")

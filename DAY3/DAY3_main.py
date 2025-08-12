# LESSON 1: 'if' or 'else' are used to provide True or False statement which depends on the user input . Also you can use 'elif' which can be a used to create multiple conditions inside the if/else statement :

print("welcome to ZOOLAHOO Ride at wonderla")
height = int(input("please enter height in cms:"))
age = int(input("what is your age in Yrs:"))
if height > 140 :
  print("welcome you can ride the rollercoster")
  if age < 12 :
   print("your ticket cost is 5 $")
  elif age <= 18 :
    print("your ticket cost is 7 $")
  else :
    print("your ticket cost is 12 $")

else:
  print("you are not allowed on this ride sorry")

# There are comparison operators which can be classified : >  , <  , >= (greater than or equal to) ,  <= (less than or equal to) , == (equal to) or != (not equal to) .

# you cant use '=' in an if/else fn since this doesnt show a condition and gives syntax ERROR.
# '=' means you are assigning a value to the variable whereas "==" means you are checking the statement .

#LESSON 2 : using a modulo '%' to distinguish a odd even determination is it simply tries to divide and deduces its remainder  .

number = int(input("enter a number to be checked: "))

if number % 2 > 0 :
  print("this number is ODD")
else :
  print("this number is EVEN")

# PROJECT 1 :-Making a BMI CALCULATOR using if /else/ elif

print("WELCOME TO BMI 2.0 CALCULATOR")
height_bmi = float(input("enter your height in mtrs :"))
weight_bmi = float(input("enter your weight in kgs :"))

bmi_calculated = round(weight_bmi / height_bmi ** 2)

if bmi_calculated < 18.5 :
  print("you are UNDERWEIGHT stuff some food down your GOBB")

elif bmi_calculated <= 25.0 :
  print(f"you are in NORMAL RANGE with BMI {bmi_calculated} . CONGRATULATIONS")

elif bmi_calculated <= 30.0 :
  print(f"you are OVERWEIGHT with BMI {bmi_calculated} plz eat sensibly")

elif bmi_calculated <= 35.0 :
  print(f"you are OBESE with BMI {bmi_calculated}   Go join a gym and get that belly in you couch")

else :
  print(f"you are CLIINICALY OBESE with BMI {bmi_calculated}. There is no hope left start praying for a new pacemaker GOODLUCK LOL !")

# PROJECT 2 : Make a leap year deducer with condition that if evenly divides by 4 ,except that yr is evenly divisible by 100 unless yr is evenly divided by 400 :

year = int(input("Enter the year to check for leap yr here:"))

if year % 4 == 0 :
  print(f"The year entered {year} is LEAP YEAR.")
elif year % 100 == 0 :
  print(f"The year entered {year} is not LEAP YEAR.")
elif year % 400 == 0 :
 print(f"The year entered {year} is not LEAP     YEAR.")
else :
  print(f"The year entered {year} is not LEAP     YEAR.")

# Remember always layout the map for logic before you start coding to have a bigger picture of project !!

# EDITED LESSON 1 PROJECT : IF / IF / ELIF/ ELSE

print("welcome To Wonderla")

height = int(input("please enter height in cms:"))

age = int(input("what is your age in Yrs:"))

bill = 0

if height > 140 :
  print("welcome you can ride the rollercoster")

  if age < 12 :
   bill = 5
   print("your ticket cost is 5 $")

  elif age <= 18 :
    print("your ticket cost is 7 $")
    bill = 7

  elif age >= 45 and age <= 55 :
    print("your ticket is on the house . Enjoy your mid life crisis to the fullest.")

  # Refer to LESSON 3 below on logical operators to understand the code above.

  else :
    print("your ticket cost is 12 $")
    bill = 12

  want_photos = input("Do you want to click picture ? type Y OR N :")

  if want_photos == "Y":
    bill = bill + 3
    print(f"Now your ticket cost is {bill} $ due to add-on photo.")

  else :
    print(f"Now your ticket cost is {bill} $ with no add-on photo.")

else:
  print("you are not allowed on this ride sorry")

# NOTE : from above technique we learned that using the 'if' fn inside a pre-existing if /else allows us to take multipe inputs from user . also we added the variable 'bill =' to add 3$ into the value which previousl was a string .

# PROJECT 3 :CREATE A PIZZA ORDER DELIVERY CALC

print("WELCOME TO PYTHON PIZZERIA .\nPlease place your order below !!!!")

size = input("what size pizza do you wish to get? S / M / L :")

add_cheese = input("Do you wish to add extra cheese in pizza? Y OR N :")

add_pepperonin = input("Do you wish to add extra peperoni in your pizza? Y OR N :")

bill = 0

if size == 'S':
  bill += 15

elif size == 'M':
  bill += 20

else :
  bill += 25

if add_pepperonin == "Y" :
    if size == 'S':
      bill += 2
    else :
      bill += 3

if add_cheese == "Y" :
    bill += 1
    (print(f"your outstanding bill along with                   the  add-ons is {bill}\n"))
else :
  bill += 0
  (print(f"your outstanding bill along with NO CHEESE is {bill}\n"))

print('THANK YOU FOR VISITING PYTHON PIZZERIA \n HAVE A NICE DAY CUTIPIE MUAAH!')

#LESSON 3: LOGICAL OPERATORS

#To include multiple conditions in same if/else statements using different conjuctures like and / Or / not .

# e.g; if A> B and A > C                         using AND operator -> both conditions need to be TRUE for the statement to be be interpreted as TRUE.                                                   using OR operator -> any one of 2 conditions need to be TRUE . if both are FALSE then it is FALSE .                                                                             using NOT operator -> you can use this to reverses any condition . so if its TRUE it becomes FALSE and vise-versa.

# PROJECT LOVE CALCULATOR :                         TIPS @! : using the .lower () fn we convert our statement into lowercase .                                                               using .count ("") fn you can specify a specific subscript / letter in this case inside ("") to extract that for counting.               REMEMBER !! this count fn is Case Sensitive so 'A' & 'a' is treated diffrently inside same word.

print("WELCOME TO LOVE CALCULATOR:")

name_1 = input("please enter your name here:\n")
name_2 = input("please enter the name of Him/Her:\n")

combined_name = name_1 + name_2

combined_lower = combined_name.lower()


t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l =combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

your_love_score = str(true) + str(love)

your_love_score = int(your_love_score)

if your_love_score >= 90 or your_love_score <= 10:
 print(f"your love score is {your_love_score}. Start planing the honeymoon swoony")
  
elif your_love_score >= 40 and your_love_score <= 50 :
  print(f"your love score is {your_love_score}.There is potential keep at it guys!")

else :
  print(f"your score is {your_love_score}. start looking for someone else this boat has sailed.")

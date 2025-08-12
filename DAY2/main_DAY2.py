#LESSON 1 : Data types of various kinds which can be classified as : Strings , Booolean , Integers & Float.

# Diff btw data type : 
print("123" + "456") 

print(123 + 456) 

# we always count from number 0 instead of 1 eg;as seen in below example that using 0 returns 'h' because that is the 1st chrcter noted by computer  

print("hello"[0]) 

#this method of pulling out a specific chars is called 'Subscripting'

# ** use cmmnd [ctrl + /] to convert into comment

# num_chrs = len(input("what is your name?"))
# print("your name has" + num_chrs +"characters.")

# this above code will give you a type error as interger & strng cant be conjoined using '+' fn. Instead do this :

num_chrs = len(input("what is your name?\n"))

new_num_chrs = str(num_chrs)

print("your name has " + new_num_chrs +" characters.")

#LESSON 2 :to subscript an input and print its sum ie; input = 55 then you print '5 + 5 = 10' :

digit_numb = input("enter your 2 digit numb here:")

print(type(digit_numb))

first_digit = digit_numb[0]
second_digit = digit_numb[1]

# by default input fn takes strng data type which needs to be converted to an int for it to be summed!

result = (int(first_digit) + int(second_digit)) 
print(result)

#LESSON 3 :P.E.M.D.A.S is the order followed for executing multiple mathematical cmnds in same line :

# parenthesis
# exponents 
# multiply 
# divide 
# Addition 
# Subtraction 

print(3 + 6 - 19 + 50 * 2 / 3)

#PROJ WORK 1 -creating a BMI CALCULATOR , but the result shld be a whole number :

height = input("enter your height here(mtr):")
bodyweight = input("enter your bodyweight here(kg):")

BMI_var = int(bodyweight) / float(height) ** 2

result= int(BMI_var)

print(result)

if result > 25 :
 print("your are FAATHH GO TO GYMMMHH")
else :
  print("you are SLIM LOOKINN ")

# data type conversions : 

print(8 / 3) # thhis gives a float data type whereas,

print(8 // 3) # this will convet it to an int. 

print(8 / 3 , 3) # result will be rounded off to 3 decimal

# LESSON 4 : Use the 'f' strng type to help automatically identify the respective data type inside the input.

score = 0
height = 1.9 
winning = True
print(f"your score is {score} ,your height is {height  } , your wining {winning}")

# PROJ WORK - create a life cycle in weeks chart which shows how many weeks , mmths and days are left if a person lives upto 90 yrs max :

age = input("enter your real age here :\n")

Life_left = 90 - int(age)

months_remain = Life_left * 12 
weeks_remain = Life_left * 52
days_remain  = Life_left * 365

message = f"you have {months_remain} mnths , {weeks_remain} weeks, and {days_remain} days left in this lifetime.\n START GRINDING BOI \n TIME IS MONEY"

print(message)
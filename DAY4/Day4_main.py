# DAY 4 : LESSON 1 : using random module to seek randomized number with diffrent fn -
import random   

random_integer = random.randint(1, 10)
print(random_integer)
 
random_float = random.random() # random.random returns a flaot but it doent include the int 
print(random_float)

# if I set the range to be from 0 to 5 then the console will take range to be 0.0000... to 4.9999.. excludes 5.0
randomfloat = random.random() *  5
print(randomfloat)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

#Code Ex: to make a Coin toss simulator : assign a random number from 0 to 1 to a variable called toss_outcome. if toss_outcome is 0 then print tails else print heads.

import random 

toss_outcome = random.randint(0,1)
if toss_outcome == 0 :
    print("Tails")
else :
    print("Heads")   

# LESSON 4 : LISTS :
# lists are used to store multiple items of diff data types in a single variable.
# using append fn to add one item to the list.  
# using extend fn to add multiple items to the list.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
"New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", 
"Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", 
"Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", 
"Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]    

states_of_america.append("argintina")
states_of_america.extend(["bangladesh", "pakistan", "nepal"])
print(states_of_america)

# Code ex : To make a bankers russioan roullete :- the names are entered and picked one out randomly ,this person  has to pay the entire bill
# using str.split(",") fn we can convert a bunch of strings taken from user into list by seperating by comma.

name_bankers = input("Enter the name of the Bankers here seperated by commas :")

new_names = name_bankers.split(",") 

list_range = len(new_names)

# As observed new_names now becomes a list due to the str.split() function 
# the main problem with this code ex is that you cant enter a range for random module to operate as the names of bankers is not fixed ,it cld be 3 or 10(user dependant)
# here len() fn can be used to determine no.of strn present inside the list.

import random  
random_banker = random.randint(0 , list_range-1)
print(f"{random_banker} is going to pay the bill today") 

# # we do -1 from list because acc .to len() fn the list start from 1 instead of 0 but acc. to list the 1st str is denoted by [0] 
# # look at Ex of states of america above : the total states acc to len () will come out to be 50 but for list there are 49 states as [0] = Delaware .
# print(f"{new_names[random_banker]} get your wallet out cause its turn today!")

# we can also use random.choice() fn to pick a random item from the list but need to understand the logic behind it as shown above.

# random_banker = random.choice(new_names)
# print(f"{random_banker} is going to pay the bill today")

# LESSON 2 : NESTED LIST - A list containing multiple list usualy indentified with [[]] double sq bracekts .

list_1 = ['tomatoes' , 'tangerines' , 'lemons' , 'spinach']
list_2 = ['apples' , 'oranges' , 'papapya' , 'banana']
list_3 = ['salt' , 'pepper' , 'soy sauce']
list_mix_1 = [list_1 + list_2 + list_3]
print(list_mix_1)

# Code ex : Treasure Hunt - make a list with row and column specified to mark a coordinate .
#  Then ask the user to enter a coordinate (row,column) ex; (2,3) means 2nd row 3rd column to mark an 'X' in its place.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position  = input("enter the co-ordinate where the treasure chest goes :")


horizontal_postn = int(position[0])
vertical_postn = int(position[1])

print(f"column No is :{horizontal_postn} \n Row No is :{vertical_postn}")

selected_row = map[vertical_postn - 1]
selected_row[horizontal_postn - 1] = 'X'  

print(f"{row1}\n{row2}\n{row3}")

# !! tricky to understand : 'selected_row' variable defines the row user needs then in that row the column is defined by using '[]' 
# for eg; if input says 32{vertical becomes -> '2' & horizontal becomes -> '3'}  
# then it means 3rd column 2nd row hence selected_row = map[v - 1] ie; selected_row = map[2-1]=> map[1] which for the list means 2nd row because list starts form '0'
# now once row is estb then map[1][h-1] => map[1][3-1]=>map[1][2] means ki 2nd row ka 3rd datatype (because list mai 2 = 3rd as there is +1 )
 













    





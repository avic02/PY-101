#PROJECT NAME: PASSWORD GENERATOR

# the password generated can be either random or arranged according to preset conditions.
import random as rnd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))

#if nr_letters == 0 or nr_symbols == 0 or nr_numbers == 0 :
#    print("you have entered wrong input .PLEASE TRY AGAIN")
#else:
#    password_letter = [rnd.choice(letters) for _ in range(nr_letters)]
#    password_number = [rnd.choice(numbers) for _ in range(nr_numbers)]
#    password_symbol = [rnd.choice(symbols) for _ in range(nr_symbols)]
#    password = password_letter+password_number+password_symbol

# password = ""  instead of using empty strg in password we make a list since we need to join them OR append them which is only done in list.

password_list = [] 

for char in range (1, nr_letters + 1):
    # password_list += rnd.choice(letters) instead of using += we can use .append() fn to add to the list in loop .
    password_list.append(rnd.choice(letters))

for char in range (1, nr_numbers + 1): 
    password_list += rnd.choice(numbers) 
   

for char in range (1, nr_symbols + 1):
    password_list += rnd.choice(symbols) 


print(f"original password list: {(password_list)}")
print(rnd.shuffle(password_list))            
# we use the shuffle.() fn as an inbtw fn which means it can't iterate chrs of variable.example ; 
# had you written print(rnd.shuffle(password_list)) it will return none since it can't process the print fn along with shuffling fn so always write it seperately before printing the list of shuffled chrs.

print(f"shuffed password list: {(password_list)}")

password = "" 
for char in password_list:
    password += char
print(f"final password: {password}")

# typing line 47 to 50 allows us to print the list as a single strng form where all the chars have been added to form one single wording.
# ex; before coding it will show ==> shuffed password list: ['I', '6', '#', 'a', '+', 'J', 'g', 'I'] 
# after coding it will show ==> shuffed password list: I6#agI+JgI
# the code takes the shuffled list generated in line 45 and adds up each chrs of the list to form a password.


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

if nr_letters == 0 or nr_symbols == 0 or nr_numbers == 0 :
    print("you have entered wrong input .PLEASE TRY AGAIN")
else:
    password_letter = [rnd.choice(letters) for _ in range(nr_letters)]
    password_number = [rnd.choice(numbers) for _ in range(nr_numbers)]
    password_symbol = [rnd.choice(symbols) for _ in range(nr_symbols)]
    password_genNEW = password_letter+password_number+password_symbol

print(f"original password: {(password_genNEW)}")
rnd.shuffle(password_genNEW)
print(f"shuffed password: {''.join(password_genNEW)}")

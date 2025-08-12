import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock , paper , scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_choice = game_list[user_input]

if user_input >= 3 or user_input < 0 : # to make sure user doesnt enter a number outside range (0,2)
    print("YOU HAVE ENTERED WRONG INPUT")
else:    
    print(f"you chose {user_choice}")

CPU_input = int(random.randint(0,2)) 
CPU_choice = game_list[CPU_input]

print(f"CPU choses {CPU_choice}")

#rule of game rock beats scissors ; scissor beats paper ;paper beats rock now as rock = 0 ,ppr = 1 & scissors = 2 
# subsituting the rules in numeric form we get 2 > 1 ; 1 > 0 ; 0 > 2 & 0=0 (draw case).


if user_input == CPU_input: # for draw scenario ex : rock v/s rock etc.
    print("THIS MATCH IS A DRAW")
elif user_input == 0 and CPU_input == 2: #rock(0) beats scissors(2)
    print("YOU WIN")
elif CPU_input == 0 and user_input == 2: 
    print("YOU LOSE")
elif user_input > CPU_input :  
    print("YOU WIN!")
elif CPU_input > user_input :
    print("YOU LOSE")
  
       
     





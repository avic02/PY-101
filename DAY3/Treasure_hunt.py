# DAY 03 FINAL PROJECT:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island of Dungeons and Dragons .")

print("Your mission is to find the treasure and hopefully be alive in one piece.\n\nLET THE GAMES BEGIN CHILD!") 
lvl_diff = input("choose level of difficulty : Hard / Harder / Hardest: H1 /H2 /H3?\n")

if lvl_diff == "hardest" or lvl_diff == "H3":
          print("You are the choosen one please enter .\n THE ONLY RULE IS DONT DIE ")
else :
          print("You are a loser go harder come onnnn!!")
          
Location = input("Enter the location ? Urban OR Rural :")

Location = Location.lower()

if Location == "rural":
          choice_1 = input("choose LAND OR SEA : L OR S ?")
          if choice_1 == "S":
                    print("You just encountered with GHOST OF SALTMARSH \n You are dedddhhh ")
          if choice_1 == "L":
                    choice_2 = input("choose to enter Zombies or vampire camp :Z / V ?")
                    if choice_2 == "Z":
                              print("you entered the zombie camp ")
                              choice_3 = input("would you fight them or run : F / R?")
                              
                              if choice_3 == "F":
                                        print("you choose to fight the zombies but got outnumberd .YOU ARE DEDHHHHH!")
                                        
                              elif choice_3 == "R": 
                                        print("You escaped and came across a treasure chest : what wld you do ?")
                                        choice_4 = input("open or leave game :")
                                        
                                        if choice_4 == "open" or choice_4 == "O" :
                                                  print("There was a zombie siting inside the dummy chest .He bit you \n YOU ARE DEADDDDDHHH.")
                                                  
                                        if choice_4 == "leave" or choice_4 == "L":
                                                  print("You came across a princess who had the treasure chest . She asked you to choose a number btw 1 and 100 .")
                                                  
                                        choice_5 = int(input("enter a number btw 1 and 100:"))
                                        
                                        if choice_5 > 50 and choice_5 < 90 : 
                                                  print("YOU WON CONGRATULATIONS ON WASTING YOUR TIME")
                                        
                                        
                    elif choice_2 == "V":
                              print("You entered vampire's cave and he sucked the blood out of you . YOU ARE DEADDDDDHHHH!!  ")
                    else : 
                              print("WRONG INPUT ENTERED. RETRY ")


          
else : 
          print("WRONG INPUT ENTERED. RETRY ")


          
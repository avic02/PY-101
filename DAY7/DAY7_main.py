#HANGMAN GAME : Prepare a game logic and use conditional operators 

import random 

hangman_lives = [
'''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]
 
# ramdom.choice() > selects characters randomly based on the specified length (k)

index_lives = -1 

word_list = ["aardvark" , "baboon" , "camel" , "astonishing" , "fifa"]

word_selected = random.choice(word_list)
print(word_selected)

# hangman = []                              #Dont use the list approach since it's more complex to replace 
# for letter in word_selected :
#     hangman.append("_")
# print(hangman)

game_over = False

total_lives_remain = len(hangman_lives)

placeholder = ""

correct_letter_stored = []

word_length = "" #this variable will hold the word choosen and the spaces to fill it by user.

choosen_wordlen = len(word_selected) # introduced this variabel to get the no of chrs present in the choosen random word 

for chrs in range(choosen_wordlen):
    word_length += "_"
print(word_length)

# for chrs in word_selected : 
#     word_length += "_"
# print(word_length)

while not game_over :

    user_guess = input("Guess the letter :").lower()   # to make it more simplified when guessing make all unified
    print(user_guess) 

    for letter in word_selected : 
            if letter == user_guess :
                placeholder += user_guess
                correct_letter_stored.append(user_guess)

            elif letter in correct_letter_stored :  # we wrote this line of code to create an empty list that restores the memory for the correct letter guessed by user.
                 placeholder += letter 

            elif letter not in user_guess :  
                total_lives_remain -= 1
                print("YOU GUESSED THE WRONG LETTER !") 
                index_lives += 1
                print(hangman_lives[index_lives])
                
            else :
                placeholder += "_"

    if "_" not in placeholder:
         game_over == True
         print("You have guessed all the letters .CONGRATULATIONS !!")

    elif total_lives_remain == 0 :
         game_over == True
         print("ALL LIVES EXHAUSTED, GAME OVER!") 

print(placeholder)


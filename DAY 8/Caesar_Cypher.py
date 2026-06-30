
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar ():
    caesar_cypher = ""
    for letter in user_text:

        # Handle non-alphabet characters (like spaces or punctuation) safely
        if letter not in alphabets:
            caesar_cypher += letter
            continue

        if direction == "encrypt":
            new_position = alphabets.index(letter) + shift_place
            in_range = new_position % 26
            caesar_cypher += alphabets[in_range]
                   

        elif direction == "decrypt":
            
            new_position = alphabets.index(letter) + (shift_place * -1) 
            in_range = new_position % 26
            caesar_cypher += alphabets[in_range]

    print(f"This is the {direction}ed word: {caesar_cypher}")     

cyphering = True

while cyphering == True :
    
    direction = input ("Type encrypt Or decrypt : \n").lower()

    user_text = input("enter the text here :").lower()

    shift_place = int(input("How many places to shift ? : \n"))

    caesar()

    looper = input("Do you wish to continue type 'yes' or end the cypher type 'no' :  \n").lower()

    if looper == "no":
        cyphering == False
        print("Caesar Cypher ends here . Thnk you !")
        break

    
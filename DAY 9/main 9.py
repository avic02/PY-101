# DICTIONARIES : A data str that allows us to keep the key = value format inside together enclosed in {}.
# syntax : program_dict = {"Avinash": "sona" , "Abhinav":"shampy" , "KK":"R"}
# syntax : print(program_dict["Avinash"]) -> returns the value of key that is  => sona 
# To append a new key with its value -> program_dict["Harsh"] = "Hunter X" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {} 

#Remember that looping through a Dictionary will only give you the keys and not the values.Hence we say for key in instead of value.

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

for key in student_scores :
    
    score = student_scores[key]
    
    if score >= 91 :
        student_grades[key]=  "Outstanding"
    
    elif score >= 81 :
        student_grades[key]=  "Exceeds Expectations"    
        
    elif score >= 71 :
        student_grades[key] = "Acceptable"
        
    else :
        student_grades[key] = "Fail"
        
print(student_grades)

#Nested list : you can have a list as value for a key incide a dictionary
# Q
travel_log = {
    "france" : ["paris" , "lille" , "dijon"],
    "Germany": ["stutgart" , "Hamburg" , "Bonn"]
} 

# to call "lille" we can use the syntx: dict_variable_name["key"[index of strng to be called from nested list]]
print(travel_log["france"][1]) # >> in order to call specific data from list enter the index in sequence using []

# Q
travel_log = {
    "france" : ["paris" , "lille" , "dijon"],
    "Germany": ["stutgart" , "Hamburg" , "Bonn"],
    "UK" : ["made up of 7 islands", ["england" , "jersey" , "gurnsey"]]  # its a list inside a list inside a dict
}


# print "gurnsey" from the nested list"
print(travel_log["UK"][1][2])  
    # >> first call the key from dict then the sequencial order of index for list depending on which data u need from which list.


# To append new key:value to a exisiting dictionary 
# SYNTX : dict_name["key"] = value or use the .update() fn for multiple enteries together.


# * in dict , unlike indexation feature like [1] won't call the 2nd item inside the dict ,it requires the specific "key" name

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

# to call "steak" >> syntx : print(order["main"][1]) 
# once you enter the first key inside which a list reside we can use index feature to locate the value


# max() fn : Return the name with the highest value, ordered alphabetically or Return the item in a tuple with the highest value

# SYNTAX max (name of dict , key=dict.get) this will obtain the highest "value" assigned to the key(:) inside the dict.

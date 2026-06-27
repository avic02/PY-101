# def () fn used to create a set a defined commands that allows the user to call
#   repeadtly without performing the whole task step by step

# def my_function (something):  # something = XYZ
    #Do this with (something)
    #Then do this 
    #Then finally do this

# Here inside () is called 'parametr' and XYZ is an 'Argument'
 
#-------------------------------------------X-------------------------------

user_age = int(input("Enter your age :"))

def life_in_weeks():
    age_left = 90-user_age
    weeks_left = age_left * 52 
    print(f"you have {weeks_left} weeks left")

life_in_weeks() 
# --------------------------------------------
# positinal arguments can be replaced and still give same output on changing the order inside ():
# def greet_with(Name , location):
#     print(f"hello {Name} how are you doing , you live here in {location} ? ")

# greet_with("Avinash" , "Delhi")

# def greet_with(Name , location):
#     print(f"hello {Name} how are you doing , you live here in {location} ? ")

# ----------------------------------------------------------
# LOVE CALCULATOR using SYNTAX -> string.count(value, start, end)

name1 = str(input("What is the first persons name :"))
name2 = str(input("what is the 2nd persons name :"))

def calculate_truelove ():
    lower_names = (name1 + name2).lower()
    t = lower_names.count("t")     # remember to attach the "" to represent the string in word for .count() syntax
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    total1= t+r+u+e
    total2= l+o+v+e

    love_calc = int(str(total1) + str(total2))
    print(love_calc)

calculate_truelove()


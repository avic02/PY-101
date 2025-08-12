# LESSON 1- LOOP FN : for item in list: this fn used to iterate through a list
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)

# as there are 3 items in the list, it will iterate through the list 3 times thus carrying out print cmmnd 3 times.
 
# Coding Exercise 1: 
student_heights = input("Input a list of student heights with space \n").split(" ")
for n in range(0,len(student_heights)) :
    student_heights[n] = int(student_heights[n])
print(student_heights)

#now without using sum() or len() we need to calculate the average heights of students 

total_height = 0
for height in student_heights :
    total_height += height
print(total_height)

# this above code has subsituted the fn of sum()

no_of_students = 0 
for student in student_heights :
    no_of_students += 1
print(no_of_students)

# this code has subsituted the fn len()

average_height = round(total_height / no_of_students)

print(f"average of height of the all students entered is : {average_height}")

#------------------------------------------------------------------------------------------------------------------
#Coding ex : high score identifier 

student_scores = input("enter all the scores of the students : \n").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n]) 
print(student_scores)

# without using max() fn seperate the highest score 

highest_score = 0
for score in student_scores :
    if score > highest_score: 
     highest_score = score
print(f"The highest score amogst the students is {highest_score}")


#for loop with range() fn : used to generate a sequence of numbers syntax : range(start,stop,step).

for number in range(1,11,3):
    print(number)

# Coding ex : sum of all even numbers from 1 to 100 :

total = 0
for number in range(2 , 101 , 2):
    print(number)
    total += number
print(total)
#--------------------------------V/S[APPROACH 2]--------------------------
total2 = 0 
for number in range(1,101):
    if number % 2 == 0 : #(because all even numbers give 0 in return for modulo "% 2")
        total2 += number
print(total2)        

#FIZZBUZZ GAME : if the no is div by 3 print fizz ,div by 5 print 'buzz' ,if by both then 'fizzubzz'.

for number in range(1,101):
    
    if number % 5 == 0 and number % 3 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0 :
        print("BUZZ")
    else :
     print(number)           


  


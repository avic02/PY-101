
# DEF fn SYNTAX AND OPERTAIONS:

def my_function ():
    #do this 
    print("Hello, world!")  
    #do that
    print("Goodbye, world!")
    my_function()  # Call the function

#this "def" fn is used to define a fn and then use the calling cmd to perform various actions defined used the fn.


# def move_right():
#     turn_left()
#     turn_left()
#     turn_left()

#  def make_square():  # *use ctrl + [ or ] key to move selected lines of code to diffrent aligment*
#     turn_left()
#     move()
#     move_right()
#     move()
#     move_right()
#     move()
#     move_right()
#     move()
    
# make_square() *go to  reeborg.ca/ to see the robot make a square using def cmnd call a fn.

#*HURDLE JUMPER ROOBORG: for hurdle 1*

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
     
# jump()
# jump()
# jump()
# jump()
# jump()
# jump()

#---------------------------X----------X---------X----------X-------------------------
# !!! OR YOU CAN SUBSITUTE CALLING SAME FN MULTIPLE TIMES BY writing this cmd: (6) is the number of hurdles displayed hence the looping occurs six times .

#>>  for step in range(6):   
#       jump_hurdle()       

# while something_is_true : { SNYTAX OF WHILE LOOP }

number_of_hurdles = 6

while number_of_hurdles > 0 : # This line of code is TRUE hence the while loop will operate the fn inside the indent till the hurdles become = 5 > 4 ....> 0 , here the loop stops since the statement hurdles > 0 has become FALSE!
    print("jump")
    number_of_hurdles -= 1
    print(number_of_hurdles)


# Now if the number of hurdles was randomly decided instead of being fixed (6) then we wld have to use other operators like !=(means not equal to)
#  EX; while at_goal() != True:
#          jump_hurdle()
# or  while not at_goal():
#          jump()     * as soon as the robot reaches the flag it has reached the goal and the while loop ends.




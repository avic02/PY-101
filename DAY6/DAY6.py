#LESSON NO 1: DEF fn introduced

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
    
# make_square() *go to  reeborg.ca/ to see the robot make a square using def cmnd call a fn using make_square().

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

# LESSON NO :2 WHILE LOOPS

# while something_is_true : { SNYTAX OF WHILE LOOP }

number_of_hurdles = 6

while number_of_hurdles > 0 : # This line of code is TRUE hence the while loop will operate the fn inside the indent till the hurdles become = 5 > 4 ....> 0 , here the loop stops since the statement hurdles > 0 has become FALSE!
    print("jump")
    number_of_hurdles -= 1
    print(number_of_hurdles)


# Now if the number of hurdles was randomly decided instead of being fixed (6) then we wld have to use other operators like !=(means not equal to)
while at_goal() != True:
      jump_hurdle()
      while not at_goal():
          jump()     
                     #* as soon as the robot reaches the flag it has reached the goal and the while-loop ends.

#---------------------------X----------X---------X----------X-------------------------SIDENOTE

# for loop VS While loop :
 
# 1. While loop is used when we don't know how many times the loop will run but are dangerous since the loop will keep running repeatedly until the statement becomes false !
# 2. For loop is used when we know how many times the loop will run or we want to iterate new cmnd into prexisting lists , or even use the range function easily.


#---------------------------X----------X---------X----------X-------------------------
# LESSON NO :3 BREAK AND CONTINUE USING IF/ELSE ALONG WITH 
while not at_goal():
    if wall_in_front() :   # each of these IF statements have to be true to execute the cmnd it contains ie; jump() in this case and use False statement for else cmnd.
        jump()
    else:
        move()
        # using if/else conditions to make chanfes in loop 
#LESSON NO 4 : MULTIPLE WHILE CASE SCENARIO FOR ONSPOT DEVIATION IN MAP OF ROBOT >>

def turn_right():
    turn_left()
    turn_left()             #this code (99-102) depicts turning right by individually making left turn thrice to face right.
    turn_left()

def jump():
    turn_left()
    while wall_on_right():  # notice how line(109-111) isn't inside the while indentation(line 106) which implies that it works outside/independat to the while loop.
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():  # we have used 3 whiles out of which 2 are under the jump fn (using DEF cmmnd) 
        move()
    turn_left() #>>>> this left turn is important since the robot wld crash into the bottom wall of map(refer to game site)   

while not at_goal():           #this while statement (line 118) operates outside 
    
    if wall_in_front():
        jump()
        
    else:
        move()

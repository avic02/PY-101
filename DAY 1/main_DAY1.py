# LESSON 1 :using backslash(\) along with n enters strng in nxt line 

print("this is strnd for line 1 \nthis is strng for line 2")


#LESSON 2 :leaving space ie; " world" OR "hello " can help  create space btw 2 words      OR                                   can use "wrd1" +"" +"wrd2" for indent

print("hello" " world")


     #ERROR DEBUGGING EXCERSICE:-Q THEN A:

#print("strng concatenation is done with the"+"sign.") INCORRECT

print('strng concatenation is done with the"+"sign.') 

#LESSON 3 :Build a charcter counter code.

print(len(input("How many chrs in this username?"))) 

#using this code instead of usign len() and count() fn to summarize the code briefly.

#LESSON 4 :How to switch variable values. 
 
 #trick is to introduce a 3rd variable and correleate      all input values with each other[c=a,a=b,b=c]. In print command use print("a =" + a) which will show               RESULT-->   a = b.

a= input("a =?")
b= input("b =?")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)


#The END 

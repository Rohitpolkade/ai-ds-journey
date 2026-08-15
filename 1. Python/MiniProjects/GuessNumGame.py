# Guess the number 
'''pc picks a number & we have to pick the same number'''
'''if our no is less than pc no -->it show result like that ,wise versa'''

import random
#it is a inbuilt module use for creating random number,letter,character
target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit(Q): ")
    
    if(userchoice == "Q"):
        print("Failed")
        break

    userchoice =int(userchoice)
    if(userchoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userchoice <target):
        print("your number is small. Take a bigger Guess")
    else:
        print("your number is bigger.Take a smaller Guess")

print("---game over---")

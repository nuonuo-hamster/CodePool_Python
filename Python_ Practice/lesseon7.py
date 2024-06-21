"""Python 0706 課程7"""

import random

##answer = int( random.random() * 100 ) % 100+ 1
answer = random.randrange( 100 ) 

guess = -1
print("....answer is ",answer,"....")
while(answer != guess):
    
    guess = input("input an digit:")    #this is message
    guess = int(guess)

    if guess > answer:
        print("over")

    elif guess < answer:
        print("not enough")
    
    else:
        print("You just guess it !")

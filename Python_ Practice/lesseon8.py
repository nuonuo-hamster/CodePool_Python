"""Python 0706 課程8"""

import random

#######

seed = random.getstate()

#print(random.getstate())

random.setstate(seed)

while(True):
    x = input("Enter pls ")
    answer = random.randint(1,100)

    if x == "0": break

    else: print("....answer is ",answer,"....")


random.setstate(seed)

while(True):
    x = input("Enter pls")
    answer = random.randint(1,100) 

    print("....answer is ",answer,"....")

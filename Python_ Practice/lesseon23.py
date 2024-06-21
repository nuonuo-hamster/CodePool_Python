"""lesson 23"""

x =[0]*3

print(len(x))

for i in range(len(x)):
    x[i] = [0]*3

print(x,"\n")
for sglMatrix in x:
    for k in sglMatrix:
        print(k,end =" ")
    print()

num = 0

for sglMatrix in x:
    for k in range(len(sglMatrix)):
        num += 1
        sglMatrix[k] = num

print("\n",x,"\n",num)

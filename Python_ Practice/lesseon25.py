"""lesson 25"""
import copy

x = [0]*3
for i in range(3):
    x[i] = [0] * 3

L = len(x)

y = copy.deepcopy(x)
for i in range(0,9):
    y[i // L][i % L] = i+1
    
for i in y:
    for j in i:
        print(j,end = " ")
    print()

z = copy.deepcopy(x)
string = "ABCDEFGHI"
stringLenth = len(string)
No = 0
for i in string:
    z[No // L][No % L] = i
    No += 1
    
for i in z:
    for j in i:
        print(j,end = " ")
    print()

x = []

x = [col for col in range(L)]
print(x)

x = [y[i][2] for i in range(L)]
print(x)

x = [M[2] for M in y]
print(x)

x = [y[i][i] for i in range(L)]
print(x)

x = [y[i][-(i+1)] for i in range(L)]
print(x)

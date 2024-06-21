"""lesson 26"""

x = [[0]*3 for i in range(3)]
print(x)

y = ["Annnnn","Bnnnnn","Cnnnnn","Aaaaa"]
x = [word for word in y if word[0] == "A"]
print(x)

x = [[0,1,2],
     [3,4,5],
     [6,7,8]]
z = [col for row in x for col in row]
print(z)

word = ["ABCD","abcd"]
w = [a+b for a in word[0] for b in word[1]]
print(w)

p = [[A,B] for A in range(1,10) if A % 2 == 0 for B in range(1,10) if B % 3 == 0]
print(p)

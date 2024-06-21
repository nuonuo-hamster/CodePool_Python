# a = input("hi>")
# print(a is '1',bool(""))

# x=[1,2]
# x[2:]=[3,4]
# print(x)

# a="hi"
# b="there"
# print(a,b,sep='',end='')
# print("123")

# x=[[1,2,3],[4,5,6]]
# y=x.copy()
# y[0][0]=100
# x[1][1]=999
# print(x)
# print(y)

# z=[0,0]*3
# z[0]=1
# print(z)

# range_=3    #essential
# w=[0]*range_
# for i in range(range_):
#     w[i]=[0]*3
# w[0][0]=1
# print(w)

# a=[0]*3
# for i in range(3):
#     a[i]=[0]*3
#     for j in range(3):
#         a[i][j]=[0]*3
# print(a,"\n")

# a=[[[1,1,1],[2,2,2],[3,3,3]],[[4,4,4],[5,5,5],[6,6,6]],[[7,7,7],[8,8,8],[9,9,9]]]

# for i in range(9):
#     row=i//3
#     col=i%3
#     if (col==0) & (row!=0): #and
#         print("\n")
#     print(a[row][col],end='')

# x="hello world"
# print(x.find("l"))
# table=str.maketrans("ABCDEF","123456","lov")
# a="I_love_Fish".translate(table)
# print(a)

a="{}{}{}{{}}".format(1,2,3)
b="{:%<10}".format(250)
c="{:_}".format(1000000)
print(a)
print(b)
print(c)
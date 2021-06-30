x=int(input("x:"))
y=int(input("y:"))
z=[]
a=0
for i in range(y):
    z.append(int(input("~")))
for i in range(y):
    if x>=z[i]:
        a+=1
print(a)
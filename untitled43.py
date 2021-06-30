x=int(input("~"))
y=[]
for i in range(x):
    y.append(int(input("~")))
y.sort()
print(y[x-1])
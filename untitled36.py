n=int(input("n(0<n<1000,000):"))
print(n,end=" ")
a=0
while 1:
    if n==1:
        print()
        break;
    else:
        if n%2==1:
            n=3*n+1
        elif n%2==0:
            n=n/2
        print("%d"%(n),end=" ")
        a+=1
print("cycle length:"+str(a+1))
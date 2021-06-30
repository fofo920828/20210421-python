x=input("x:")
y=input("y:")
a=0;
b=0;
for i in range(4):
    for j in range(4):
        if y[i]==x[i]:
            a+=1;
        if y[i]==x[j]:
            b+=1;
print("%dA,%dB"%(a,b))
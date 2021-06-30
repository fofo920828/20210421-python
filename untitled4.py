x=int(input("x:"))
y=int(input("y:"))
if x>0:
    if y>0:
        print("該點位於第一象限,離原點距離為根號%d"%(x^2+y^2))
    elif y<0:
        print("該點位於第四象限,離原點距離為根號%d"%(x^2+y^2))
    elif y==0:
        print("該點位於右半平面x軸上,離原點距離為根號%d"%(x^2+y^2))
elif x<0:
    if y>0:
        print("該點位於第二象限,離原點距離為根號%d"%(x^2+y^2))
    elif y<0:
        print("該點位於第三象限,離原點距離為根號%d"%(x^2+y^2))
    elif y==0:
        print("該點位於左半平面x軸上,離原點距離為根號%d"%(x^2+y^2))
elif x==0:    
    if y>0:
        print("該點位於上半平面y軸上,離原點距離為根號%d"%(x^2+y^2))
    elif y<0:
        print("該點位於下半平面y軸上,離原點距離為根號%d"%(x^2+y^2))
    elif y==0:
        print("該點位於原點")
x=float(input("輸入度數"))
if x<=120:
    print("Summer months:%0.2f"%(x*2.10))
    print("Non-Summer months:%0.2f"%(x*2.10))
elif x>120 and x<=330:
    print("Summer months:%0.2f"%( (x-120)*3.02 + 120*2.1 ))
    print("Non-Summer months:%0.2f"%( (x-120)*2.68 + 120*2.1 ))
elif x>330 and x<=500:
    print("Summer months:%0.2f"%( (x-330)*4.39 + 210*3.02 + 120*2.1 ))
    print("Non-Summer months:%0.2f"%( (x-330)*3.61 + 210*2.68 + 120*2.1 ))
elif x>500 and x<=700:
    print("Summer months:%0.2f"%( (x-500)*4.97 + 170*4.39 + 210*3.02 + 120*2.1 ))
    print("Non-Summer months:%0.2f"%( (x-500)*4.01 + 170*3.61 + 210*2.68 + 120*2.1 ))
elif x>700:
    print("Summer months:%0.2f"%( (x-700)*5.63 + 200*4.97 + 170*4.39 + 210*3.02 + 120*2.1 ))
    print("Non-Summer months:%0.2f"%( (x-700)*4.50 + 200*4.01 + 170*3.61 + 210*2.68 + 120*2.1 ))
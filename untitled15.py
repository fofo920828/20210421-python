# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:32 2021

@author: User
"""

x=input("輸入一組數字:")
y=""
for i in range(len(x)):
    y=y+str((int(x[i])+7)%10)
#print(list(y))
z=""
z=y[2]+y[3]+y[0]+y[1]
print(z)
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:33 2021

@author: User
"""
#not finshed

x=[]
for i in range(3):
    x.append(input("~").split(" "))
    if len(x[i])>3:
        break;
print(list(x))
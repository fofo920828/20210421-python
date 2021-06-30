# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:30 2021

@author: User
"""

m=int(input("m:"))
n=1;
for i in range(1,101):
    n=n*i;
    if n>m:
        print(i);
        break;
    i+=1
    
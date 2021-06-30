# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:49 2021

@author: User
"""

n = int(input("n:"))
k = int(input("k:"))
a = n//k;
while 1:
    n=n+a;
    if a>=k:
        a=a//k;
    else:
        print(n);
        break;
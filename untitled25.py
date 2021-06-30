# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:34 2021

@author: User
"""


z=0;
while 1:
    x=input("x:")
    if x=="end":
        break;
    else:
        y=input("y:")
        z=x.count(y)
        print(z)
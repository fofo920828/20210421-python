# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:22:31 2021

@author: User
"""
#背
data1=input("請輸入一字元為：")
data2=data1[-1::-1]
if data1 == data2:
    print("YES")
else:
    print("NO")
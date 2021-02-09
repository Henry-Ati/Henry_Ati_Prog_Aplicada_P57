# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:28:15 2021

@author: DAVID
"""

while True:
    x=input("Enter a number to count"'\n')
    if x== 'q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print (y)
        y=y+1
        if y>x:
            break
        
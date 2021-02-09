# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:12:31 2021

@author: DAVID
"""

file=open('devices.txt',"a")
while True:
    newItem=input("Ingrese un nuevo Item:")
    if newItem == "exit":
        print("ALL DONE!!")
        break
    else:
        file.write(newItem + "\n")
file.close()
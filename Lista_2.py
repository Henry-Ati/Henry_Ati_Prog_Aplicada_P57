# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:31:41 2020

@author: DAVID
"""

dict1={"R1":"192.168.0.1",
      "R2":"192.168.0.2",
      "R3":"192.168.0.3"}
print(dict1)
print(dict1['R2'])
dict1['R4']="192.168.0.4"
dict1['S3']="192.168.1.4"
print("S5" in dict1)
print("S3" in dict1)

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:13:42 2020

@author: DAVID
"""

nombre=input("Ingrese su nombre"'\n')
apellido=input("Ingrese su apellido"'\n')
edad=input("Ingrese su edad"'\n')
localidad=input("Ingrese su localidad"'\n')
padre=input("Ingresa la edad de tu padre"'\n')
madre=input("Ingresa la edad de tu madre"'\n')
novia=input("Ingresa el nombre de tu novia"'\n')
space=""
print("Hola",nombre,space,apellido,space,"Vives en",localidad,space,"tienes",edad,space,"años")
print(novia,"te pone los cachos")
   
if padre==madre :
    print("Tus padres tiene ",space,padre,space,"años")
   
elif padre<=madre:
     
    print("Tu madre es mayor que tu padre")
elif padre>=madre:
    
    print("Tu padre es mayor que tu madre ")


    

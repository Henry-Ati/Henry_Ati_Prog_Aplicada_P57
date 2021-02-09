# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:03:27 2021

@author: Acer
"""


import urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
key ="xxECUq7fIubJBImLAMjqZNp9qNzDnA0m"
while True:
    orig = input("Starting Location: ")
    if orig == 'quit' or orig == 'q':
        break
    dest = input("Destionation: ")
    if dest == 'quit' or dest == 'q':
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call. \n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"]))
        print("==============================================")
        
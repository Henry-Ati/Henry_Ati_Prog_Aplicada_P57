# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:37:47 2021

@author: DAVID
"""

import urllib.parse
import requests
main_api="https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key ="bVn94C3O4ITcRzJZK1YGC0qSmBu0O3Fl"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL:"+ (url) )
json_data=requests.get(url).json()

json_status= json_data["info"]["statuscode"]
                       
if json_status==0:
    print("API status: " + str(json_status) + "= A successful rute call.\n " )
    
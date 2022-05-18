# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:36:25 2022

@author: oged
"""

import requests

api_file = open('google_api.txt', 'r')
api_key = api_file.read()
api_file.close()

#where are you?
location = input ("Enter a location \n")


#base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

#get response
r = requests.get(url +"origins=" + location + "&destinations= rome" + "&key=" + api_key)

#return time as text.
try:
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]

#print travel time

    print ("\n all roads leads to Rome, it will take you: ", time, "from", location)
    print ("\n your horse will carry you for: ", distance)
except:
    print("there is no roads between " + location +" and Rome.")
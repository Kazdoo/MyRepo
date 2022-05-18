# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:26:33 2022

This program get data regarding earthquakes from Jan - April (included).
There is several alert level (gree, yellow, orange,red) available. 

Date and alert level are currently hard coded but we could easily make that parameter user driven.
The Json is then converted to text to be able to be regex-processed.

we extract 3 fields: date/time, Place and Magnitude.
There is a lot more in the data such as "did that quake triggered a Tsunami" but it is grim enough like that!

These 3 are put in a dictionary which is then published in a text file.




@author: oged
"""


import requests
import json
import re
import datetime


def earthquake(f):
    
    paramss = {"format": "geojson", "starttime": "2022-01-01", "endtime": "2022-04-30", "alertlevel": "yellow"}
    data    = requests.get(f, params = paramss)
    data    = json.loads(data.text)
    data    = json.dumps(data, ensure_ascii=False) #convert JSON to String for Regex later, the 2nd argument is to handle the special characters.

    return data

def main():
    
    
    f = r"https://earthquake.usgs.gov/fdsnws/event/1/query?"
    a = earthquake(f)

    #The Regex part: we are extracting the whole sequence containing the 3 parameters we are interested about.
    pattern = '"mag":\s([0-9]+.[0-9]+),\s"place":\s"(.*?)",\s"time":\s(\d{13})'
    
    result = re.findall(pattern,a)
    
    #dictionary and elements
    #the primary key is the time stamp, so we are using it as a key.
    d = {}
    for i in result:
        print("mag" + i[0] + " city: " + i[1] + " time: " + i[2])
        d[i[2]] = (i[0], i[1])
    
    
    #for the header we do a bit of formating, this is currently hard coded. If we were to make that proper, we could use len().        
    with open("earthquake_report.txt", 'w') as f: 
        template = '%s\t%s\t%s\n'
        f.write(template % ("      Time      ", "Mag", "Place"))
        for key, value in d.items(): 
            mag, city = value
            time = datetime.datetime.fromtimestamp(int(key)/1000.0) #the Json provide miliseconds since 1970. We are formating for humans.
            niceTime = time.strftime("%m/%d/%y %H:%M:%S")

            f.write(template % (niceTime, mag, city))

    
main()

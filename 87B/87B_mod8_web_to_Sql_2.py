# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:06:03 2022

@author: oged
"""

import sqlite3
import ssl
import re
from urllib.request import urlopen

def getMaxDate():
    conn = sqlite3.connect('historical_events.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS HistoricalEvents(date TEXT UNIQUE, numOfEvents INTEGER)')
    
    url = 'https://www.vizgr.org/historical-events/search.php?format=json&begin_date=20000101&end_date=20101231&lang=en'
    context = ssl._create_unverified_context()
    connection = urlopen(url, context = context)
    data = connection.read()
    
    with open('historicalEvents.txt', 'w') as outputFile:
        outputFile.write(data.decode('utf-8'))
    
    historicalEventsFile = open('historicalEvents.txt')
    listOfDates = []
    
    for line in historicalEventsFile:
        line = line.rstrip()
        date = re.findall('\"date\": \"(20[0-9]{2}/[0-9]{2}/[0-9]{2})\"', line)
        if len(date) > 0:
            listOfDates.append(date)
    
    for i in range(len(listOfDates[0])):
        cur.execute('SELECT numOfEvents FROM HistoricalEvents WHERE date = ? LIMIT 1', (str(listOfDates[0][i]),))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE HistoricalEvents SET numOfEvents = ? WHERE date = ?', (count + 1, str(listOfDates[0][i])))
        except:
            cur.execute('INSERT INTO HistoricalEvents (date, numOfEvents) VALUES (?,1)', (str(listOfDates[0][i]),))
    
    data = cur.execute('SELECT date FROM HistoricalEvents WHERE numOfEvents in (SELECT MAX(numOfEvents) FROM HistoricalEvents)') # I believe this command with a subquery is the most useful from those I used as it gives me the value of the field that I am interested in from a condition based on another field
    
    for row in data:
        year = re.findall('(20[0-9]{2})/[0-9]{2}/[0-9]{2}', str(row))
        month = re.findall('20[0-9]{2}/([0-9]{2})/[0-9]{2}', str(row))
        day = re.findall('20[0-9]{2}/[0-9]{2}/([0-9]{2})', str(row))
        dateWithMaxEvents = ''.join(month) + '/' + ''.join(day) + '/' + ''.join(year)
    
    #cur.execute('DROP TABLE IF EXISTS HistoricalEvents')
    conn.commit()
    cur.close() 
    
    print('Between the years 2000 and 2010, the most number of historical events occurred on', dateWithMaxEvents)

def main():
    getMaxDate()
    
main()
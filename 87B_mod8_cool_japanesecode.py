# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:50:40 2022

@author: oged
"""

import json
from urllib.request import urlopen
import sqlite3
import re


# app to get all N5 Vocab ( Lowest Level Japanese Proficiency Test) 
# and put it into a database 

# organize it in an efficient manner and create a function to access vocab by meaning
# also using a user input within a query to give functionality


# requesting all N5 vocabulary from an API containing the vocab needed to pass the N5 Japanese Exam
def get_vocab():
    nfivevocab = dict()

    with urlopen('https://jlpt-keiz.vercel.app/api/words?level=5&limit=1000') as response:
        source = response.read()
    data = json.loads(source)

    for item in data['words']:
        meaning = item['meaning']
        kanji = item['word']
        furigana = item['furigana']
        romaji = item['romaji']
        nfivevocab[meaning] = [kanji, furigana, romaji]

    return nfivevocab


# Creates a database to house the data
def create_database(dictionary):
    connect = sqlite3.connect('N5VOCAB.db')
    cursor = connect.cursor()
    # Creates table
    cursor.execute('''CREATE TABLE IF NOT EXISTS vocab (
                    meaning text,
                    kanji text,
                    furigana text,
                    romaji text,
                    UNIQUE(meaning, kanji, furigana, romaji)
                     )''')

    # Inserts data retrieved from website into database
    for key, value in dictionary.items():
        cursor.execute("INSERT OR IGNORE INTO vocab VALUES (?, ?, ?, ?)", (key, value[0], value[1], value[2]))

    connect.commit()
    connect.close()


# Retrieves specific vocab from database by meaning
def retrieve_vocab():
    connect = sqlite3.connect('N5VOCAB.db')
    cursor = connect.cursor()
    user_input = str(input("What would you like to search from n5 vocab?\n *Search by meaning*\n"))
    try:
        # Selects vocab from user specified selection
        sql_command = "SELECT * FROM vocab WHERE meaning='{}'".format(user_input)
        cursor.execute(sql_command)
        print(cursor.fetchall())
        connect.commit()
    except sqlite3.Error:
        print("Invalid input, try again")

    connect.close()


def main():
    dictionary = get_vocab()
    create_database(dictionary)
    retrieve_vocab()


main()
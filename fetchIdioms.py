import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://www.englishclub.com/ref/Idioms/"


"""listOfIdioms = [
    "a drop in the bucket",
    " a fly on the wall",
    "a hard nut to crack",
    "a little bird told me",
    "a man of few words",
    "a money pit",
    "a needle in a haystack",
    "a nose for something",
    "a small fortune",
    "a ton of",
    "a whale of a time",
    "ants in your pants",
    "apple of your eye",
    "as cool as a cucumber",
    "at a snail’s pace",
    "bad hair day",
    "ball in someone’s court",
    "bark up the wrong tree",
    "bear fruit",
    "beat the pants off",
    "bend over backwards",
    "best thing since sliced bread",
    "bird’s-eye view",
    "blind as a bat",
    "bore the pants off",
    "boxed in",
    "burn the candle at both ends",
    "can of worms",
    "cat and mouse",
    " catch someone’s eye",
    "cat's got your tongue",
    "caught with your pants down",
    "couch potato",
    "count sheep",
    "crack someone up",
    "cry over spilled milk",
    "cry your eyes out",
    "the dead of winter",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]"""

mylist = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W"
]

list = {}
"""idiomsUrls=[]
examples = []
example_list = []"""
data = []

"""for i in range(23):

    list[mylist[i]] = []
    result = requests.get(url+mylist[i]+"/", headers = headers)
    doc = BeautifulSoup(result.text, "html.parser")
    idiomsUrls = doc.select('.linktitle a')

    for tag in idiomsUrls:
        result = requests.get(tag['href'])
        doc = BeautifulSoup(result.text,"html.parser")
        title = doc.find('h1').text
        meaning = doc.find_all('p')[1].text
        examples = doc.find('ul')
        for li in examples.find_all('li'):
            list[mylist[i]].append(example_list.append(li))"""

for i in range(1):

    result = requests.get(url+mylist[i]+"/", headers = headers)
    doc = BeautifulSoup(result.text,"html.parser")

    for tag in doc.select('.linktitle a'):
        result = requests.get(tag['href'])
        doc = BeautifulSoup(result.text,"html.parser")
        data.append({
            'idiom': doc.h1.get_text(strip=True),
            'meaning': doc.select_one('h1 ~ h2 + p').get_text(strip=True),
            'examples':[e.get_text(strip=True) for e in doc.select('main ul li')]
        })



with open('idioms.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)




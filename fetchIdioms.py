import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://www.englishclub.com/ref/Idioms/"



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


array = []

for i in range(23):

    list[mylist[i]] = []
    result = requests.get(url+mylist[i]+"/", headers = headers)
    doc = BeautifulSoup(result.text,"html.parser")

    tempObj = {
        "letter": mylist[i]
    }
    tempArr = []

    for tag in doc.select('.linktitle a'):
        result = requests.get(tag['href'])
        doc = BeautifulSoup(result.text,"html.parser")
        tempArr.append({
            'idiom': doc.h1.get_text(strip=True),
            'meaning': doc.select_one('h1 ~ h2 + p').get_text(strip=True),
            'examples':[e.get_text(strip=True) for e in doc.select('main ul li')]
        })

    tempObj["idioms"] = tempArr
    array.append(tempObj)


with open('idiomsDeneme.json', 'w', encoding='utf-8') as f:
    json.dump(array, f, ensure_ascii=False, indent=4)




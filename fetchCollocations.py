import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://www.englishclub.com/ref/Collocations/"

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


for i in range(23):

    list[mylist[i]] = []
    result = requests.get(url+mylist[i]+"/", headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")
    collocations = doc.find_all(class_="linklisting")

    for tag in collocations:
            case = {
                    "collocation": tag.a.string.replace("\n", ""),
                    "meaning": tag.div.string
            }
            list[mylist[i]].append(case)


with open('CollocationData.json', 'w', encoding='utf-8') as f:

    json.dump(list, f, ensure_ascii=False, indent=4)








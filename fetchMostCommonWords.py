import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://gonaturalenglish.com/1000-most-common-words-in-the-english-language/"

list = []


result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

for tag in doc.find_all('h4'):
    if(tag.strong != None):
        case = {
            "word" : tag.strong.text,
            "meaning": tag.text
        }
    list.append(case)

with open('mostCommonWord.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, indent=4)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grading ID:
Program 4
CIS 443
Due: November 23rd, 2020
This program will scrap files form the internet and compare them for similarity.
In this case we will be looking at MacBeth
"""

import requests
import spacy
from spacy_readability import Readability

nlp = spacy.load('en')
read = Readability()
nlp.add_pipe(read, last=True)

response = requests.get('http://www.gutenberg.org/cache/epub/1795/pg1795-images.html')
response2 = requests.get('https://www.gutenberg.org/files/56463/56463-h/56463-h.htm')
response3 = requests.get('https://www.gutenberg.org/files/18781/18781-h/18781-h.htm')

from bs4 import BeautifulSoup
soup1 = BeautifulSoup(response.content, 'html5lib')
text1 = soup1.get_text(strip=True)

soup2 = BeautifulSoup(response2.content, 'html5lib')
text2 = soup2.get_text(strip=True)

soup3 = BeautifulSoup(response3.content, 'html5lib')
text3 = soup3.get_text(strip=True)

macbeth = nlp(text1)
bacon = nlp(text2)
marlowe = nlp(text3)

print(f'MacBeth vs Sir Francis Bacon similarity score: {macbeth.similarity(bacon)}')
print(f'MaCBeth vs Christopher Marlowe similarity score: {macbeth.similarity(marlowe)}')
#print(f'Article 3 vs article 1 similarity score: {doc3.similarity(doc1)}') 

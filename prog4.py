# -*- coding: utf-8 -*-
"""
Grading ID: 9744
Program 4
Due: Nov 23rd, 2020
CIS 443
This program exploers the use of NLP and web scraping to compare 3 different articles on the same topic.
The program will prompt users to enter a URL for the articles and then compare them.
"""
import requests
import spacy
from spacy_readability import Readability
from textstat.textstat import textstatistics, legacy_round

nlp = spacy.load('en')
read = Readability()
nlp.add_pipe(read, last=True)

user_article = input('Enter article URL: ')
response = requests.get(user_article)
#print(response.content)

from bs4 import BeautifulSoup
soup1 = BeautifulSoup(response.content, 'html5lib')
text1 = soup1.get_text(strip=True)

doc1 = nlp(text1)

article2 = input('Enter another article: ')
response2 = requests.get(article2)

soup2 = BeautifulSoup(response2.content, 'html5lib')
text2 = soup2.get_text(strip=True)

doc2 = nlp(text2)

article3 = input('Enter a thrid article: ')
response3 = requests.get(article3)

soup3 = BeautifulSoup(response3.content, 'html5lib')
text3 = soup3.get_text(strip=True)

doc3 = nlp(text3)

# Splits the text into sentences
def break_sentences(text): 
    # nlp = spacy.load('en') 
    # doc = nlp(text) 
    return text.sents 
  
# Returns Number of Words in the text 
def word_count(text): 
    sentences = break_sentences(text) 
    words = 0
    for sentence in sentences: 
        words += len([token for token in sentence]) 
    return words 
  
# Returns the number of sentences in the text 
def sentence_count(text): 
    sentences = break_sentences(text) 
    sent_count = 0
    for sentence in sentences: 
        sent_count += 1 
    return sent_count 
  
# Returns average sentence length 
def avg_sentence_length(text): 
    words = word_count(text) 
    sentences = sentence_count(text) 
    average_sentence_length = float(words / sentences) 
    return average_sentence_length 

#Returns the # of characters in a word
def character_count(word):
    count = 0
    for char in word:
        count += 1
    return count

#Returns the average number of characters per word in a text
def avg_char_per_word(text):
    character = character_count(text)
    words = word_count(text)
    ACPW = float(character) / float(words)
    return ACPW

# Uses text stat syllable count function to count # of syllables in a word
def syllables_count(word): 
    return textstatistics().syllable_count(word) 

# Returns the average number of syllables per word in a text
def avg_syllables_per_word(text): 
    syllable = syllables_count(text) 
    words = word_count(text) 
    ASPW = float(syllable) / float(words) 
    return legacy_round(ASPW, 1) 

#print(f'Artciel 1 vs article 2 similarity score: {doc1.similarity(doc2)}')
#print(f'Articel 2 vs article 3 similarity score: {doc2.similarity(doc3)}')
#print(f'Article 3 vs article 1 similarity score: {doc3.similarity(doc1)}') 
#print()     
print(f'Grade Level - article 1: {doc1._.flesch_kincaid_grade_level}')
print(f'Grade Level - article 2: {doc2._.flesch_kincaid_grade_level}')
print(f'Grade Level - article 3: {doc3._.flesch_kincaid_grade_level}')
print()
print(f'Reading Ease - artciel 1: {doc1._.flesch_kincaid_reading_ease}')
print(f'Reading Ease - articel 2: {doc2._.flesch_kincaid_reading_ease}')
print(f'Reading Ease - artciel 3: {doc3._.flesch_kincaid_reading_ease}')
print()
print(f'Average # of words per sentences in article 1: {word_count(doc1)/sentence_count(doc1)}')
print(f'Average # of words per sentences in article 2: {word_count(doc2)/sentence_count(doc2)}')
print(f'Average # of words per sentences in article 3: {word_count(doc3)/sentence_count(doc3)}')
print()
#print(f'The average # of syllables per word - Article 1: {avg_syllables_per_word(doc1)}')
#print(f'The average # of syllables per word - Article 2: {avg_syllables_per_word(doc2)}')
#print(f'The average # of syllables per word - Article 3: {avg_syllables_per_word(doc3)}')
print()
print(f'The avergae # of characters per word - Article 1: {abg_char_per_word(doc1)}')
print(f'The avergae # of characters per word - Article 2: {avg_char_per_word(doc2)}')
print(f'The avergae # of characters per word - Article 3: {avg_char_per_word(doc3)}')


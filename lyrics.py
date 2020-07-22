# for timing our program
import timeit

# for sentiment analysis
import nltk
from textblob import TextBlob

# for mathy operations
import math 
import numpy as np

# for making plots
import matplotlib.pyplot as plt

import os

import textblob

start = timeit.default_timer()

# lyricsBlob.words = [word.lower() for word in lyricsBlob.words] # tokenization wordList, not unique
# for word in lyricsBlob.words:
#     if word in ['ass', 'shit', 'cunt', 'fuck', 'crap', 'bitch', 'fucking', 'fuckin', "fuckin'"]:
#         word = 'profanity'

fig = plt.figure()

# converts input in file into a string
filename = input("File to be read: ")
with open(filename, 'r') as file:
    lyrics = file.read().replace('\n', ' ')

lyricsBlob = TextBlob(lyrics)
lyricsBlob.words = [word.lower() for word in lyricsBlob.words] # tokenization wordList, not unique
lyricsList = list(lyricsBlob.words)
lyricsSet = set(lyricsList)

wordFreqs = {}
for word in lyricsSet:
    wordFreqs[word] = lyricsList.count(word)/len(lyricsList)
print(wordFreqs)

# Data to plot
explode = [0]*len(lyricsSet)
explode[0] = 0.1
explode = tuple(explode)  # explode 1st slice

# Plot
plt.pie(wordFreqs.values(), explode=explode, labels=wordFreqs.keys(), autopct='%1.1f%%', shadow=False, startangle=0)
patches, texts = plt.pie(wordFreqs.values(), explode=explode, startangle=0)
plt.legend(patches, wordFreqs.keys(), loc="best")
plt.title(filename + " Distribution of Words")

plt.axis('equal')
plt.tight_layout()

fig.savefig("wordFreqs.jpg")
plt.show()

stop = timeit.default_timer()
time = stop - start
print(str(time) + " microseconds")
# for timing our program
import timeit

# for sentiment analysis
from nltk.corpus import stopwords
from textblob import TextBlob

# for mathy operations
import math 
import numpy as np

# for making plots
import matplotlib.pyplot as plt

import textblob

def main(stopword, curseword, savename="wordFreqs.jpg"):
    start = timeit.default_timer()

    fig = plt.figure()

    # converts input in file into a string
    filename = input("File to be read: ")
    with open(filename, 'r') as file:
        doc = file.read().replace('\n', ' ')

    docBlob = TextBlob(doc)
    docBlob.words = [word.lower() for word in docBlob.words] # tokenization wordList, not unique
    docBlobWords = []
    curseWords = ['ass', 'shit', 'cunt', 'fuck', 'crap', 'bitch', 'fucking', 'fuckin', "fuckin'"]
    for word in docBlob.words:
        if stopword == True:
            if word in set(stopwords.words('english')):
                word = 'stopword'
        if curseword == True:
            if word in curseWords:
                word = 'curseword'
        docBlobWords += [word]

    docList = list(docBlobWords)
    docSet = set(docList)

    wordFreqs = {}
    for word in docSet:
        wordFreqs[word] = docList.count(word)/len(docList)
    print(wordFreqs)

    # Data to plot
    explode = [0]*len(docSet)
    explode[0] = 0.1
    explode = tuple(explode)  # explode 1st slice

    # Plot
    plt.pie(wordFreqs.values(), explode=explode, labels=wordFreqs.keys(), autopct='%1.1f%%', shadow=False, startangle=0)
    patches, texts = plt.pie(wordFreqs.values(), explode=explode, startangle=0)
    plt.legend(patches, wordFreqs.keys(), loc="best")
    plt.title(filename + " Distribution of Words")

    plt.axis('equal')
    # plt.tight_layout()

    fig.savefig(savename)
    plt.show()

    stop = timeit.default_timer()
    time = stop - start
    print(str(time) + " microseconds")

import json
import nltk
import operator
import sys
import re


test = ['Preheat oven to 350 degrees F (175 degrees C). Line a baking sheet with aluminum foil.', 'Mix cream cheese, Cheddar cheese, onion, bacon, jalapeno peppers, cumin, and garlic powder together in a bowl. Spoon cream cheese mixture into each mushroom. Arrange stuffed mushrooms on the prepared baking sheet.', 'Bake in the preheated oven until mushrooms are tender and cheese is melted, 30 to 40 minutes.']

toolList = ['oven', 'sheet', 'foil', 'whisk', 'corer', 'cutter', 'knife', 'fork', 'spoon', 'baster', 'torch', 'opener,' 'bowl', 'tray', 'server', 'dish', 'cheesecloth', 'pitter', 'cleaver', 'corkscrew', 'colander', 'cracker', 'board', 'scraper', 'piercer', 'poacher', 'separator', 'slicer',  'timer', 'sieve', 'sifter', 'mill', 'funnel', 'grater', 'chopper', 'ladle', 'pot', 'measuring', 'grinder', 'processer', 'baller', 'blender', 'pan', 'shears', 'thermometer', 'tongs', 'whisk', 'juicer', 'skillet','saucepan', 'spatula', 'fryer']    ]


def toolFinder(instructions):
    output = []
    wordList = []
    for i in instructions:  # arrange instructions list into list of lists of words
        wordList.append(i.split())
    flattenedWordList = []
    for w in wordList: # flatten list
        for w2 in w:
            flattenedWordList.append(w2)
    for t in toolList: # find matches in list of tools
        for f in flattenedWordList:
            t = re.sub(r'[^\w\s]','',t) # remove punctuation
            f = re.sub(r'[^\w\s]','',f)
            if t.lower() == f.lower(): # ignoring case
                output.append(t)
    output = removeDup(output)
    print output
    return output


def removeDup(seq): # helper function to remove duplicates from list
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]




toolFinder(test)

import json
import nltk
import operator
import sys
import re

testIng = ['1/2 cup butter', '3 tablespoons minced garlic', '3 tablespoons soy sauce', '1 small onion, diced']

test = ['Preheat oven to 400 degrees F (205 degrees C).', 'Pour olive oil in an 8x8-inch glass baking dish. Place the chicken breasts in the dish, coating each side with oil. Squeeze the juice of 1/2 lemon over each chicken breast. Slice the rest of the lemon and place a lemon slice on top of each chicken piece.', 'Bake in the preheated oven until no longer pink in the center and the juices run clear, 30 to 40 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).', 'Melt butter in a skillet over medium heat; add mushrooms. Cook and stir until mushrooms are brown and liquid is evaporated, about 6 minutes. Sprinkle flour over mushrooms and stir until coated. Add chicken broth, stirring to make a medium-thick sauce. Allow sauce to reduce, adjusting with a little more broth to make a creamy sauce. Add fresh parsley at the last minute. Spoon the sauce over the baked chicken breasts.']

stops = ['the', 'a', 'an']

toolList = ['oven', 'sheet', 'foil', 'whisk', 'corer', 'cutter', 'spoon', 'baster', 'torch', 'opener,' 'bowl', 'tray', 'server', 'dish', 'cheesecloth', 'pitter', 'cleaver', 'corkscrew', 'colander', 'cracker', 'board', 'scraper', 'piercer', 'poacher', 'separator', 'slicer',  'timer', 'sieve', 'sifter', 'mill', 'funnel', 'grater', 'chopper', 'ladle', 'pot', 'measuring', 'grinder', 'processer', 'baller', 'blender', 'pan', 'shears', 'thermometer', 'tongs', 'whisk', 'juicer', 'skillet','saucepan', 'spatula', 'fryer',"ladle", "tongs", "spoon", "spatula", "whisk", "knife", "grater", "peeler", "wok",
    "garlic press", "lemon press", "shears", "can opener", "corkscrew", "thermometer", "measuring cup",
    "salad spinners", "colander", "cutting board", "bowl", "saucepan", "(?<!frying |baking )pan", "baking sheet",
    "baking dish", "pot", "skillet", "fork", "forks", "griddle", "microwave", "hot plate",
    "rice cooker", "baster", "cookie cutter", "pastry brush", "rolling pin", "sieve", "stove",
    r"(?<=the )grill", "tin", "tongs", "cookie sheet", "plate", "bag", "foil", "blender", "mixer", "slow cooker",
    "refrigerator", "liner", "toothpick", "cooking spray", "container", "waffle iron", "towel", 
    "roasting rack", "deep fryer", "steamer", "meat grinder", "cutting plate", "paper towel", "Dutch oven",
    "stockpot","sauceboat","skewer","string","frying pan", "baking dish", "baking pan", "loaf pan", "mixing bowl", ]

implyKinfe = ['minced', 'chopped', 'diced', 'sliced', ]



def toolFinder(instructions, ingredients):
    output = []
    newInstructions = []
    for i in instructions:
        sentences = i.split('. ')
        for sen in sentences:
            print sen
            newInstructions.append(sen)
    for i in newInstructions:
        i = i.lower()
        for t in toolList:
            match = re.search(r'\s?'+t+'[\W]?\s|\s'+t+'[\W]?\s?', i)
            if match is not None:
                tool = remove_punc(match.group().strip())
                #tool = addDescriptors(i , remove_punc(match.group().strip()))
                output.append(tool)
    output = checkImply(output, ingredients, instructions)
    output = removeDup(output)
    #print output
    return output

def checkImply(output, ingredients, instructions):
    for ing in ingredients:
        for verb in implyKinfe:
            if verb in ing:
                output.append('knife')
    for i in instructions:
        if 'basting' in i:
            output.append('baster')
    return output


def remove_punc(st):
    not_punct_re = re.compile('\w|\s')
    return ''.join([ch for ch in st if not_punct_re.match(ch)])

def removeDup(seq): # helper function to remove duplicates from list
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

#toolFinder(test, testIng)

import json
import nltk
import operator
import sys
import re

test = ['2/3 large eggs, evenly separated', '5 1/4 teaspoon cream of tartar', '2 ounces cream cheese, very soft', '1 tablespoon white sugar', '1 dash hot pepper sauce (such as Frank\'s RedHot), or to taste']
measurements = ['teaspoon', 'cup', 'tablespoon', 'pound', 'ounce', 'liter', 'gallon', 'quart', 'pint', 'milliliter', 'pinch', 'handful', "dash", 'to taste']
def remove_parens(st):
    #parens = re.compile(r'"([A-Za-z0-9_\./\\-]*)"')
    return re.sub(r'\s?\(.*?\)', '', st)

def find_name(st):
    noMeas = st
    for meas in measurements:
        match = re.search(r''+meas+'s|'+meas+'', st);
        if match is not None:
            noMeas = re.sub(r'\s*'+match.group()+'', '', st)
    start = re.split(r',',noMeas)[0];
    name = re.split(r'\s', start)[-1];
    #print name;
    return name;

def find_quant(st):
    #pattern = r'[0-9]([0-9/\s]*)[0-9]'
    match = re.search(r'[0-9]([0-9/\s]*)[0-9]|[0-9]', st)
    #longest_match = max(matches)
    if match is not None:
        num = match.group();
        if '/' in num:
            whole = 0.0
            frac = 0.0
            wmatch = re.match(r'^[0-9]*\s', st)
            if wmatch is not None:
                whole = float(wmatch.group()[0]);
            denom = float(re.split('/', num)[1])
            numer = float(re.split('/', num)[0][-1])
            #print denom
            frac = round(whole + (numer/denom),3)
            #print frac
            return frac
        else:
            return int(num)
    else:
        return 0

def find_measurement(st):
    for meas in measurements:
        match = re.search(r''+meas+'s|'+meas+'', st);
        if match is not None:
            #print match.group()
            return match.group()
    return "discrete"

def find_descriptor(st, name, meas):
    start = re.split(r''+name+'',st)[0];
    #print start
    middle = re.split(r''+meas+'s|'+meas+'', start)[-1];
    #print middle
    desc = re.split(r'[0-9]\s', middle)[-1];
    #print desc
    if len(desc) > 0:
        if desc[0] is ' ':
            desc = desc[1:]
    if len(desc) > 0:
        if desc[-1] is ' ':
            size = len(desc)-1
            desc = desc[:size]
    #print desc
    if len(desc) > 0:
        return desc
    else:
        return []

def find_prep(st):
    words = re.split(r'\s',st)
    lastW = words[-1];
    match = re.match(r'.*ed$', lastW)
    if match is not None:
        #print match.group()
        return match.group()
    else:
        for word in words:
             match = re.match(r'.*ed$', word)
             if match is not None:
                return match.group()
        return []

def find_prep_descriptor(st):
    words = re.split(r'\s',st);
    check = words[len(words)-2];
    match = re.match(r'.*ly$', check)
    if match is not None:
        #print match.group()
        return match.group()
    else:
        return []          

def findIngredients(ingList):
    parsedIngs = []
    for ing in ingList:
        ing = remove_parens(ing)
        #print ing
        name = find_name(ing)
        meas = find_measurement(ing)
        desc = find_descriptor(ing, name, meas)
        prep = find_prep(ing);
        prepD = None
        if prep is not None:
            prepD = find_prep_descriptor(ing)
        ingDic = {"name": name, "quantity": find_quant(ing), "measurement": meas, "descriptor": desc, "preparation": prep, "prep-description": prepD}
        parsedIngs.append(ingDic);
    print parsedIngs
    return parsedIngs

#findIngredients(test)
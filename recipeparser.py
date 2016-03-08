#!/usr/bin/env python
import re
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

url= "http://allrecipes.com/recipe/246350/easy-cloud-bread/"

def parse_raw(url):

    resp = urllib2.urlopen(url)
    html = resp.read();
    parsed_html = BeautifulSoup(html, "lxml")

    return parsed_html

def parseHtml(url):
    parsed_html = parse_raw(url)
    name = getName(parsed_html)
    ingredients = getIngredients(parsed_html)
    directions = getDirections(parsed_html)
    preptime = getPrep(parsed_html)
    cooktime = getCook(parsed_html)
    #print {"Name" : name, "Ingredients" : ingredients, "Directions" : directions, "Prep Time" : preptime, "Cook Time" : cooktime}
    return {"Name" : name, "Ingredients" : ingredients, "Directions" : directions, "Prep Time" : preptime, "Cook Time" : cooktime}

def getIngredients(html):
    content = html.body.find('ul', attrs={'class':'checklist dropdownwrapper list-ingredients-1'})
    content1 = html.body.find('ul', attrs={'class':'checklist dropdownwrapper list-ingredients-2'})
    ingredient_lis1 = content.findAll('li')
    ingredient_lis2 = content1.findAll('li')
    ingredient_lis = ingredient_lis1 + ingredient_lis2

    ingredients = []
    for ingredient in ingredient_lis:
        ingredient_text = ingredient.find('span').text;
        ingredients.append(ingredient_text)

    #print ingredients
    return ingredients
    
def getDirections(html):
    content = html.body.find('div', attrs={'class':'directions--section__steps'})
    #print content
    direction_lis = content.findAll('li')
    #print instruction_lis

    directions = []
    for direction in direction_lis:
        direction_text = direction.find('span').text;
        directions.append(direction_text)

    #print directions
    return directions


def getName(html):
    content = html.body.find('h1', attrs={'itemprop':'name'})
    name_text =content.text;
    #print name_text
    return name_text

    
def getPrep(html):
    content = html.body.findAll('span', attrs={'class':'prepTime__item--time'})
    prep_text = content[0].text
    #print prep_text
    return prep_text

def getCook(html):
    content = html.body.findAll('span', attrs={'class':'prepTime__item--time'})
    cook_text = content[1].text
    #print cook_text
    return cook_text

parseHtml(url)
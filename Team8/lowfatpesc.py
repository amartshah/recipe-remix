import json
import nltk
import operator
import sys
import re

##testRecipe = {
##     "ingredients":[{
##                    "name": "chicken breast",
## 		    "quantity":	1,
##                    "measurement": "pinch",
## 		    "descriptor": "unsalted",
## 		    "preparation": "",
##                    "prep-description":"none"
## 		    },
##                    {
## 		    "name": "olive oil",
## 		    "quantity":	0.75,
## 		    "measurement": "teaspoon",
##                    "descriptor": "extra-virgin",
## 		    "preparation": "none",
##                    "prep-description":	"none"
## 		    },
##                    {
## 		    "name": "parsley",
## 		    "quantity":	1,
## 		    "measurement":"cup",
## 		    "descriptor": "fresh",
## 		    "preparation": "chopped",
##                     "prep-description": "finely"
##                    }
##        ],
## 	"primary cooking method": "boil",
## 	"cooking methods": ["chop", "stir", "boil", "simmer", "grate", "bake"],
## 	"cooking tools": ["knife", "grater", "dutch oven"],
## 	}



dairy = ['milk','butter', 'cream', 'cheese', 'ricotta', 'mozzarella', 'sour cream', 'cream cheese', 'cottage cheese']
badMethods = ['fry', 'fried', 'sautee', 'pan-fry']
pastaSauces = ['alfredo', 'alfredo sauce','cheese sauce', 'white sauce']
badMeats = ['ground beed','chicken', 'turkey', 'hot dog', 'coldcuts', 'salami', 'pork', 'chorizo', 'anduille']
dressings = ['caesar dressing', 'ranch dressing', 'italian dressing', 'russian dressing', 'caesar', 'ranch', 'french dressing']
soups = ['canned soup', 'cream of tomato soup', 'cream of mushroom soup', 'cream of tomato', 'cream of mushroom']
# lowFat(recipe) checks for high-fat ingredients and replaces with low fat, and checks for unhealthy cooking methods
# and replaces with baking

def lowFat(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for high fat dairy ingredients
        currIngredient = i["name"]
        for d in dairy:
            if currIngredient in d:
                lowFatVersion = "fat free " + currIngredient
                newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for pasta sauce
        currIngredient = i["name"]
        for d in pastaSauces:
            if currIngredient in d:
                lowFatVersion = "marinara sauce"
                newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for granola
        currIngredient = i["name"]
        if "granola" in currIngredient:
            lowFatVersion = "bran flakes"
            newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for ground beef
        currIngredient = i["name"]
        if "ground beef" in currIngredient:
                newRecipe["ingredients"][ingredIndex]["name"] = "ground turkey"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for meats
        currIngredient = i["name"]
        for d in badMeats:
            if currIngredient in d:
                lowFatVersion = "reduced fat " + currIngredient
                newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for dressings
        currIngredient = i["name"]
        for d in dressings:
            if currIngredient in d:
                lowFatVersion = "reduced fat " + currIngredient
                newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for soups
        currIngredient = i["name"]
        for d in soups:
            if currIngredient in d:
                lowFatVersion = "broth-based soup"
                newRecipe["ingredients"][ingredIndex]["name"] = lowFatVersion
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    method = oldRecipe["primary cooking method"] # change primary cooking method if it is high fried/pan fried
    for m in badMethods:
        if m == method:
            newRecipe["primary cooking method"] = "bake"
    return newRecipe


healthyMethods = ['bake', 'baked', 'boil', 'boiled', 'blanched', 'blanch', 'braise', 'braised', 'roast', 'roasted']
leanMeats = ['turkey', 'turkey breast', 'chicken', 'lean']
# hiFat(recipe) checks for low fat ingredients and replaces with whole fat, and checks for healthy cooking methods
# and replaces with frying of some sort
def hiFat(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for reduced fat/skim dairy products
        currIngredient = i["name"]
        if "low fat" in currIngredient or "skim" in currIngredient or "reduced fat" in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "whole fat" + currIngredient
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for pasta sauce
        currIngredient = i["name"]
        if "marinara" in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "alfredo sauce"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for meats
        currIngredient = i["name"]
        for d in leanMeats:
            if currIngredient in d:
                newRecipe["ingredients"][ingredIndex]["name"] = "chicken thigh with skin"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for lean ground meat
        currIngredient = i["name"]
        if "lean" in currIngredient and "ground" in currIngredient:
                newRecipe["ingredients"][ingredIndex]["name"] = "80% ground beef"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for dressings
        currIngredient = i["name"]
        if "low fat" in currIngredient and "dressing" in currIngredient:
                newRecipe["ingredients"][ingredIndex]["name"] = "regular" + currIngredient
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    method = oldRecipe["primary cooking method"] # change primary cooking method if it is high fried/pan fried
    for m in healthyMethods:
        if method in m:
            newRecipe["primary cooking method"] = "fry in duck fat"
    return newRecipe




# toPescetarian checks for both like and hearty meats and then replaces with a more suitably hearty fish type. Also
# checks for meats that may be used more for flavor or to compliment, and replaces those as well
lightMeats = ['chicken', 'chicken breast', 'chicken thigh', 'pork', 'pork chop']
heartyMeats = ['roast', 'salami', 'burger', 'veal', 'venison','beef', 'steak']
complimentaryMeats = ['bacon', 'ham', 'proscuitto']
def toPescatarian(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"]
        for d in lightMeats:
            if currIngredient in d:
                newRecipe["ingredients"][ingredIndex]["name"] = "tilapia filet"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"]
        for d in heartyMeats:
            if currIngredient in d:
                newRecipe["ingredients"][ingredIndex]["name"] = "ahi tuna steak"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"]
        for d in complimentaryMeats:
            if currIngredient in d:
                newRecipe["ingredients"][ingredIndex]["name"] = "canned albacore tuna"
        ingredIndex = ingredIndex + 1
    return newRecipe


# fromPescetarian replaces all fish ingredients with meat/poultry alternatives
otherFish = ['grouper', 'trout', 'whitefish', 'sea bass', 'flounder', 'roughey', 'mahi mahi', 'mahi-mahi']
flavorFish = ['anchovy', 'anchovies','sardines', 'sardine', 'roe', 'caviar', 'smoked salmon']
def fromPescatarian(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for tilapia
        currIngredient = i["name"]
        if "tilapia" in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "chicken breast"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for salmon
        currIngredient = i["name"]
        if "salmon" in currIngredient and "smoked salmon" not in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "pork loin"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for tuna
        currIngredient = i["name"]
        if "tuna" in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "sirloin steak"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for cod
        currIngredient = i["name"]
        if "cod" in currIngredient:
            newRecipe["ingredients"][ingredIndex]["name"] = "chicken cutlet"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for other fish
        currIngredient = i["name"]
        for d in otherFish:
            if d in currIngredient:
                newRecipe["ingredients"][ingredIndex]["name"] = "chicken breast"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for flavoring fish
        currIngredient = i["name"]
        for d in flavorFish:
            if d in currIngredient:
                newRecipe["ingredients"][ingredIndex]["name"] = "prosciutto"
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    return newRecipe

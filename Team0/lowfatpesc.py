import json
import nltk
import operator
import sys
import re

testRecipe = {
    "url": "http://allrecipes.com/Recipe/Easy-Garlic-Broiled-Chicken/",
    "ingredients": [{
            "name": ["butter"],
            "quantity": [0.5],
            "measurement": ["cup", "cups"],
            "descriptor": [],
            "preparation": [],
            "prep-description": [],
            "max": 3
        },
        {
            "name": ["garlic", "minced garlic"],
            "quantity": [3],
            "measurement": ["tablespoons","tablespoon"],
            "descriptor": [],
            "preparation": ["minced"],
            "prep-description": [],
            "max": 4
        },
        {
            "name": ["soy sauce"],
            "quantity": [3],
            "measurement": ["tablespoons", "tablespoon"],
            "descriptor": [],
            "preparation": [],
            "prep-description": [],
            "max": 3
        },
        {
            "name": ["pepper", "black pepper"],
            "quantity": [0.25],
            "measurement": ["teaspoon", "teaspoons"],
            "descriptor": ["black"],
            "preparation": [],
            "prep-description": [],
            "max": 4
        },
        {
            "name": ["parsley", "dried parsley"],
            "quantity": [1],
            "measurement": ["tablespoon", "tablespoons"],
            "descriptor": ["dried"],
            "preparation": ["dried"],
            "prep-description": [],
            "max": 4
        },
        {
            "name": ["chicken","chicken thighs","boneless chicken thighs","boneless chicken","boneless chicken thighs, with skin"],
            "quantity": [6],
            "measurement": ["thighs", "unit", "units","discrete"],
            "descriptor": ["boneless", "with skin", "thighs","boneless thighs, with skin"],
            "preparation": ["boneless","with skin"],
            "prep-description": [],
            "max": 5
        },
        {
            "name": ["parsley", "dried parsley","dried parsley, to taste"],
            "quantity": [0,1,"none"],
            "measurement": ["to taste", "taste"],
            "descriptor": ["dried","dried, to taste"],
            "preparation": ["dried"],
            "prep-description": [],
            "max": 4
        }
    ],
    "max": {
        "ingredients": 27,
        "primary cooking method": 1,
        "cooking tools": 6,
        "cooking methods": 11
    },
    "primary cooking method": "fry",
    "cooking methods":["grease","greasing","preheat","preheating","mix","mixing","melted","melting","arrange","arranging","microwave","microwaving","coat","coating","basting","broil","broiling","turning","sprinkle","sprinkling"],
    "cooking tools": ["oven","knife", "baking pan", "microwave safe bowl", "microwave", "baster"]
}


dairy = ['milk',  'butter', 'cream', 'cheese']
badMethods = ['fry', 'fried', 'sautee', 'pan-fry']

# lowFat(recipe) checks for high-fat dairy ingredients and replaces with low fat, and checks for unhealthy cooking methods
# and replaces with baking

def lowFat(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for high fat dairy ingredients
        currIngredient = i["name"] # list of strings
        for c in currIngredient:
            for d in dairy:
                if c in d:
                    lowFatVersion = "fat free " + c
                    newRecipe["ingredients"][ingredIndex]["name"] = [lowFatVersion]
        ingredIndex = ingredIndex + 1
    method = oldRecipe["primary cooking method"] # change primary cooking method if it is high fried/pan fried
    for m in badMethods:
        if m == method:
            newRecipe["primary cooking method"] = "bake"
    print newRecipe
    return newRecipe
            

# pescetarian checks for both like and hearty meats and then replaces with a more suitably hearty fish type. Also
# checks for meats that may be used more for flavor or to compliment, and replaces those as well

lightMeats = ['chicken', 'chicken breast', 'chicken thigh', 'pork', 'pork chop']
heartyMeats = ['roast', 'salami', 'burger', 'veal', 'venison','beef', 'steak']
complimentaryMeats = ['bacon', 'ham', 'proscuitto']
        
    
def pescetarian(recipe):
    oldRecipe = recipe
    newRecipe = recipe
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"] # list of strings
        for c in currIngredient:
            for d in lightMeats:
                if c in d:
                    pesc1 = "tilapia filet"
                    newRecipe["ingredients"][ingredIndex]["name"] = [pesc1]
        ingredIndex = ingredIndex + 1
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"] # list of strings
        for c in currIngredient:
            for d in heartyMeats:
                if c in d:
                    pesc2 = "ahi tuna steak"
                    newRecipe["ingredients"][ingredIndex]["name"] = [pesc2]
        ingredIndex = ingredIndex + 1 
    ingredIndex = 0
    for i in oldRecipe["ingredients"]: # check for light meats
        currIngredient = i["name"] # list of strings
        for c in currIngredient:
            for d in complimentaryMeats:
                if c in d:
                    pesc3 = "pulled albacore tuna"
                    newRecipe["ingredients"][ingredIndex]["name"] = [pesc3]
        ingredIndex = ingredIndex + 1
    print newRecipe
    return newRecipe


#pescetarian(testRecipe)

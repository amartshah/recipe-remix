
import json
import nltk
import operator
import sys
import re
import urllib

#All subs are pulled from national heart, lung, and blood institute

nonEssentialHighCal = [""]

lowCalStopwords = ["whole milk", "evaporated whole milk","ice cream", "yogurt", "beef","guacamole", "refried beans", "cheese", "mayonnaise", "whipping cream", "sour cream", "cream cheese", "cheese", "mozzarella cheese" ,"bacon", "sausage", "ground beef", "eggs", "chorizo", "margarine", "butter", "salad dressing" ]

lowCalSubsNames = {
	"whole milk": "milk",
	"evaporated whole milk": "milk",
	"ice cream": "sorbet",
	"refried beans": "black beans",
	"mayonnaise": "miracle whip",
	"whipping cream": "cream",
	"sour cream": "yogurt",
	"cream cheese": "cream cheese",
	"cheese": "cheese",
	"mozzarella cheese": "mozzarella cheese",
	"bacon": "ham",
	"sausage": "ham",
	"beef": "beef",
	"guacamole": "salsa",
	"ground beef": "beef",
	"eggs": "egg whites",
	"chorizo": "sausage",
	"margarine": "margarine",
	"fudge sauce": "chocolate syrup",
	"butter": 'butter2.0',
	"salad dressing": "salad dressing",
}

lowCalSubsDescriptor = {
	"whole milk": "skim",
	"evaporated whole milk": "skim",
	"ice cream": "fat-free",				
	"yogurt": "low calorie",
	"refried beans": "low calorie",
	"mayonnaise": "non-fat",
	"whipping cream": "imitation whipped",
	"sour cream": "plain low-fat",
	"cream cheese": "light",
	"cheese": "fat-free",
	"mozzarella cheese": "low-moisture",
	"bacon":"lean",
	"sausage":"lean",
	"beef": "trimmed off external fat",
	"guacamole": "fresh",
	"ground beef":"extra lean ground",
	"eggs":  "",
	"chorizo": "turkey",
	"margarine": "light spread",
	"fudge sauce":  "",
	"butter": "low-calorie whipped",
	"salad dressing": "reduced-calorie",
}

highCalBadwords = ["fat-free", "light", "reduced-calorie", "low-fat", "lean", "non-fat", "low-calorie", "low calorie", "reduced calorie", "low fat", "non fat"]
highCalGoodwords = ["whole", "whole", "high fat", "high fat", "", "fattening"]
lowCalBadwords = ["whole", "high fat"]
lowCalGoodwords = ["reduced-calorie"]




#lowCalGood = ["quinoa", "peanut butter", "avovados", "nuts", "olive oil", "bananas"]
lowSodiumStopwords = ["bacon", "canned fruit", "salt", "broth", "buttermilk", "cheese", "canned vegetables"]
lowSodiumSubNames = {
	"bacon": "bacon",
	"canned fruit": "fruit",
	"salt": "lemon juice",
	"broth": "broth",
	"buttermilk": "milk",
	"cheese": "cheese",
	"canned vegetables": "vegatables",
}

lowSodiumSubDes = {
	"bacon": "turkey",
	"canned fruit": "fresh",
	"salt": "",
	"broth": "reduced sodium",
	"buttermilk": "",
	"cheese":"low sodium",
	"canned vegetables": "low sodium canned",
}

highSodiumBadwords = ["fresh", "unsalted", "reduced sodium", "low sodium"]
lowSodiumBadwords = ["salted", "canned", "cured", "frozen"]
lowSodiumGoodwords= ["fresh"]



# #take this out later
# testRecipe = dict()
# testRecipe = {

# "ingredients":
# [{
# 									"name":	"light salt",
# 									"quantity":	1,
# 									"measurement":	"pinch",
# 									"descriptor":	"unsalted",
# 									"preparation":	"",
# 									"prep-description":	"none"
# 								},
# 								{
# 									"name":	"olive	oil",
# 									"quantity":	0.75,
# 									"measurement":	"teaspoon",
# 									"descriptor":	"extra-virgin",
# 									"preparation":	"none",
# 									"prep-description":	"none"
# 								},
# 								{
# 												"name":	"parsley",
# 												"quantity":	1,
# 												"measurement":	"cup",
# 												"descriptor":	"fresh",
# 												"preparation":	"chopped",
# "prep-description":	"finely"
# 								}],
# 				"primary cooking	method":	"primary	cooking	method	here",
# 				"cooking methods":	["chop",	"stir",	"boil",	"simmer",	"grate", "bake"],
# 				"cooking tools":	["knife",	"grater",	"dutch	oven"],
# 				}


#----------------------------------------------------------------------------------------


#This just makes sure that I didnt make a mistake in commas or something up there
# def testallkeywords(dct):
# 	print dct

# testallkeywords(testRecipe)


#----------------------------------------------------------



def High2LowCal(dct):
	tranrep = dct
	ingredients_current = tranrep["ingredients"]
	for ing in ingredients_current:
		for stopword in lowCalStopwords:
			if stopword in ing['name']:
				ing['name'] = lowCalSubsNames[stopword]
				ing['descriptor'] = lowCalSubsDescriptor[stopword]
	for ing in ingredients_current:
		for badword in lowCalBadwords:
			if badword in ing['name']:
				ing['name'] = ing['name'].replace(badword, lowCalGoodwords[0])
			if badword in ing['descriptor']:
				ing['descriptor'] = ing['descriptor'].replace(badword, lowCalGoodwords[0])
			if badword in ing['preparation']:
				#print ing['preparation']
				ing['preparation'] = ing['preparation'].replace(badword, lowCalGoodwords[0])
				#print ing['preparation']
			if badword in ing['prep-description']:
				ing['prep-description'] = ing['prep-description'].replace(badword, lowCalGoodwords[0])
	#print tranrep
	return tranrep

def LowCal2High(dct):
	tranrep = dct
	ingredients_current = tranrep["ingredients"]
	for ing in ingredients_current:
		for stopword in highCalBadwords:
			if stopword in ing['name']:
				ing['name'] = ing['name'].replace(stopword, "")
	 		if stopword in ing['descriptor']:
				ing['descriptor'] = ing['descriptor'].replace(stopword, "")
	#print tranrep
	return tranrep


def High2LowSodium(dct):
	tranrep = dct
	ingredients_current = tranrep["ingredients"]
	for ing in ingredients_current:
		for stopword in lowSodiumStopwords:
			if stopword in ing['name']:
				ing['name'] = lowSodiumSubNames[stopword]
				ing['descriptor'] = lowSodiumSubDes[stopword]
	for ing in ingredients_current:
		for badword in lowSodiumBadwords:
			if badword in ing['name']:
				ing['name'] = ing['name'].replace(badword, lowSodiumGoodwords[0])
			if badword in ing['descriptor']:
				ing['descriptor'] = ing['descriptor'].replace(badword, lowSodiumGoodwords[0])
			if badword in ing['preparation']:
				ing['preparation'] = ing['preparation'].replace(badword, lowSodiumGoodwords[0])
			if badword in ing['prep-description']:
				ing['prep-description'] = ing['prep-description'].replace(badword, lowSodiumGoodwords[0])
	#print tranrep
	return tranrep

def Low2HighSodium(dct):
	tranrep = dct
	ingredients_current = tranrep["ingredients"]
	for ing in ingredients_current:
		for stopword in highSodiumBadwords:
			if stopword in ing['name']:
				ing['name'] = ing['name'].replace(stopword, "")
	 		if stopword in ing['descriptor']:
				ing['descriptor'] = ing['descriptor'].replace(stopword, "")
	#print tranrep
	return tranrep

#Low2HighSodium(testRecipe)
























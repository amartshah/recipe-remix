
import json
import nltk
import operator
import sys
import re
import urllib

#All subs are pulled from national heart, lung, and blood institute
#The high versions simply just get rid of useless words
#low versions are much better than high versions

nonEssentialHighCal = [""]

lowCalStopwords = ["whole milk", "alfredo sauce","oil" ,"custard", "evaporated whole milk","ice cream", "yogurt", "beef","guacamole", "refried beans", "cheese", "mayonnaise", "whipping cream", "sour cream", "cream cheese", "cheese", "mozzarella cheese" ,"bacon", "sausage", "ground beef", "eggs", "chorizo", "margarine", "butter", "salad dressing" ]

lowCalSubsNames = {
	"whole milk": "milk",
	"oil": "lemon juice",
	"alfredo sauce": "tomato sauce",	
	"evaporated whole milk": "milk",
	"ice cream": "sorbet",
	"refried beans": "black beans",
	"mayonnaise": "miracle whip",
	"whipping cream": "cream",
	"sour cream": "yogurt",
	"cream cheese": "cream cheese",
	"cheese": "cheese",
	"custard": "pudding",	
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
	"butter": 'butter',
	"salad dressing": "salad dressing",
}

lowCalSubsDescriptor = {
	"whole milk": "skim",
	"oil": "low-calorie",
	"alfredo sauce": "low-calorie",	
	"evaporated whole milk": "skim",
	"ice cream": "fat-free",
	"yogurt": "low calorie",
	"refried beans": "low calorie",
	"mayonnaise": "non-fat",
	"whipping cream": "imitation whipped",
	"sour cream": "plain low-fat",
	"cream cheese": "light",
	"cheese": "fat-free",
	"custard": "low-fat",	
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




lowSodiumStopwords = ["bacon", "bread", "mayonnaise", "soy sauce", "canned fruit", "salt", "broth", "buttermilk", "cheese", "canned vegetables"]
lowSodiumSubNames = {
	"bacon": "bacon",
	"canned fruit": "fruit",
	"bread": "tortilla",
	"salt": "lemon juice",
	"soy sauce": "molasses",
	"mayonnaise": "yogurt",
	"broth": "broth",
	"buttermilk": "milk",
	"cheese": "cheese",
	"canned vegetables": "vegatables",
}

lowSodiumSubDes = {
	"bacon": "turkey",
	"canned fruit": "fresh",
	"bread": "corn",
	"mayonnaise": "non-fat",
	"salt": "",
	"soy sauce": "",
	"broth": "reduced sodium",
	"buttermilk": "",
	"cheese":"low sodium",
	"canned vegetables": "low sodium canned",
}

highSodiumBadwords = ["fresh", "unsalted", "reduced sodium", "low sodium"]
lowSodiumBadwords = ["salted", "canned", "cured", "frozen"]
lowSodiumGoodwords= ["fresh"]


def High2LowCal(dct, steps):
	steps1 = steps
	splits = []
	for a in range(0, len(steps1)):
		splits.append(steps1[a].split())
	for stopword in lowCalStopwords:
		for item in range(0, len(splits)):
			for z in range(0, len(splits[item])):
				if stopword == splits[item][z]:
					splits[item][z] = lowCalSubsNames[stopword]
				if stopword + ';' == splits[item][z]:
					splits[item][z] = lowCalSubsNames[stopword]
				if stopword + '.' == splits[item][z]:
					splits[item][z] = lowCalSubsNames[stopword]
				if stopword + ',' == splits[item][z]:
					splits[item][z] = lowCalSubsNames[stopword]
	for a in range(0, len(splits)):
		splits[a] = " ".join(splits[a])
	steps1 = splits
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
				ing['preparation'] = ing['preparation'].replace(badword, lowCalGoodwords[0])
			if badword in ing['prep-description']:
				ing['prep-description'] = ing['prep-description'].replace(badword, lowCalGoodwords[0])
	#print tranrep
	return (tranrep, steps1)

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


def High2LowSodium(dct, steps):
	steps1 = steps
	splits = []
	for a in range(0, len(steps1)):
		splits.append(steps1[a].split())
	for stopword in lowSodiumStopwords:
		for item in range(0, len(splits)):
			for z in range(0, len(splits[item])):
				if stopword == splits[item][z]:
					splits[item][z] = lowSodiumSubNames[stopword]
				if stopword + ';' == splits[item][z]:
					splits[item][z] = lowSodiumSubNames[stopword]
				if stopword + '.' == splits[item][z]:
					splits[item][z] = lowSodiumSubNames[stopword]
				if stopword + ',' == splits[item][z]:
					splits[item][z] = lowSodiumSubNames[stopword]
	for a in range(0, len(splits)):
		splits[a] = " ".join(splits[a])
	steps1 = splits
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
	return (tranrep, steps1)

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

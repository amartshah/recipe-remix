from recipeparser import parseHtml
from cooking_methods import METHODS
from tools import toolFinder
from ingredients import findIngredients

class Parser:
    def __init__(self, url):
        self.full_recipe = None
        self.url = url
        self.parse_html()
        self.get_cooking_methods()

    def __package__(self):
        return self.__name__

    def parse_html(self):
        parsed = parseHtml(self.url)
        self.ingredients = parsed["ingredients"]
        self.steps = parsed["directions"]
        self.cook_time = parsed["cook time"]
        self.prep_time = parsed["prep time"]
        self.name = parsed["name"]

    def separate_ingredients(self):
        return findIngredients(self.ingredients)

    def get_tools(self):
        return toolFinder(self.steps)

    def get_cooking_methods(self):
        self.cooking_methods = []
        self.primary_cooking_method = None

        for m in reversed(METHODS):
            if m in self.name.lower():
                self.primary_cooking_method = m
            self.cooking_methods.append(m)

        for step in reversed(self.steps):
            for m in METHODS:
                if m in step.lower():
                    self.cooking_methods.append(m)
                    if self.primary_cooking_method == None:
                        self.primary_cooking_method = m

    def fully_parsed(self):
        if self.full_recipe == None:
            self.full_recipe = {
                "url": self.url,
                "ingredients": self.separate_ingredients(),
                "primary cooking method": self.primary_cooking_method,
                "cooking methods": self.cooking_methods,
                "cooking tools": self.get_tools()
            }
        print ">>>>>>>>>>>>>>>>>>>>>>"
        print self.full_recipe
        print "<<<<<<<<<<<<<<<<<<<<<<"
        return self.full_recipe

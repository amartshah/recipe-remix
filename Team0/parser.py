from recipeparser import parseHtml
from cooking_methods import METHODS
from tools import toolFinder
from ingredients import findIngredients

class Parser():
    def __init__(self, url):
        self.url = url
        parse_html()

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

    def primary_cooking_method(self):
        pass
        return ""

    def cooking_methods(self):
        self.methods = [m for m in METHODS if m in self.name.lower()]
        if self.methods == []:
            for step in reversed(self.steps):
                self.methods += [m for m in METHODS if m in self.name.lower()]
                if self.methods != []: # depends if too many methods is a problem
                    break

    def fully_parsed(self):
        if not self.full_recipe:
            self.full_recipe = {
                "url": self.url,
                "ingredients": self.separate_ingredients(),
                "primary cooking method": self.primary_cooking_method(),
                "cookings methods": self.cooking_methods(),
                "cooking tools": self.get_tools()
            }
        return self.full_recipe

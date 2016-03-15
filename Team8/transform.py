from change_style import change_style_to
from SodiumAndCal import High2LowCal, High2LowSodium, Low2HighSodium, LowCal2High
from lowfatpesc import lowFat, hiFat, fromPescatarian, toPescatarian
import copy

class Transformer:
    def __init__(self, recipe, steps):
        self.recipe = recipe # see Recipes folder for format
        print steps
        self.steps = steps
        # ["Stir the butter and flour together in a bowl", "cook it for 15 minutes", "etc"]

    def change_style(self, style):
        # handles: vegetarian, vegan, asian, mexican
        new_ingredients, new_steps = change_style_to(style, self.recipe['ingredients'], self.steps)
        new_recipe = copy.deepcopy(self.recipe)
        new_recipe['ingredients'] = new_ingredients
        return (new_recipe, new_steps)

    def low_cal(self):
        return High2LowCal(self.recipe, self.steps)

    def high_cal(self):
        LowCal2High(self.recipe)
        return (self.recipe, self.steps)

    def low_sodium(self):
        #High2LowSodium(self.recipe, self.steps)
        return High2LowSodium(self.recipe, self.steps)

    def high_sodium(self):
        Low2HighSodium(self.recipe)
        return (self.recipe, self.steps)

    def low_fat(self):
        return (lowFat(self.recipe), self.steps)

    def high_fat(self):
        return (hiFat(self.recipe), self.steps)

    def to_pescatarian(self):
        return (toPescatarian(self.recipe), self.steps)

    def from_pescatarian(self):
        return (fromPescatarian(self.recipe), self.steps)

    def transform(self, transformation):
        self.recipe['name'] = (transformation + ' ' + self.recipe['name']).replace('_', ' ').title()
        if transformation == 'asian':
            return self.change_style('asian')
        elif transformation == 'mexican':
            return self.change_style('mexican')
        elif transformation == 'vegetarian':
            return self.change_style('vegetarian')
        elif transformation == 'vegan':
            return self.change_style('vegan')
        elif transformation == 'low_sodium':
            return self.low_sodium()
        elif transformation == 'high_sodium':
            return self.high_sodium()
        elif transformation == 'low_fat':
            return self.low_fat()
        elif transformation == 'high_fat':
            return self.high_fat()
        elif transformation == 'low_cal':
            return self.low_cal()
        elif transformation == 'high_cal':
            return self.high_cal()
        elif transformation == 'non_pescatarian':
            return self.from_pescatarian()
        elif transformation == 'pescatarian':
            return self.to_pescatarian()

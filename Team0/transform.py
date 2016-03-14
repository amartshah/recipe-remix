from change_style import change_style_to
import copy

class Transformer:
    def __init__(self, recipe, steps):
        self.recipe = recipe # see Recipes folder for format
        self.steps = steps
        # ["Stir the butter and flour together in a bowl", "cook it for 15 minutes", "etc"]

    # !!!! READ THIS !!!!
    # All the below methods need to transform and return transformations as tuples:
    # return (recipe, steps)

    def change_style(self, style):
        # Collin
        # handles: vegetarian, vegan, asian, mexican
        new_ingredients, new_steps = change_style_to(style, self.recipe['ingredients'], self.steps)
        new_recipe = copy.deepcopy(self.recipe)
        new_recipe['ingredients'] = new_ingredients
        return (new_recipe, new_steps)

    def low_cal(self):
        # Amar
        pass

    def low_sodium(self):
        # Amar
        pass

    def low_fat(self):
        # Dan
        pass

    def pescatarian(self):
        # Dan
        pass

    # !!!! READ THIS !!!!
    # All the above methods need to transform and return transformations as tuples:
    # return (recipe, steps)

    def transform(self, transformation):
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
        elif transformation == 'low_fat':
            return self.low_fat()
        elif transformation == 'pescatarian':
            return self.pescatarian()

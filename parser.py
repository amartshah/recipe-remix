class Parser():
    def __init__(self, url):
        extract_recipe(url)

    def parse_html(self, url):
        pass

    def extract_recipe(self, url):
        (ingredients, steps, cook_time, prep_time) = parse_html(url)
        self.ingredients = ingredients
        self.steps = steps
        self.cook_time = cook_time
        self.prep_time = prep_time

    def separate_ingredients(self):
        pass

    def get_tools(self):
        pass

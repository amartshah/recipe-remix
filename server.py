from flask import Flask, render_template
from modify import modify_recipe
from parser import extract_recipe


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("api/parse", methods=['POST'])
def parse_this_url():
    """App receives the url of the recipe in the POST
    params, scrapes/parses the recipe, then """
    recipe = extract_recipe(url)

@app.route("api/parse", methods=['POST'])
def mash_up_like_this():
    """This will send the JSON recipe, along with the
    user's selection of bbhow the recipe will be modified.
    We will modify the JSON recipe here, and return it
    to the frontent, still as a JSON object"""
    new_recipe = modify_recipe(recipe, modification)

if __name__ == "__main__":
    app.run(debug=True)
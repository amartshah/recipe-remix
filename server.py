from flask import Flask, render_template, request, jsonify
from Team8.parser import Parser
from Team8.transform import Transformer
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/parse", methods=['POST'])
def parse_this_url():
    """App receives the url of the recipe in the POST
    params, scrapes/parses the recipe, then """
    print request.form
    parser = Parser(request.form['recipeUrl'])
    return jsonify({
        'recipe': parser.fully_parsed(),
        'steps': parser.steps
    })

@app.route("/api/transform", methods=['POST'])
def mash_up_like_this():
    """This will send the JSON recipe, along with the
    user's selection of bbhow the recipe will be modified.
    We will modify the JSON recipe here, and return it
    to the frontent, still as a JSON object"""
    print request.form
    transformer = Transformer(json.loads(request.form['recipe']), json.loads(request.form['steps']))
    (recipe, steps) = transformer.transform(request.form['transformation'])
    return jsonify({
        'recipe': recipe,
        'steps': steps
    })

if __name__ == "__main__":
    app.run(debug=True)

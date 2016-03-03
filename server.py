from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# @app.route("api/url", methods=['POST'])
# def

if __name__ == "__main__":
    app.run(debug=True)

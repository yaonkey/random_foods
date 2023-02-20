from flask import Flask, render_template
from food import get_random_food

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    current_food = get_random_food()
    return render_template("home.html", food=current_food)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(port=5001, host="0.0.0.0")

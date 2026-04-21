import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/guess")
def guess():
    return render_template("guess.html")

@app.route("/guess/<guessed_name>")
def name(guessed_name):

    params = {
        "name": guessed_name
    }

    # API request for age estimation
    response_age = requests.get(url="https://api.agify.io?", params=params)
    text_age = response_age.json()
    age = text_age["age"]

    # API request for gender probability
    response_gender = requests.get(url="https://api.genderize.io?", params=params)
    text_gender = response_gender.json()

    gender = text_gender["gender"]


    return render_template("name.html", name=guessed_name.capitalize(), gender=gender, age=age)


@app.route("/blog")
def blog():
    response_blog = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response = response_blog.json()
    return render_template("blog.html", posts=response)


if __name__ == "__main__":
    app.run(debug=True)


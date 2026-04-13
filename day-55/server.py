from flask import Flask
import random

app = Flask(__name__)

random_n = random.randint(0,9)

@app.route("/")
def welcome():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2xyamxyMTk1ZjFyNWRzcXd0bHF3dWFxNHNwbWxpYTR2dmNsOGk2NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUn3CftPBajoflzROU/giphy.gif' />")

@app.route("/<int:guessed_number>")
def number_too_high(guessed_number):

    if guessed_number > random_n:
        return ("<h1 style='color: orange'>Too high, try again</h1>"
                    "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDBvY3dkcXFtZXU2Zm1vazJuZmZxaWtsZXk4cHY3enA4NzZlaTN5byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YhtiUrWWtpe7QpinHZ/giphy.gif' />")
    elif guessed_number < random_n:
        return ("<h1 style='color: red'>Too low, try again</h1>"
                "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm5kbXJuZGkxMDl0NTU2OHFmbWw1cm00dXdjeXZqb2I4azN4b2l2cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xUOrw3Cbfg9yTWUoaQ/giphy.gif' />")

    else:
        return ("<h1 style='color: green'>You found me</h1>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzAwMnl4YjNtdzUzOTE3cmRlaTdmOHVxZnN1YmdwamJsdWlyeWJxciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTOQHQ9lim011gF80j/giphy.gif' />")

if __name__ == "__main__":
    app.run(debug=True)
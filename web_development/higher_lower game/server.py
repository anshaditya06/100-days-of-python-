from flask import Flask
from random import randint

app = Flask(__name__)

# Generate a random number when the app starts
RANDOM_NUMBER = randint(0, 9)

@app.route("/")
def guess_number():
    return "<h1 style='color: #2E86AB'>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def check_guess(number):
    if number == RANDOM_NUMBER:
        return "<h1 style='color: green'>🎉 You guessed it right!</h1>"
    elif number < RANDOM_NUMBER:
        return "<h1 style='color: orange'>📉 Too low, try again!</h1>"
    else:
        return "<h1 style='color: purple'>📈 Too high, try again!</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from functools import wraps

app = Flask(__name__)

# Decorator for Bold text
def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

# Decorator for Emphasised (Italic) text
def make_italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper

# Decorator for Underlined text
def make_underlined(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

# Example route using all three decorators together
@app.route('/')
@make_bold
@make_italic
@make_underlined
def home():
    return "Welcome to my web application!"

if __name__ == '__main__':
    app.run(debug=True)

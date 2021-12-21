from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


# returns Hello, World
@app.route('/')
def hello_world():
    return 'Hello, World!'


# returns name and number variables inside the page.
@app.route('/<name>/<int:number>')
def hello_user(name, number):
    return f"Hello {name}, you are one of the {number} people who visited the site."


@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


if __name__ == '__main__':
    # debug = True enables debugging and autoload of page.
    app.run(debug=True)

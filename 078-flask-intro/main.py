from flask import Flask
import random

app = Flask(__name__)


@app.route('/flask')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()

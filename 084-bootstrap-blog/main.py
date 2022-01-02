from flask import Flask, render_template
import os

app = Flask(__name__, root_path=os.getcwd())


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page_name>')
def pages(page_name):
    return render_template(f'{page_name}')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)
agify_api = 'https://api.agify.io/'
genderize_api = 'https://api.genderize.io'


@app.route('/')
def home():
    header = "Hello World!"
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)


@app.route('/guess/<name>')
def guess(name):
    check_name = f"{name.title()}"
    api_params = {"name": name}
    print(check_name)
    age = requests.get(url=agify_api, params=api_params).json()['age']
    gender = requests.get(url=genderize_api, params=api_params).json()['gender']
    current_year = datetime.now().year
    return render_template('guess.html', year=current_year, name=check_name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)

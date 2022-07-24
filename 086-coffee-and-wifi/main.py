from asyncore import read
import readline
from sqlite3 import Row
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_bootstrap import Bootstrap
import csv


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[
        DataRequired(), Length(min=4)])
    location = StringField('Location', validators=[
        DataRequired(), Length(min=4), URL()])
    open_time = StringField('Opening Time E.g.8.00 AM', validators=[
        DataRequired(), Length(min=3)])
    close_time = StringField('Closing Time E.g.8.00 PM', validators=[
        DataRequired(), Length(min=3)])
    coffee = SelectField('Coffee Rating', choices=[
        '✖', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], validators=[DataRequired(), Length(min=1)])
    wifi = SelectField('Wifi Strength', choices=[
        '✖', "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired(), Length(min=1)])
    power = SelectField('Power Availability', choices=[
        '✖', "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

data_file = 'cafe-data.csv'


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=["GET", "POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        with open(data_file, "a") as file:
            file.write((
                f"{form.cafe_name.data},{form.location.data},{form.open_time.data},{form.close_time.data},"
                f"{form.coffee.data},{form.wifi.data},{form.power.data}\n"))
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes', methods=["GET"])
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
       csv_data = csv.reader(csv_file, delimiter=',')
       list_of_rows = []
       for row in csv_data:
           list_of_rows.append(row)    
    print(list_of_rows)
    return render_template('cafes.html', data=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)

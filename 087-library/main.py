from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)


# Code to run SQL commands directly inside python
# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title} | {self.author} | {self.rating}>'


db.create_all()
all_books = []


@app.route('/')
def home():
    all_books = db.session.query(Books).order_by(Books.rating.desc()).all()
    return render_template('index.html', data=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['book']
        author = request.form['author']
        rating = request.form['rating']
        new_book = Books(title=title, author=author, rating=rating)
        if new_book.title and new_book.author and new_book.rating:
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('add.html')

    return render_template('add.html')


@app.route('/edit', methods=('GET', 'POST'))
def edit():
    if request.method == "POST":
        rating = request.form['rating']
        id = request.form['id']
        book_to_edit = Books.query.get(id)
        book_to_edit.rating = rating
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template('edit.html', data=book_selected)


@app.route('/delete')
def delete():
    id = request.args.get('id')
    book_selected = Books.query.get(id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

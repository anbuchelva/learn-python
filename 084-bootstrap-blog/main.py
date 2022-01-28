import requests
from flask import Flask, render_template, request
import os
from datetime import datetime
from post import Post
from telegram import send_message

app = Flask(__name__, root_path=os.getcwd())
endpoint = 'https://api.npoint.io/f6a68cce2c012b111224'
posts = requests.get(url=endpoint).json()

post_objects = []
for post in posts:
    date = datetime.now().strftime('%B %d, %Y')
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['date'], post['body'], post['author'])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template('index.html', all_posts=post_objects)


@app.route('/<page_name>')
def pages(page_name):
    if page_name == "index.html":
        return render_template(f'{page_name}', all_posts=post_objects)
    else:
        return render_template(f'{page_name}')


@app.route('/posts/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
            print(blog_post.title)
            return render_template("post.html", post=requested_post)


@app.route('/contact', methods=['POST', 'GET'])
def receive_data():
    print(request.method)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        message_text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        send_message(message_text)
        # return '<h1> Successfully Sent your message!</h1>'
        return render_template('contact.html', h1_message='Successfully Sent your message!')
    else:
        return render_template('contact.html', h1_message='Contact Me')


if __name__ == "__main__":
    app.run(debug=True)

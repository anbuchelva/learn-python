import requests
from flask import Flask, render_template
import os
from datetime import datetime
from post import Post

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


if __name__ == "__main__":
    app.run(debug=True)

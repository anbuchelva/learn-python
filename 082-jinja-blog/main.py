from flask import Flask, render_template
import requests
from post import Post

blog_source_url = 'https://api.npoint.io/4af156202f984d3464c3'
posts = requests.get(url=blog_source_url).json()

post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
            return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

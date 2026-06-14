from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home():
    response = requests.get(BLOG_API)
    posts = response.json()

    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    response = requests.get(BLOG_API)
    posts = response.json()

    selected_post = None
    for post in posts:
        if post["id"] == post_id:
            selected_post = post
            break

    return render_template("post.html", post=selected_post)

if __name__ == "__main__":
    app.run(debug=True)


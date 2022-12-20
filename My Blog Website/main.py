from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/dfdffb31b3c8375aca7c"
response = requests.get(blog_url)
all_posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return render_template("post.html", post_data=all_posts[post_id])


@app.route("/about")
def get_about_page():
    return render_template("about.html")


@app.route("/contact")
def get_contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

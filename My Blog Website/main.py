from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
server_address = "your email"
server_password = "your email password"
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


@app.route("/contact", methods=["GET", "POST"])
def get_contact_page():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        email_msg = f"Name: {name} \nEmail: {email} \nPhone: {phone} \nMessage: {message} \n"
        print(email_msg)
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=server_address, password=server_password)
            connection.sendmail(from_addr=server_address, to_addrs=server_address, msg=f"Subject:Server Message \n\n{email_msg}")

        return render_template("contact.html", is_message_sent="True")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.secret_key = "dsjhfandkjfns98sdfjha7fsdfs998dfss"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(100), nullable=False, unique=True)
    body = db.Column(db.String(300), nullable=False)


db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        new_task = Task(
            heading=request.form["heading"],
            body=request.form["body"]
        )
        if new_task.heading and new_task.body:
            db.session.add(new_task)
            db.session.commit()
    tasks_data = db.session.query(Task).all()
    return render_template("tasks.html", tasks=tasks_data)


if __name__ == "__main__":
    app.run(debug=True)

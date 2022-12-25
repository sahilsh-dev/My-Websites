from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from forms import RateMovieForm, AddMovieForm
import tmdbsimple as tmdb

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-database.db"
app.app_context().push()
db = SQLAlchemy(app)
tmdb.API_KEY = "your_api_key"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(100))
    img_url = db.Column(db.String(200))


db.create_all()
new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
db.session.add(new_movie)
db.session.commit()


@app.route("/")
def home():
    movies_list = db.session.query(Movie).all()
    return render_template("index.html", movies=movies_list)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("movie_id")
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_data_to_update = Movie.query.get(movie_id)
        movie_data_to_update.rating = form.rating.data
        movie_data_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", id=movie_id, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_name = form.title.data
        search = tmdb.Search()
        response = search.movie(query=movie_name)
        search_movies_list = response['results'][:12]
        return render_template("select.html", search_list=search_movies_list)

    # Add new movie to the list
    if request.args.get("movie_title"):
        new_movie = Movie(
            title=request.args.get("movie_title"),
            year=request.args.get("movie_date")[:4],
            description=request.args.get("movie_description"),
            img_url="https://image.tmdb.org/t/p/w500" + request.args.get("movie_img_url")
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=new_movie.id))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

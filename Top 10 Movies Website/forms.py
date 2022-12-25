from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating 10 e.g. 7.5",
                        validators=[DataRequired()])
    review = StringField("Your Review",
                         validators=[DataRequired()])
    submit = SubmitField("Done")

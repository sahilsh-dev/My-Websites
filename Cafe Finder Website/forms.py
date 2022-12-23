from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField
from wtforms.validators import Length, URL


class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name",
                            validators=[Length(4, 30)])
    location = URLField(label="Cafe Location on Google Map(URL)",
                        validators=[URL()])
    opening_time = TimeField(label="Opening Time e.g. 8:00AM")
    closing_time = TimeField(label="Closing Time e.g. 5:30PM")
    coffee_rating = SelectField(label="Coffee Rating",
                                choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"])
    wifi_rating = SelectField(label="Wifi Strength Rating",
                              choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_availability = SelectField(label="Power Socket Availability",
                                     choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label="Submit")

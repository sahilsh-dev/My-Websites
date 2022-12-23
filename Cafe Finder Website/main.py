from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import csv
from forms import CafeForm

app = Flask(__name__)
app.secret_key = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a") as file:
            cafe_data = f"{form.cafe_name.data},{form.location.data},{form.opening_time.data.strftime('%I:%M%p')}," \
                        f"{form.closing_time.data.strftime('%I:%M%p')},{form.coffee_rating.data}," \
                        f"{form.wifi_rating.data},{form.power_availability.data}\n"
            file.write(cafe_data)
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv') as csv_file:
        data = csv.reader(csv_file)
        list_of_rows = []
        for row in data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

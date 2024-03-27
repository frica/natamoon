import datetime

import ephem
from babel.dates import format_date, format_datetime
from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    date_today = datetime.date.today()
    date_time_full_moon = ephem.next_full_moon(date_today)
    date_today = format_date(date_today, locale='FR')
    date = format_datetime(date_time_full_moon.datetime(), locale='FR')

    return render_template("index.html", today=date_today, date=date)


@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')


@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')


if __name__ == '__main__':
    app.run(debug=True)

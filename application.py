from __future__ import print_function
from flask import Flask, render_template
from datetime import date, timedelta
import calendar
import sys

app = Flask(__name__)

@app.route('/')
def current_week():

    week_start = get_week_start(date.today(), calendar.SATURDAY)
    week_dates = [week_start + timedelta(days=n) for n in range(7)]
    lunches = [d.strftime("%Y%m%dl") for d in week_dates]
    dinners = [d.strftime("%Y%m%dd") for d in week_dates]
    # print(week_dates, file=sys.stderr)
    return render_template('index.html', dates=week_dates, lunches=lunches, dinners=dinners)

def get_week_start(week_date, start_day):
    differ = 0
    if start_day > 0:
      differ = 7 - start_day
    differ = differ + week_date.weekday()
    return week_date - timedelta(days=differ)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        start_time = request.form['start-time']
        break_time = request.form['break-time']
        gamezone_time = 0
        if request.form.get("gamezone-time") == "yes":
            gamezone_time = 15
        # Call your Python function to calculate the result
        result = calculate_time(start_time, break_time, gamezone_time)

        return render_template('index.html', result=result)

    return render_template('index.html')


def calculate_time(start_time, break_time, gamezone_time):
    entry_time = datetime.strptime(start_time, "%H:%M")
    total_work_time = timedelta(hours=9) + entry_time
    remaining_time_minutes = 40 - int(break_time) - int(gamezone_time)
    if remaining_time_minutes > 0:
        total_work_time -= timedelta(minutes=remaining_time_minutes)
    else:
        total_work_time += timedelta(minutes=abs(remaining_time_minutes))
    return total_work_time.strftime("%H:%M")


if __name__ == '__main__':
    app.run(debug=True)

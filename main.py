# code coming soon.

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def age_calculator():
    age = None

    if request.method == 'POST':
        birthdate = request.form['birthdate']
        
        try:
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        except ValueError:
            error_message = "Invalid date format. Please use YYYY-MM-DD."

            return render_template('index.html', error_message=error_message)

    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)


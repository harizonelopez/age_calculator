from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def age_calculator():
    age_years = None
    age_months = None
    age_days = None

    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            month = int(request.form['month'])
            day = int(request.form['day'])
        
            birthdate = datetime(year, month, day)
            today = datetime.now()
            
            age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            
            birthdate_anniversary = datetime(today.year, month, day)
            if today >= birthdate_anniversary:
                age_months = today.month - birthdate_anniversary.month
                age_days = today.day - birthdate_anniversary.day
            else:
                age_months = (today.month - birthdate_anniversary.month - 1 + 12) % 12
                age_days = (today.day - birthdate_anniversary.day + 30) % 30

        except ValueError:
            error_message = "Invalid date inputs. Please enter valid numerical values for year, month and day."

            return render_template('home.html', error_message=error_message)

    return render_template('home.html', age_years=age_years, age_months=age_months, age_days=age_days)

if __name__ == '__main__':
    app.run(debug=True)
